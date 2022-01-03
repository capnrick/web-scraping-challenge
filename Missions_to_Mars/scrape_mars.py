#scrape_mars

from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)        

def scrape():

    #scraping the news title from mission_to_mars.py
    browser=init_browser()
    url= 'https://redplanetscience.com/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    #grab main headline from URL
    headlines = soup.find('div', class_="list_text")
    news_title=headlines.find('div', class_='content_title').text
    

    #scraping the text related to the article title summary and saving to variable
    news_p=headlines.find('div', class_="article_teaser_body").text
    news_p
    browser.quit()


    #scraping the images 
    browser=init_browser()
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    browser.links.find_by_partial_text('FULL IMAGE').click()
    
    html = browser.html
    soup = bs(html, 'html.parser')
    partial_image_path= soup.find('img', class_='fancybox-image')['src']
    featured_image_url=url+partial_image_path
    browser.quit()



    #scraping mars/earth table data
    browser=init_browser()
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    table_data= pd.read_html(url)
    new_df=table_data[0]
    new_df = new_df.iloc[1: , :]
    new_df.columns= ["", "Mars", "Earth"]
    html_table = new_df.to_html(index=False)
    new_html_table=html_table.replace('"', "")
    browser.quit()

   
   
    #scraping mars hemisphere images and names
    
    browser=init_browser()
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    
    #scraping hemisphere names and storing in list 'hemisphere_names
    hemisphere_names=[]

    results= soup.find_all('div', class_="collapsible results")
    hemisphere_list=results[0].find_all('h3')

    for hemisphere in hemisphere_list:
        hemisphere_names.append(hemisphere.text)



    #scraping thumbnail url and storing in list,'thumbnail_url_list'
    thumbnail_results = results[0].find_all('a')

    thumbnail_url_list = []
    for thumbnail in thumbnail_results:
    
        if (thumbnail.img):
            thumbnail_url = 'https://marshemispheres.com/' + thumbnail['href']
            thumbnail_url_list.append(thumbnail_url)   


    browser.quit()
    
    ##scraping full image URL and sorting into list 'full images
    full_images = []     
    
    for url in thumbnail_url_list:
        
        browser=init_browser()
        browser.visit(url)
        html =browser.html
        soup =bs(html, 'html.parser')
        results= soup.find_all('img', class_='wide-image')
        
        partial_image_path = results[0]['src']
        full_image_link = 'https://marshemispheres.com/' + partial_image_path
    
        # Add full image links to a list
        full_images.append(full_image_link)
    
    browser.quit()


    #storing titles and full url into list 
    combined_list = zip(hemisphere_names, full_images)
    combined_list = zip(hemisphere_names, full_images)
    list_dictionaries = []

    for name,image in combined_list:
    
       
        combined_dict = {}
    
        # Add hemisphere title to dictionary
        combined_dict['title'] = name
        combined_dict['img_url']= image
   
        #list dictionaries has title and full image url scraped data
        list_dictionaries.append(combined_dict)

    #saving scraped data stored into variables into dictionary
    mars_info = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": featured_image_url,
        "table": new_html_table,
        "hemisphere_thumbnail": thumbnail_url_list,
        "hemisphere_combined_dict":list_dictionaries
    }

    #returning dictionary of scraped data
    print(mars_info)
    return mars_info

