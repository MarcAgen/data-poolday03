##
## EPITECH PROJECT, 2026
## day03
## File description:
## task02
##
import pymongo
import json
from glob import glob
from task00 import get_db

def import_data(db, data_path:str):
    for i in glob("*.json"):
        with open(i, 'r') as file:
            filedata = json.load(file)
        db[i[0:-5]].insert_one(filedata)

db = get_db ( "localhost" , 27017 , "nobel_database" )
import_data ( db , "./ data" )
print ( db . list_collection_names () )
