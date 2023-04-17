from pydantic import BaseModel
from enum import Enum
from datetime import date
from datetime import datetime

class Kategorie(str, Enum):
    Latte = "Latte"
    Americano = "Americano"
    Limonade = "Limonade"
    Apfelschorle = "Apfelschorle"

class Pro_kategorie(str, Enum):
    Kuhmilh = "Kuhmilh"
    Hafermilch = "Hafermilch"
    Kaffenbohnen = "Kaffenbohnen"
    Limonade = "Limonade"
    Apfelschorle ="Apfelschorle"
    Wasser = "Wasser"

class Buecher(BaseModel):
    Titel : str
    Autor : str
    Erscheinungsjahr : int
    Herausgeber : str
    Seitenanzahl : int
    Preis : float
    AufLager : int

class E_Buecher(BaseModel):
    Titel : str
    Autor : str
    Erscheinungsjahr : int
    Herausgeber : str
    Seitenanzahl : int
    Preis : float

class Filme(BaseModel):
    Titel : str
    Produzent : str
    Erscheinungsjahr : int
    Preis : float
    AufLager : int

class Backstocks(BaseModel):
    Produkt : Pro_kategorie
    Bestand : int
    

class Drink(BaseModel):
    bestellung_id : int
    kategorie : Kategorie
    Preis : int
    Anzahl : int
    Besteldatum : datetime
