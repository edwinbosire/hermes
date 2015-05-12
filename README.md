Hermes
======
Hermes is the messenger of the gods


This is a news scrapper, I will be writting a follow-up blog here http://edwinbosire.github.io/

####Introduction

Sometimes you want to build an app but you do not have an API to siphon data from, fret not brethrens, the solution is as old as the web itself -web scraping is here to save you.

Hermes is a scraper for [Nation Media](http://www.nation.co.ke), one of Kenya's top news sites. They provide a feed for the news but its usually a few hours old and frankly, quite unreliable, my solution is to get the news directly from the source.

####Requirements
- python 2.7
- MongoDB
- [Scrapy](http://scrapy.org/)
- Scrapyd ***for deployment***
- Understanding of python
- Programming knowledge, duh!


#### Running the scraper.

Before you run the scrapper, you will need to modify a few settings. At the moment, the app is saving the scraped data to a MongoDB instance. You will need to provide connection details. These three variables can be initialised in the 'settings.py' file. 

- **MONGODB_SERVER**   address to your mongoDB instance
- **MONGODB_PORT**  port for the server
- **MONGODB_DB**   the database to use
- **MONGODB_COLLECTION**  the collection to use, a new one will be created if it does not exist.


***I'll complete this document when i get time***

****1 year later, I guess I never got any time****
