# Create flask app
# Using Flask and Mongo to create Mars Web App

from flask import Flask, render_template # Use render_template
from flask_pymongo import PyMongo # Use pymongo to interact with mongo
import scraping # to use the scraping code, we will convert from Jupyter notebook to Python.

app = Flask(__name__) # Set up flask

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
 