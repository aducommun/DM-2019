import csv

# display dictionary
def display_dict(dict):
    for k, v in dict.items():
        print(k, v)

# Get file path directory
def get_file_dir(region):
    dir = region[0] + '/' + region[1] + '/' + region[2] + '/' + region[3] + '/'
    return dir

# Get currency for given country
def get_currency(country):
    with open('codes-all.csv', encoding='UTF8') as f:
        csvreader = csv.reader(f,delimiter=',')
        split_country = country.upper().split(' ')
        code = ''
        found = False
        for row in csvreader:
            if found == True:
                break
            for sp in split_country:
                if sp in row[0]:
                    found = True
                    code = row[2]
                else:
                    found = False
                    code = ''
    return code

# Change date format from web scrapping
# "14 September, 2019" to "2019-09-14"
def format_date(date):
    d = date.split(' ')

    dd      = d[0]
    mm      = get_month(d[1].strip(','))
    yyyy    = d[2]

    return yyyy + '-' + mm + '-' + dd

# Get month dictionary
def get_month(month):
    months = {
        "January"   : "01",
        "February"  : "02",
        "March"     : "03",
        "April"     : "04",
        "May"       : "05",
        "June"      : "06",
        "July"      : "07",
        "August"    : "08",
        "September" : "09",
        "October"   : "10",
        "November"  : "11",
        "December"  : "12"
    }
    return months[month]

