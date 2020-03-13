import os
import glob
import pandas as pd
import csv
import sqlite3
from pandas import DataFrame

files = r'C:\Users\USER\Desktop\ex7\regions_listings\Bordeaux_listings_11_02_2019.csv'
df1 = pd.read_csv(files)
df1.insert(16, 'Region', 'Bordeaux')  # Adding new column region
df1.to_csv(files, index=False)
df1.insert(17, 'Currency', 'Euro')  # Adding new column Euro
df1.to_csv(files, index=False)


files = r'C:\Users\USER\Desktop\ex7\regions_listings\Lyon_listings_11_02_2019.csv'
df1 = pd.read_csv(files)
df1.insert(16, 'Region', 'Lyon')
df1.to_csv(files, index=False)
df1.insert(17, 'Currency', 'Euro')
df1.to_csv(files, index=False)


files = r'C:\Users\USER\Desktop\ex7\regions_listings\Paris_listings_11_02_2019.csv'
df1 = pd.read_csv(files)
df1.insert(16, 'Region', 'Paris')
df1.to_csv(files, index=False)
df1.insert(17, 'Currency', 'Euro')
df1.to_csv(files, index=False)

files = r'C:\Users\USER\Desktop\ex7\regions_listings\Geneva_listings_11_02_2019.csv'
df1 = pd.read_csv(files)
df1.insert(16, 'Region', 'Geneva')
df1.to_csv(files, index=False)
df1.insert(17, 'Currency', 'CHF')
df1.to_csv(files, index=False)

files = r'C:\Users\USER\Desktop\ex7\regions_listings\Vaud_listings_11_02_2019.csv'
df1 = pd.read_csv(files)
df1.insert(16, 'Region', 'Vaud')
df1.to_csv(files, index=False)
df1.insert(17, 'Currency', 'CHF')
df1.to_csv(files, index=False)

df2 = pd.DataFrame(
    columns=['File_name', 'Date_of_download', 'Region', 'Country', 'URL'])  # Creating a new csv file for metadata

df2['File_name'] = ['Bordeaux_listings_11_02_2019', 'Lyon_listings_11_02_2019',
                    'Paris_listings_11_02_2019', 'Geneva_listings_11_02_2019', 'Vaud_listings_11_02_2019']

df2['Date_of_download'] = ['11/02/2019', '11/02/2019',
                           '11/02/2019', '11/02/2019', '11/02/2019']

df2['Region'] = ['Bordeaux', 'Lyon', 'Paris', 'Geneva', 'Vaud']

df2['Country'] = ['France', 'France', 'France', 'Switzerland', 'Switzerland']

df2['URL'] = ['http://data.insideairbnb.com/france/nouvelle-aquitaine/bordeaux/2019-09-25/visualisations/listings.csv', 'http://data.insideairbnb.com/france/auvergne-rhone-alpes/lyon/2019-09-25/visualisations/listings.csv',
              'http://data.insideairbnb.com/france/ile-de-france/paris/2019-09-16/visualisations/listings.csv', 'http://data.insideairbnb.com/switzerland/geneva/geneva/2019-09-25/visualisations/listings.csv', 'http://data.insideairbnb.com/switzerland/vd/vaud/2018-11-26/visualisations/listings.csv']

df2.to_csv(r'C:\Users\USER\Desktop\ex7\metadata\metadata.csv',
           index=None, encoding='utf-8')  # metadata csv file created

# Folder contains the listings of all cities

os.chdir(r'C:\Users\USER\Desktop\ex7\regions_listings')

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
# export to csv
combined_csv.to_csv("combined.csv", index=False)

# Creating SQlite database for the following dataset
conn = sqlite3.connect('ex7.db')
c = conn.cursor()

# Create table - COMBINE

c.execute('''CREATE TABLE COMBINE
([id] INTEGER PRIMARY KEY,[name] text, [host_id] INTEGER, [host_name] TEXT, [neighbourhood_group] text, [neighbourhood] text, [latitude] float, 
[longitude] float, [room_type] TEXT, [price] INTEGER, [minimum_nights] INTEGER, [number_of_reviews] INTEGER, [last_review] DATE, 
[reviews_per_month] float, [calculated_host_listings_count] INTEGER, [availability_365] INTEGER, [Region] text, [Currency] text)''')

# Create table - METADATA

c.execute(
    ''' CREATE TABLE METADATA ([File_name] text Primary Key, [Date_of_download] date, [Region] text, [Country] text, [URL] text )''')

conn.commit()

read_combined = pd.read_csv(
    r'C:\Users\USER\Desktop\ex7\regions_listings\combined.csv', low_memory=False)
read_combined.to_sql('COMBINE', conn, if_exists='append',
                     index=False)  # Importing data to sqlite

read_metadata = pd.read_csv(
    r'C:\Users\USER\Desktop\ex7\metadata\metadata.csv', low_memory=False)
read_metadata.to_sql('METADATA', conn, if_exists='append', index=False)
