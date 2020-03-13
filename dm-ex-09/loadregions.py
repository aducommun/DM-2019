import sqlite3
import pandas as pd

# CREATE or REPLACE table LISTINGS to store data from csv files
def csv_to_sqlite(region):

    for date, link in region[3].items():
        dir = 'data/' + region[0] + '/' + region[1] + '/' + region[2] + '/' + date + '/'
        file = region[2] + ' ' + date + ' tr.csv'
        filepath = dir + file    
        try:
            conn = sqlite3.connect('db/PROJECT-DM-G11.db')
            c = conn.cursor()

            # Create table LISTINGS if not exists
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS LISTINGS (
                    [id] INTEGER PRIMARY KEY,
                    [country] TEXT,
                    [region] TEXT,
                    [city] TEXT,
                    [name] TEXT,
                    [host_id] INTEGER,
                    [host_name] TEXT,
                    [neighbourhood_group] TEXT,
                    [neighbourhood] TEXT,
                    [latitude] TEXT,
                    [longitude] TEXT,
                    [room_type] TEXT,
                    [price] INTEGER,
                    [currency] TEXT,
                    [minimum_nights] INTEGER,
                    [number_of_reviews] INTEGER,
                    [last_review] DATE,
                    [reviews_per_month] FLOAT,
                    [calculated_host_listings_count] INTEGER,
                    [availability_365] INTEGER,
                    [csv_file_path] TEXT,
                    [download_date] TEXT,
                    [link] TEXT
                )
                """
            )
            # Insert data from csv to sqlite
            reader = pd.read_csv(filepath)
            reader.to_sql('LISTINGS', conn, if_exists='append', index=False)
            conn.commit()
        except Exception as err:
            print("-------------------------------------------- /!\ " + str(err))
        finally:
            conn.close()
