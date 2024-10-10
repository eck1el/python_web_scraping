import bs4
import requests
from lxml import html

def webscraping_test():
    result = requests.get('http://books.toscrape.com/')
    #soup = bs4.BeautifulSoup(result.text, 'lxml')

    tree = html.fromstring(result.content)

    #Use Xpth to find thw tag <a> tag inside <h3> and extract the title attribute
    title = tree.xpath('//h3/a/@title')

    #Verify if the title has been found and display it
    if title:
        for t in title:
            print(f"The title is:{t}")
    else:
        print("the title has not been found")

if __name__ == '__main__':
    webscraping_test()
