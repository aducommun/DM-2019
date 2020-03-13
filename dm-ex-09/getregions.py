import requests
from bs4 import BeautifulSoup
import tools
from selenium.webdriver import Chrome


URL = "http://insideairbnb.com/get-the-data.html"


""" ------------------------------------------------------------------------
    return all the regions with their metadata in a dictionary in which the
    city is the key and the value is a list of metadata.

    regions[city] : [country, region, city, [date, link]]
    ------------------------------------------------------------------------
"""
def get_regions(URL):

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
    for table in table.findAll('tbody'):
        city = table.findAll('tr')[4].findAll('td')[1].text
        files = {}

        for tr in table.findAll('tr'):
            if tr.findAll('td')[2].find('a').text == 'listings.csv':
                date = tools.format_date(tr.findAll('td')[0].text)
                link = tr.findAll('td')[2].find('a').get('href')

                files[date] = link

        if city in regions:
            regions[city].append(files)

    return regions


""" ------------------------------------------------------------------------
    return region of Switzerland and France with all historical data
    regions[city] : [ country, region, city, [date]=link ]
    ------------------------------------------------------------------------
""" 
def get_regions_sui_fra(URL):
    regions = get_regions(URL)
    regions_sui_fra = {}

    for region in regions:
        if regions[region][0] == "France" or regions[region][0] == "Switzerland":
            regions_sui_fra[region] = regions[region]
    
    return regions_sui_fra