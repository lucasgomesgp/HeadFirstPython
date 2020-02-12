from flask import Flask
from vsearch import search4vowels

app = Flask(__name__)
@app.route("/")
def hello() -> str:
    return "Hello world from Flask!"

@app.route("/search4")
def do_search() -> str:
    return str(search4vowels("life, the universe, and everything, 'eiru!'"))
app.run()
