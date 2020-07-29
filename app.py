# Create flask app
# Using Flask and Mongo to create Mars Web App

from flask import Flask, render_template # Use render_template
from flask_pymongo import PyMongo # Use pymongo to interact with mongo
import scraping # to use the scraping code, we will convert from Jupyter notebook to Python.

app = Flask(__name__) # Set up flask

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app" # tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL
mongo = PyMongo(app) # is the URI we’ll be using to connect our app to Mongo. This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a database named ”mars_app”.

# set up 2 Flask routes: 
# one for the main HTML page everyone will view when visiting the web app, 
# and one to actually scrape new data using the code we’ve written.
 
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"  


if __name__ == "__main__":
   app.run()  