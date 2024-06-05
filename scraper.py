import requests
from bs4 import BeautifulSoup

url = "https://sebyb87.github.io/Portfolio/HangmanList.html"

def get_words_from_web():
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')

    ol =soup.find('ol')
    words = ol.find_all('li')
    wordList = []

    for tag in words:
        word = tag.text
        wordList.append(word)

    return wordList

