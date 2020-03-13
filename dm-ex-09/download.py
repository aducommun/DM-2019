import getregions
import tools
import os
import wget

#   Download the listings.csv for the given region
def download_region(region, force):
    links = region[3]
    for date, link in links.items():
        dir = 'data/' + region[0] + '/' + region[1] + '/' + region[2] + '/' + date + '/'
        filename = 'listings.csv'
        file_path = dir + filename

        if not os.path.exists(file_path):
            os.makedirs(dir)
            wget.download(link, file_path)
            tools.save_download(region[2], region[1], region[0], file_path, date, link)
            print(file_path + ' downloaded')
        elif os.path.exists(dir):
            if force == True:
                wget.download(link, file_path)
                tools.save_download(region[2], region[1], region[0], file_path, date, link)
                print('File overrided')
            else:
                print(file_path + ' already exist')
                tools.save_download(region[2], region[1], region[0], file_path, date, link)
