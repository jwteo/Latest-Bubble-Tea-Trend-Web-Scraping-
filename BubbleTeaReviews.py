from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://eatbook.sg/category/class/bubble-tea/').text
soup = BeautifulSoup(source, 'lxml')

# writing into csv file
csv_file = open('BubbleTeaReviews.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['HEADLINE', 'SUMMARY', 'DATE POSTED'])

# Scraping the website
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='post-entry').p.text
    print(summary)

    date = article.find('div', class_='list-meta').span.text
    print(date)

    print()

    csv_writer.writerow([headline, summary, date])
csv_file.close()
