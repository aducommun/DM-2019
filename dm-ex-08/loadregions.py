import sqlite3
import pandas as pd

# CREATE or REPLACE table LISTINGS to store data from csv files
def csv_to_sqlite(csv_file_path):
    try:
        conn = sqlite3.connect('PROJECT-DM-G11.db')
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
        reader = pd.read_csv(csv_file_path)
        reader.to_sql('LISTINGS', conn, if_exists='append', index=False)

        conn.commit()
        conn.close()
    except:
        conn.close()
        pass
