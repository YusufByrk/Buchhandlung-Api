from fastapi import FastAPI, BackgroundTasks, HTTPException
import sqlite3 as sql
from buchhandel_classen import Buecher, E_Buecher, Filme, Backstocks, Drink
import pandas as pd
from typing import Union, List
from datetime import datetime


app = FastAPI()

############### BOOKS ##################
def buch_db_conn():
    conn = sql.connect("Buchhandlung.db")
    cursor = conn.cursor()
    return cursor

@app.get("/")
async def root():
    return "Herzlich Willcommen Buchhandel 1.0"

############## Backgroundtask ##############

def write_notification(message:str):
    with open("C:\\Users\\Admin\\Desktop\\DATA-CRAFT\\Praxisproject 3\\Buchhandlung Api\\logdatei\\log.txt", mode ="w") as message_file:
        content = f"This user was added: {message} at this time {datetime.now()}"
        message_file.write(content)

############## get all products #############

@app.get("/books")
async def get_all_books():
    cursor_b = buch_db_conn()
    data = cursor_b.execute("SELECT * FROM books where AufLager > 0").fetchall()
    return data

@app.get("/e_books")
async def get_all_e_books():
    cursor_b = buch_db_conn()
    data = cursor_b.execute("SELECT * FROM e_books").fetchall()
    return data

@app.get("/films")
async def get_all_films():
    cursor_b = buch_db_conn()
    data = cursor_b.execute("SELECT * FROM films where AufLager > 0").fetchall()
    return data

############## get one product by id #############

@app.get("/books/{id}")
async def get_book_id(book_id:int):
    cursor_b = buch_db_conn()
    data = cursor_b.execute(f"SELECT * FROM books where book_id = {book_id}").fetchone()
    return data

@app.get("/e_books/{id}")
async def get_e_books_id(id:int):
    cursor_b = buch_db_conn()
    data = cursor_b.execute(f"SELECT * FROM e_books where e_book_id = {id}").fetchone()
    return data

@app.get("/films/{id}")
async def get_films_id(id:int):
    cursor_b = buch_db_conn()
    data = cursor_b.execute(f"SELECT * FROM films where film_id = {id}").fetchone()
    return data

############### Gesamt Waren ##############

@app.get("/total")
async def get_total():
    cursor_b = buch_db_conn()
    summe_book = cursor_b.execute("SELECT sum(AufLager) FROM books").fetchone()[0]
    summe_film = cursor_b.execute("SELECT sum(AufLager) FROM films").fetchone()[0]
    return f"Gesamtzahl der vorrätigen Bücher: {summe_book}\nGesamtzahl der vorrätigen Filme: {summe_film}"

############### POST ##############

# post for books
@app.post("/books", status_code=201)
async def add_book(books: Buecher, background_tasks:BackgroundTasks):
    cursor_b = buch_db_conn()
    cursor_b.execute('INSERT INTO books (Titel, Autor, Erscheinungsjahr, Herausgeber, Seitenanzahl, Preis, AufLager) VALUES (?,?,?,?,?,?,?);', 
                    (books.Titel, 
                    books.Autor, 
                    books.Erscheinungsjahr, 
                    books.Herausgeber, 
                    books.Seitenanzahl, 
                    books.Preis, 
                    books.AufLager))
    cursor_b.execute("commit")   
    background_tasks.add_task(write_notification, message=books) 
    return {"message": "Book/books added successfully"}


# post for e_books


@app.post("/e_books", status_code=201)
async def add_ebook(e_b: E_Buecher, background_tasks:BackgroundTasks):
    cursor_b = buch_db_conn()
    cursor_b.execute('INSERT INTO e_books (Titel, Autor, Erscheinungsjahr, Herausgeber, Seitenanzahl, Preis) VALUES (?,?,?,?,?,?);', 
                           (e_b.Titel, 
                            e_b.Autor, 
                            e_b.Erscheinungsjahr, 
                            e_b.Herausgeber, 
                            e_b.Seitenanzahl, 
                            e_b.Preis))
    cursor_b.execute("commit")    
    message = f"{e_b} added successfully"
    background_tasks.add_task(write_notification, message=message) 
    return {"message": message}

# post for films

