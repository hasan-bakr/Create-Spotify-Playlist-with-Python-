import requests
from bs4 import BeautifulSoup

date = input("Give me a date for best of 100 hit songs:")
response = requests.get(url='https://www.billboard.com/charts/hot-100/' + date)
soup = BeautifulSoup(response.text, 'html.parser')
mySongNames = soup.find_all(name="h3", class_='u-line-height-125')
myTitles = []
for _ in mySongNames:
    myTitles.append(_.text.strip())

