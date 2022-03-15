import studikasus2
import os
import pandas as pd

# data ={"Nama": ["Tito", "Ninis"], "Umur": [19, 19]}

db = studikasus2.studikasus2("localhost", "3306", "root", "")
df = db.import_csv("C:\\Users\\Acer\\PycharmProjects\\Exercise1\\addresses.csv")

print(db.create_db('studikasus'))
print(db.create_table('studikasus', 'test1table', df))
print(db.load_data('studikasus', 'test1table'))
print(db.import_csv("C:\\Users\\Acer\\PycharmProjects\\Exercise1\\addresses.csv"))
# print(help(studikasus2.studikasus2))