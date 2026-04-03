from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']  # Replace with your database name

if __name__ == '__main__':
    app.run(debug=True)