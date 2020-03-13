import getregions
import requests_cache
import csv
import download as dl
import transformregions as tr
import loadregions as lr
import tools as t

# CACHE
requests_cache.install_cache('web-reg-cache', backend='sqlite', expire_after=60)


# TESTING : Download 
given_region = 'Barcelona'

dl.download_region(given_region, False)
filepath_output = tr.transform_region(given_region)
lr.csv_to_sqlite(filepath_output)
print('FINISHED')
