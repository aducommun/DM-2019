import getregions
import requests_cache
import csv
import download as dl
import transformregions as tr
import loadregions as lr
import tools as t

URL = "http://insideairbnb.com/get-the-data.html"

# CACHE
requests_cache.install_cache('web-reg-cache', backend='sqlite', expire_after=60)


# Download regions for France and Switzerland
regions = getregions.get_regions_sui_fra(URL)

for key in regions:
    region = regions[key]
    
    print('BEGIN DOWNLOAD')
    dl.download_region(region, False)
    print('END DOWNLOAD')

    print('BEGIN TRANSFORM')
    tr.transform_region(region)
    print('END TRANSFORM')

    print('BEGIN LOAD')
    lr.csv_to_sqlite(region)
    print('END LOAD')
    print(key + ' : success')

print('FINISH')