@app.post("/films", status_code=201)
async def add_film(film:Filme, background_tasks:BackgroundTasks):
    cursor_b = buch_db_conn()
    cursor_b.execute('INSERT INTO films (Titel, Produzent, Erscheinungsjahr, Preis, AufLager) VALUES (?,?,?,?,?);', 
                           (film.Titel, 
                            film.Produzent, 
                            film.Erscheinungsjahr,  
                            film.Preis, 
                            film.AufLager))
    cursor_b.execute("commit")    
    background_tasks.add_task(write_notification, message=film)     
    return {"message": "Film/films added successfully"}


############### PUT ##############

# update books
@app.put("/books/")
async def update_book(book_id: int, book: Buecher, background_tasks:BackgroundTasks):
    cursor_b = buch_db_conn()
    cursor_b.execute('''UPDATE books SET
                        Titel = ?,
                        Autor = ?,
                        Erscheinungsjahr = ?,
                        Herausgeber = ?,
                        Seitenanzahl = ?,
                        Preis = ?,
                        AufLager = ?
                        WHERE book_id = ?''',
                      (book.Titel, book.Autor, book.Erscheinungsjahr, book.Herausgeber, book.Seitenanzahl, 
                       book.Preis, book.AufLager, book_id))
    cursor_b.execute('commit')
    background_tasks.add_task(write_notification, message=book)   
    return f"message: {cursor_b.rowcount} eintrager wurde aktualisiert"


# book preis change
@app.put("/books/{book_id}")
async def update_book_preis(book_id: int, preis: float, background_tasks:BackgroundTasks):
    cursor_b = buch_db_conn()
    cursor_b.execute("UPDATE books SET Preis = ? WHERE book_id = ?", (preis, book_id))
    cursor_b.execute('commit')
    background_tasks.add_task(write_notification, message=f"{book_id}{preis}")
    return f"message: {cursor_b.rowcount} eintrag wurde aktualisiert"

# ebook update
@app.put("/e_books/")
async def update_e_book(id: int, e_book: E_Buecher, background_tasks:BackgroundTasks):
    cursor_b = buch_db_conn()
    cursor_b.execute('''UPDATE e_books SET
                        Titel = ?,
                        Autor = ?,
                        Erscheinungsjahr = ?,
                        Herausgeber = ?,
                        Seitenanzahl = ?,
                        Preis = ?
                        WHERE e_book_id = ?''',
                      (e_book.Titel, e_book.Autor, e_book.Erscheinungsjahr, e_book.Herausgeber, e_book.Seitenanzahl, 
                       e_book.Preis, id))
    cursor_b.execute('commit')
    background_tasks.add_task(write_notification, message=e_book)   
    return f"message: {cursor_b.rowcount} eintrager wurde aktualisiert"


# e_book preis change
@app.put("/e_books/{e_book_id}")
async def update_e_book_preis(e_book_id: int, preis: float, background_tasks:BackgroundTasks):
    cursor_b = buch_db_conn()
    cursor_b.execute("UPDATE e_books SET Preis = ? WHERE e_book_id = ?", (preis, e_book_id))
    cursor_b.execute('commit')
    background_tasks.add_task(write_notification, message=f"{e_book_id}{preis}")
    return f"message: {cursor_b.rowcount} eintrag wurde aktualisiert"


# film update

@app.put("/films/")
async def update_films(id:int, film:Filme, background_tasks:BackgroundTasks):
    cursor_b = buch_db_conn()
    cursor_b.execute('''UPDATE films SET
                        Titel = ?,
                        Produzent = ?,
                        Erscheinungsjahr = ?,
                        Preis = ?,
                        AufLager = ?
                        WHERE film_id = ?''',
                      (film.Titel, film.Produzent, film.Erscheinungsjahr,
                       film.Preis, film.AufLager, id))
    cursor_b.execute('commit')
    background_tasks.add_task(write_notification, message=film) 
    return f"message: {cursor_b.rowcount} eintrager wurde aktualisiert"


# film preis change
@app.put("/films/{film_id}")
async def update_film_preis(film_id: int, preis: float, background_tasks:BackgroundTasks):
    cursor_b = buch_db_conn()
    cursor_b.execute("UPDATE films SET Preis = ? WHERE film_id = ?", (preis, film_id))
    cursor_b.execute('commit')
    background_tasks.add_task(write_notification, message=film_id)
    return f"message: {cursor_b.rowcount} eintrag wurde aktualisiert"


