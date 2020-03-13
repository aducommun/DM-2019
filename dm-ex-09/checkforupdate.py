from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getregions
import csv

def verify():
    regions = getregions.get_regions('http://insideairbnb.com/get-the-data.html')
    new = False
    regions_news = []
    with open('data/regions-metadata.csv', 'r', encoding='UTF8', newline='') as f:
        csvreader = csv.reader(f, delimiter=',')
        for row in csvreader:
           for r in regions:
            region = regions[r]
            for date, link in region[3].items():
                filepath = 'data/' + region[0] + '/' + region[1] + '/' + region[2] + '/' + date + '/listings.csv'
                if not filepath == row[3]:
                        new = True
                        regions_news.append(region[2])
    if new:
        send_email(regions_news)

def send_email(regions):
    message = MIMEMultipart()
    message["from"] = "Data Management System - Exercise 9"
    message["to"] = "alexandre.ducommun@bluewin.ch"
    message["subject"] = "New data available"

    body = "new data available for :\n"
    for region in set(regions):
        r = "\n " + region
        body += r

    message.attach(MIMEText(body))

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("system.testdm@gmail.com", "UNINE12345678")
        smtp.send_message(message)
        print("Sent...")

verify()
