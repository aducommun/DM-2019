import pandas as pd
import getregions
import tools



def transform_region(city_key):
    regions = getregions.get_all_regions("http://insideairbnb.com/get-the-data.html")
    region = regions[city_key]
    file = tools.get_file_dir(region)
    trname = file + city_key + ' ' + region[3] + ' TR.csv'

    f = pd.read_csv(file + 'listings.csv')

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
    f.insert(21, 'download_date', region[3])
    f.to_csv(trname, index=False)
    
    # add "LINK"
    f.insert(22, 'link', region[4])
    f.to_csv(trname, index=False)

    return trname
