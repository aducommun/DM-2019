import requests
from bs4 import BeautifulSoup
import tools

URL = "http://insideairbnb.com/get-the-data.html"


""" ------------------------------------------------------------------------
    return all the regions with their metadata in a dictionary in which the
    city is the key and the value is a list of metadata.

    regions[city] : [country, region, city, date, link]
    ------------------------------------------------------------------------
"""
def get_all_regions(URL):

    # Create the parse tree
    soup = BeautifulSoup(requests.get(URL).content, 'html5lib')
    table = soup.find('div', attrs = {'class':'contentContainer'})
    regions = {}

    # Put all the regions in the dictionary with the city as key
    for row in table.findAll('h2'):
        area = row.text.rsplit(',', 2)
        city = area[0]
        region = area[1]
        country = area[2]

        regions[city] = [country[1:], region[1:], city]

    # Add metadata for each region of the dictionary
    for t in table.findAll('table'):
        date = t.findAll('tr')[4].findAll('td')[0].text
        date = tools.format_date(date)
        city = t.findAll('tr')[4].findAll('td')[1].text
        link = t.findAll('tr')[4].findAll('td')[2].find('a').get('href')
        metadata = [date, link]

        if city in regions:
            regions[city].extend(metadata)

    return regions

