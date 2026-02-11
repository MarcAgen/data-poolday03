##
## EPITECH PROJECT, 2026
## day03
## File description:
## task02
##
from mongoengine import *

class Laureate(Document):
    id:str
    firstname:str
    surname:str
    born:str
    died:str

    bornCountry:str
    bornCountryCode:str

    bornCity:str

    diedCountry:str
    diedCountryCode:str

    diedCity:str

    gender:str

    prizes:list[Prize]

class Country(Document):
    name:str
    code:str

class Prize(Document):
    year:str
    category:str
    laureates:list[Laureate] = []
