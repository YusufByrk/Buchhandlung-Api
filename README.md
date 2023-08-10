**English README:**

# Bookstore Management API

You have been tasked with creating an API for managing products in a bookstore. The bookstore specializes in providing comprehensive services to its customers and sells not only books but also e-books, movies, and coffee in its in-house café.

Your task is to create an API that allows queries to be made about the available products. To create a better structure, the bookstore has decided to store the data for books, e-books, and movies in one database, and the café's data in another database. This means that your API needs to interact with two databases, each with its own set of functions.

For each product, the following calls should be possible:
- Retrieve individual items (e.g., book, movie) by ID
- Retrieve all entries
- Add an entry
- Modify an entry
- Remove an entry

All changes within the two datasets should be traceable through an appropriate log file; it should record which change (addition / update / removal) occurred at what time (timestamp), on which entry (ID), and with what content (specification of column contents).

The following contents are the minimum requirements for your API databases. You can certainly add additional columns if you deem it necessary.

Product Databases (Books, E-Books, Movies):

Book:
- Title
- Author
- Publication Year
- Publisher
- Number of Pages
- ID
- Price
- In Stock

E-Book:
- Title
- Author
- Publication Year
- Publisher
- Number of Pages
- ID
- Price

Movie:
- Title
- Producer
- Release Year
- ID
- Price
- In Stock

Café Database:

Backstock: (Quantity of available items, e.g., Milk, indicated by a number)
- Cow's Milk
- Oat Milk
- Coffee Beans
- Lemonade
- Apple Spritzer
- Water

Latte:
- Price
- ID
- Order Date

Americano:
- Price
- ID
- Order Date

Lemonade:
- Price
- ID
- Order Date

Apple Spritzer:
- Price
- ID
- Order Date

In addition to the described functions, the manager would also like to quickly retrieve the total number of products currently in the bookstore (excluding the café) along with their total value.

----------------

**Deutsche README:**

# API für Buchhandlungsverwaltung

Du wurdest beauftragt, eine API für die Verwaltung von Produkten in einer Buchhandlung zu erstellen. Die Buchhandlung hat sich darauf spezialisiert, ihren Kunden umfassende Dienstleistungen anzubieten und verkauft neben Büchern auch E-Books, Filme und Kaffee in ihrem eigenen Café.

Deine Aufgabe besteht darin, eine API zu erstellen, die Abfragen zu den verfügbaren Produkten ermöglicht. Um eine bessere Struktur zu schaffen, hat sich die Buchhandlung entschieden, die Daten für Bücher, E-Books und Filme in einer Datenbank und die Daten des Cafés in einer anderen Datenbank zu speichern. Das bedeutet, dass deine API mit zwei Datenbanken interagieren muss, von denen jede ihre eigenen Funktionen hat.

Für jedes Produkt sollten folgende Aufrufe möglich sein:
- Einzelne Einträge (z.B. Buch, Film) anhand der ID abrufen
- Alle Einträge abrufen
- Einen Eintrag hinzufügen
- Einen Eintrag ändern
- Einen Eintrag entfernen

Alle Änderungen in den beiden Datensätzen sollten über eine entsprechende Logdatei nachvollziehbar sein. Diese sollte erfassen, welche Änderung (Hinzufügen / Aktualisieren / Entfernen) zu welchem Zeitpunkt (Zeitstempel), an welchem Eintrag (ID) und mit welchem Inhalt (Angabe der Spalteninhalte) vorgenommen wurde.

Die folgenden Inhalte sind das Mindeste für deine API-Datenbanken. Du kannst selbstverständlich zusätzliche Spalten hinzufügen, wenn du dies für sinnvoll hältst.

Datenbanken für Produkte (Bücher, E-Books, Filme):

Buch:
- Titel
- Autor
- Erscheinungsjahr
- Herausgeber
- Anzahl der Seiten
- ID
- Preis
- Auf Lager

E-Book:
- Titel
- Autor
- Erscheinungsjahr
- Herausgeber
- Anzahl der Seiten
- ID
- Preis

Film:
- Titel
- Produzent
- Erscheinungsjahr
- ID
- Preis
- Auf Lager

Café-Datenbank:

Backstock: (Menge der verfügbaren Artikel, z.B. Milch, angegeben als Zahl)
- Kuhmilch
- Hafermilch
- Kaffeebohnen
- Limonade
- Apfelschorle
- Wasser

Latte:
- Preis
- ID
- Bestelldatum

Americano:
- Preis
- ID
- Bestelldatum

Limonade:
- Preis
- ID
- Bestelldatum

Apfelschorle:
- Preis
- ID
- Bestelldatum

Zusätzlich zu den beschriebenen Funktionen möchte die Geschäftsführerin auch mit einem get-Befehl auf einen Blick erfahren können, wie viele Produkte sich derzeit in der Buchhandlung befinden (ohne das Café) und zusätzlich deren Gesamtwert.
