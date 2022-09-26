from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first" href="/item7265346753/page_1">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li class="not-special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

# print(html.split("<body>")[-1].split("</body>")[0])

soup = BeautifulSoup(html, "html.parser")

# print(soup.body)

# print(type((soup.find("div"))))
# print(soup.find_all("div"))

el = soup.find_all(class_="special")
el2 = soup.find_all(attrs={"data-example": "yes"})
el3 = soup.select(("#first"))

el4 = soup.select(".special")
# for element in el4:
#     print(element.get_text())

el5 = soup.select(".special")
# for element in el5:
#     print(element.name)

# abu stringai, niekuo nesiskiria
# string1 = 'string'
# string2 = "string"


attribute = soup.select("div")[0]["href"]
# print(attribute)

attribute1 = soup.find("div")["id"]
# print(attribute1)


# paieska pagal atributo pavadinima
attribute2 = soup.select("[data-example]")
# print(attribute2)

# print(soup.div.contents)

li = soup.find("li")
# print(li.next_sibling.next_sibling)

# print(li.parent.parent)

# print(li.find_next_sibling(class_="not-special"))


li = soup.find("li")

res = li.find_parent().find_previous_sibling()["id"]
print(res)
