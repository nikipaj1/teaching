from random import randint
from re import L
from urllib import request
import requests
from bs4 import BeautifulSoup

"""
# requests -> GET -> html
# html -> soup
# --------> tags

html = request.get("www.delfi.lt").text
soup = BeautifulSoup("www.delfi.lt", "html.parser")
"""


"""
                        2 UZDUOTIS
"""

url = "https://quotes.toscrape.com"
res = requests.get(url)
# print(res.text)

soup = BeautifulSoup(res.text, "html.parser")

# gauti citatas
quotes_spans = soup.select(".text")  # CSS selectors
quotes_list = [quote.get_text() for quote in quotes_spans]

# gauti nuorodas
a_blocks = soup.find_all("a", attrs={"class": None})
hrefs = [tag["href"] for tag in a_blocks if tag.get_text() == "(about)"]

# atsakymai
authors_blocks = soup.find_all("small", class_="author")
answers = [i.get_text() for i in authors_blocks]

# uzuominos #1
hints_1 = []
for answer in answers:
    splitted_name = answer.split()
    hint = ""
    for word in splitted_name:
        if "." not in word:
            hint += word[0] + "."
        else:
            hint += word
    hints_1.append(hint)

hints_2 = []


def get_second_hint(i):
    res = requests.get(url + hrefs[i])
    soup = BeautifulSoup(res.text, "html.parsers")
    text = soup.select("p")[1].get_text()
    return text


# LET THE GAME BEGIN
while 1:
    i = randint(1, 10)
    print("\n", quotes_list[i])
    answer1 = input("Your Answer: ")
    if answer1 != answers[i]:
        print(hints_1[i])
        answer2 = input("Your answer: ")
        if answer2 != answers[i]:
            print(get_second_hint(i))
            answer3 = input("Your answer")
            if answer3 != answers[i]:
                if_continue = input(f"Correct answerr is {answers[i]} Continue? y/n: ")
                if if_continue == "y":
                    continue
                else:
                    break
