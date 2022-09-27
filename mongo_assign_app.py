from flask import Flask
from flask_pymongo import PyMongo, ObjectId
import json

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/Employees"
app.config['SECRET_KEY'] = "@123@ssIgnMent$%^"

mongo = PyMongo(app)

db = mongo.db.details

with open ('data.json') as file:
    file_data = json.load(file)

if isinstance(file_data,list):
    db.insert_many(file_data)
else:
    print("====================")
    print("error loading file")
    print("====================")

