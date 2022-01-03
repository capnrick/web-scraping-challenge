#mission to mars
from flask import Flask, render_template, redirect
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo
import scrape_mars



 
# create instance of Flask app
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection, name of database is mars_db
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# create route that renders index.html template
@app.route("/")
def index():
    listings = mongo.db.listings.find_one()
    return render_template("index.html", listings=listings)


#using scrape route to call scrape function
@app.route("/scrape")
def scraper():
    listings = mongo.db.listings

    #runs function in scrape_mars.py
    listings_data = scrape_mars.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)
 

#this allows us to launch our app from the command line
if __name__ == "__main__":
    app.run(debug=True)
