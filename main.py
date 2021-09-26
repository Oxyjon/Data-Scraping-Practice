import requests
from bs4 import BeautifulSoup
import csv
#get url
response = requests.get('https://www.allrecipes.com/')
#convert to text
recipe_site = response.text
#init Beautiful soup
soup = BeautifulSoup(recipe_site, 'html.parser')
#find all titles
titles = [title.text for title in soup.find_all('h3', class_='card__title')]
#Find all links
links = [a['href'] for a in soup.find_all('a', href=True, class_='card__titleLink')]
#remove duplicates from the links list
links = list(dict.fromkeys(links))
#open CSV
with open('recipe.csv', 'w') as file:
    #setup csv writer
    recipe_writer = csv.writer(file)
    #for loop to loop through all the items in the list
    for recipe in range(len(titles)):
        #write rows of recipe names and links
        recipe_writer.writerow([titles[recipe]] + [links[recipe]])
