import pandas as pd
import getregions
import tools
import os


def transform_region(region):

    for date, link in region[3].items():
        dir = 'data/' + region[0] + '/' + region[1] + '/' + region[2] + '/' + date + '/'
        trname = dir + region[2] + ' ' + date + ' tr.csv'

        if not os.path.exists(trname):
            f = pd.read_csv(dir + 'listings.csv')

            # add "CITY"
            f.insert(16, 'city', region[2])
            f.to_csv(trname, index=False)

            # add "REGION"
            f.insert(17, 'region', region[1])
            f.to_csv(trname, index=False)

            # add "COUNTRY"
            f.insert(18, 'country', region[0])
            f.to_csv(trname, index=False)

            # add "CURRENCY"
            f.insert(19, 'Currency', tools.get_currency(region[0]))
            f.to_csv(trname, index=False)

            # add "CSV_FILE_PATH"
            f.insert(20, 'csv_file_path', trname)
            f.to_csv(trname, index=False)

            # add "DOWNLOAD_DATE"
            f.insert(21, 'download_date', date)
            f.to_csv(trname, index=False)
            
            # add "LINK"
            f.insert(22, 'link', link)
            f.to_csv(trname, index=False)

    return trname
