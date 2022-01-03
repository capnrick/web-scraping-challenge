# web-scraping-challenge
My solution for HW 12 -Web Scraping with Mongo DB for Northwestern University Data Science and Visualization Bootcamp

In this exercise, data scraped from various websites are stored and then retreived from a Mongo Database and displayed in an HTML page using a Flask App. This is done with the help of PyMongo, BeautifulSoup, JupyterNotebook, and Bootstrap elements. 


## Step 1- Scraping
 
 1. The first step in this scraping assignment is create a jupyter notebook and title it `mission_to_mars`. This contains all the code to scrape various websites containing text, tables and images to be saved into variables for later retrieval.
 2. First scrap [Mars News Site](https://redplanetscience.com/). Use Beautiful Soup and Splinter as well as ChromeDriver Manager to create objects that whose HTML code can be parsed and relevant information stored into variables, in this case the title.
 3. Scrape [Featured Space Image site ](https://spaceimages-mars.com/).Do this using the previous tasks except with the added challenge of saving the URL to the image and then stored again in a variable. Added note here is to remember to quit the browser after each scrape. 
 4. Scrape the [Mars Facts](https://galaxyfacts-mars.com/) site using a pandas function `pd.read.html(url)`. This saved the table data into manageable dataframe that is then altered to obtain just a single table. The dataframe is then converted to html code using the useful `df.to_html' function.
 5. Visit the [Astrogeology site](https://marshemispheres.com/) to obtain images of each of the 4 hemispheres into a Python dictionary using `image_url` and `title` as keys. The challenge here ist to use the `.click` function allowing the browser to actually click on the larger resolution image button to obtain the next html page,then save and parse to obtain the full resolution URL.
 
 ## Step 2- MongoDB and Flask Application
 
 1. In this step, create a Flask app within `app.py` to connect to a **Mongo Database**. This is done with help of `PyMongo` which is imported. 
2. Create a routing table for the various routes that will be accessed on the index.html page. The first route being the `index.html` homepage that displays the clickable **button** that will intiate the scraping of the previously mentioned websites, as well as the route that will access the scrape functions written in the `scrape_mars.py` file.The `scrape_mars.py` file contains simply python code taken from the jupyter notebook `mission_to_mars` and modified to return a list dictionary values containing all the saved variables.  
 3. Create an 'index.html' file that contains the layout of the scraped data including news, mars facts table and images using bootstrap to strucure the HTML template.
 4. Screenshot the resulting page created. 
