from flask import Flask, url_for, render_template
from jinja2 import Markup

app = Flask(__name__)   # __name__ je proměnná nastavená pythonem na jméno aktuálního modulu

@app.route('/')
def hello():
    return url_for('hello_english',
            username='Jana',
            count=3)

@app.route('/hello')
@app.route('/hello/<username>/')    # dává se nakonec lomítko, je to konvence (když tam nebude, nic se nestane)
@app.route('/hello/<username>/<int:count>/')
def hello_english(username=None, count=1):
    return render_template('hello.html',
                            name=username)


# MŮŽU SI NAPSAT VLASTNÍ FILTR, pak to dám v hello. thml za capitalize s tou rovnou čárou
#@app.template_filter
#def reverse(text):
#    return reversed(text)

@app.template_filter('em')
def em(text):
    return Markup('<em>{}</em>').format(text)
#pomocí markup označuji, že je to html a je to v pořádku
