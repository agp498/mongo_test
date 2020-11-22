#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from pprint import pprint
import matplotlib.pyplot as plt


def main():
    db, collection = server_connect('mongodb://localhost:27017/')
    """
    collection.drop()
    for x in range(1, 120000):
        point_ = make_point(x+20, x**3, x)
        # Insert business object directly into MongoDB via isnert_one
        result = collection.insert_one(point_)
        # Print to the console the ObjectID of the new document
        # print(f'Created {x} as {result.inserted_id}')
    # Tell us that you are done
    print('finished creating')
    # server_status(db)
    # print_docs(collection)
    """
    list_of_docs = list(collection.find().limit(150000))
    make_plot(list_of_docs)


def server_connect(server_address, db='test_db', col='stats_test'):
    client = MongoClient(server_address)
    db = client[db]
    collection = db[col]
    return db, collection


def server_status(db):
    # Issue the serverStatus command and print the results
    serverStatusResult = db.command("serverStatus")
    pprint(serverStatusResult)


def print_docs(collection):
    for user in collection.find():
        pprint(user)


def make_point(x, y, point_number):
    point_ = {
        'x': x,
        'y': y,
        'point_number': point_number
    }
    return point_


def make_plot(list_of_docs, fname='test.png'):
    xs = [doc['x'] for doc in list_of_docs]
    ys = [doc['y'] for doc in list_of_docs]
    fig, ax = plt.subplots()
    ax.plot(xs, ys)
    ax.set(xlabel='x', ylabel='y',
           title='y = f(x)')
    ax.grid()
    fig.savefig(fname)
    plt.show()


if __name__ == "__main__":
    main()
