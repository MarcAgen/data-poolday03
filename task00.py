##
## EPITECH PROJECT, 2026
## day03
## File description:
## task00
##
import pymongo as mongo

def get_db(host:str, port:int, db_name:str):

    client = mongo.MongoClient(host + ":" + port)
    return client[db_name]

