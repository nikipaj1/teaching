## 1 užduotis:

**main.py** failas:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
```


**templates/home.html** failas:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Labas</title>
</head>
<body>
    <h1>Norimas tekstas</h1>
</body>
</html>
```

## 2 užduotis:

**main.py** failas:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<word>")
def word(word):
    return render_template("word.html", word = word)

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/word.html** failas:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Žodžiai</title>
</head>
<body>
    {% for x in range(5) %}
        {{word}}
    {% endfor %}
</body>
</html>
```

## 3 užduotis:

**main.py** failas:

```python
from flask import Flask, render_template
import calendar

app = Flask(__name__)

@app.route("/keliamieji")
def leap():
    return render_template("leap.html", calendar = calendar)

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/leap.html** failas:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Leap</title>
</head>
<body>
    {% for year in range(1900, 2100) %}
    {% if calendar.isleap(year) %}
    {{year}}
    {% endif %}
    {% endfor %}
</body>
</html>
```

## 4 užduotis:

**main.py** failas:

```python
from flask import Flask, render_template, request
import calendar

app = Flask(__name__)

@app.route("/arkeliamieji", methods=["GET", "POST"])
def isleap():
    if request.method == "GET":
        return render_template("getyear.html")
    elif request.method == "POST":
        year = request.form["year"]
        return render_template("isleap.html", year=int(year), calendar=calendar)

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/getyear.html** failas:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Get Year</title>
</head>
<body>
<form action="#" method="post">
    <p>Metai:</p>
    <p><input type="text" name="year"/></p>
    <p><input type="submit" value="Patikrinti"/></p>
</form>
</body>
</html>
```

**templates/isleap.html** failas:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Is Leap</title>
</head>
<body>
    {% if calendar.isleap(year) %}
    <p>Keliamieji</p>
    {% else %}
    <p>Nekeliamieji</p>
    {% endif %}
</body>
</html>
```