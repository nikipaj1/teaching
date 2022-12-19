from flask import Flask, request, render_template
from dictionary import data # importuojame duomenis
from forms import ContactForm

import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        date = request.form['date']
        autorius = request.form['autorius']
        tekstas = request.form['tekstas']
        pavadinimas = request.form['pavadinimas']
        data.append({
            'data': date,
            'autorius': autorius,
            'pavadinimas': pavadinimas,
            'tekstas': tekstas,
            'status': 'published'
        })

    return render_template('index.html', data=data)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/<string:title>')
def article(title):
    return render_template('article.html', title=title, data=data)

@app.route("/add_article")
def add_article():
    return render_template('add_article.html')

@app.route("/contact_us", methods=['GET', 'POST'])
def contact_us():
    form = ContactForm() # musu sukurta formos klase
    if form.validate_on_submit():
        return render_template('contact_success.html', form=form)
    return render_template('contact_us.html', form=form)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)