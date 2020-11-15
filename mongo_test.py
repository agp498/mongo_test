#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from pprint import pprint


def main():
    db, collection = server_connect('mongodb://localhost:27017/')
    server_status(db)
    print()
    print_doc(collection)

def server_connect(server_address):
    client = MongoClient(server_address)
    db=client.test_db
    collection = db.test_collection
    return db, collection

def server_status(db):
    # Issue the serverStatus command and print the results
    serverStatusResult=db.command("serverStatus")
    pprint(serverStatusResult)

def print_doc(collection):
    for user in collection.find():
        pprint(user)

if __name__ == "__main__":
    main()