############### DELETE ##############
#delete book
@app.delete("/books")
async def delete_book(id:int, background_tasks:BackgroundTasks):
    cursor_b = buch_db_conn()
    cursor_b.execute("DELETE FROM books WHERE book_id = :id", {"id": id})
    cursor_b.execute('commit')
    background_tasks.add_task(write_notification, message=id)
    return f"message: {cursor_b.rowcount} eintrager wurde gelöscht"

#delete e book
@app.delete("/e_books")
async def delete_ebook(id:int, background_tasks:BackgroundTasks):
    cursor_b = buch_db_conn()
    cursor_b.execute("DELETE FROM books WHERE book_id = :id", {"id": id})
    cursor_b.execute('commit')
    background_tasks.add_task(write_notification, message=id)
    return f"message: {cursor_b.rowcount} eintrager wurde gelöscht"

#delete film
@app.delete("/films")
async def delete_film(id:int, background_tasks:BackgroundTasks):
    cursor_b = buch_db_conn()
    cursor_b.execute("DELETE FROM films WHERE film_id = :id", {"id": id})
    cursor_b.execute('commit')
    background_tasks.add_task(write_notification, message=id)
    return f"message: {cursor_b.rowcount} eintrager wurde gelöscht"


############### CAFE ##############
def back_db_conn():
    conn = sql.connect("Cafe.db")
    cursor = conn.cursor()
    return cursor


############# Backstock get all #################
@app.get("/backstock")
async def get_all_backstock():
    cursor_c = back_db_conn()
    data = cursor_c.execute("SELECT * FROM backstock where Bestand > 0").fetchall()
    return data


############# Backstock add #################

@app.post("/backstock", status_code=201)
async def add_produkt(bc: Union[Backstocks, list[Backstocks]], background_tasks:BackgroundTasks):
    cursor_c = back_db_conn()
    if isinstance(bc, list):
        for b in bc:
            cursor_c.execute('INSERT INTO backstock VALUES (?,?);', (b.Produkt, b.Bestand))
    else:
        cursor_c.execute('INSERT INTO backstock VALUES (?,?);', (bc.Produkt, bc.Bestand))
    cursor_c.execute("commit")    
    background_tasks.add_task(write_notification, message=bc)     
    return {"message": "Backstock added successfully"}


############# Backstock update #################

@app.put("/backstock/{produkt}")
async def update_pro_bestand(produkt: str, bestand: int, background_tasks: BackgroundTasks):
    cursor_c = back_db_conn()
    cursor_c.execute("UPDATE backstock SET Bestand = ? WHERE Produkt = ?", (bestand, produkt))
    cursor_c.execute('commit')
    background_tasks.add_task(write_notification, message=produkt)
    return f"message: {cursor_c.rowcount} eintrag wurde aktualisiert"

############# Backstock delete #################

@app.delete("/backstock/{produkt}")
async def delete_produkt(produkt:str, background_tasks: BackgroundTasks):
    cursor_c = back_db_conn()
    cursor_c.execute("DELETE FROM backstock WHERE Produkt = ?", (produkt, ))
    cursor_c.execute('commit')
    background_tasks.add_task(write_notification, message=produkt)
    return f"message: {cursor_c.rowcount} eintrag wurde gelöscht"



######################### drinks ##################


@app.get("/drinks/")
async def get_drink_report():
    cursor_c = back_db_conn()
    report = cursor_c.execute("SELECT kategorie, sum(Anzahl), sum(Preis) FROM Drinks GROUP BY kategorie").fetchall()
    return report

##### bestellung hinzufügen ######

# bestellung giriş
@app.post("/Bestellung", status_code =201)
async def add_bestellung(category:str, zahl:int, background_tasks:BackgroundTasks):
    cursor_c = back_db_conn()
    cursor_c.execute('INSERT INTO Drinks (kategorie, Anzahl, Preis) VALUES (?,?,?);', (category, zahl, f"{zahl*3}"))
    cursor_c.execute('commit')
    background_tasks.add_task(write_notification, message=category)
    return f"message: This order is succesfully added."







