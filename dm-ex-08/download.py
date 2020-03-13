import getregions
import tools
import os
import wget


#   Download the latest version of listings.csv for the given region
def download_region(city, force):    
    regions = getregions.get_all_regions("http://insideairbnb.com/get-the-data.html")
    region  = regions[city]
    link    = region[4]
    dir     = tools.get_file_dir(region)
    filename = 'listings.csv'
    file_path = dir + filename

    if not os.path.exists(file_path):
        os.makedirs(dir)
        wget.download(link, file_path)
        print('file downloaded')
    elif os.path.exists(dir):
        if force == True:
            wget.download(link, file_path)
            print('File overrided')
        else:
            print('file already exist')

            