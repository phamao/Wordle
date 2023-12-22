import requests
import re
from bs4 import BeautifulSoup

# Returns a list of 5 letter words
def get_words():

    # Collection of 5 letter words
    URL = 'https://byjus.com/english/5-letter-words/'
    page = requests.get(URL)

    # Parses the HTML
    soup = BeautifulSoup(page.content, 'lxml')

    # Puts all <tr> tagged values into a list
    tr_list = soup.find_all('tr')

    # Stores 5 letter words
    word_list = []

    # Loops through the tr_list for <td> tags
    for tr in tr_list:

        # Creates a list of the <td> tags in the current <tr> tag
        td_list = tr.find_all('td')
        
        # Loops through td_list and puts the text inside into a separate list
        for td in td_list:
            word_list.append(td.text)

    # Purges any non-5 letter words that were also tagged from the word list
        for word in word_list:
            if len(word) != 5:
                word_list.remove(word)

    # Removes '\nHow Many Types of Noun\n' since it wasn't purged for some reason
    del word_list[-1]

    return word_list

# print(get_words())