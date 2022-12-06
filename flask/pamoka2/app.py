from flask import Flask, render_template
from dictionary import data # importuojame duomenis

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', data=data)

if __name__ == "__main__":
    pub1 = Publisher("Baltos Lankos")
    pub2 = Publisher("Alma Littera")




    db.session.add_all([pub1, pub2])