import requests
import json
from bs4 import BeautifulSoup

filename = 'thesample.html'
with open (filename, 'r' ) as file:
    content = file.read()
    #print(content)

    soup = BeautifulSoup(content,'lxml')
    #print(soup)

    article_tags = soup.find_all('h3')
    #print(article_tags)

    article_divs = soup.find_all('div', class_= 'article')
    for article in article_divs:
        article_actual = article.find('p', class_='content')
        article_author = article.find('p', class_='author')
        print(article_author.text,article_actual.text)





url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'lxml') # beautiful soup will give a chance to parse
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
#print(soup.body) # gives the whole page on the website
print(response.status_code)
boston_data_list = soup.find('ul', class_='custom-stat-list')
labels_boston_data_list = soup.find_all('span', class_='stat-label')
figures_boston_data_list = soup.find_all('span', class_='stat-figure')

try:
    boston_dict = {}
    for x in range (len(labels_boston_data_list)):
        boston_dict[labels_boston_data_list[x].text] = figures_boston_data_list[x].text
except:
    print("Indexing error, not enough figures or labels")

boston_json = json.dumps(boston_dict, indent=2) # indent could be 2, 4, 8. It beautifies the json

with open('boston__uni_stats.json', 'w', encoding='utf-8') as f:
    json.dump(boston_dict, f, ensure_ascii=False, indent=2)