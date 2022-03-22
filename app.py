import random
from secrets import choice
from flask import Flask, render_template

app=Flask(__name__)

from moje_programy.character_wiki import character
from moje_programy.open_poem import open_poem

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/zajecia-programowania')
def zajecia():
    return render_template('zajecia-programowania.html')

@app.route('/siema-lukas')
def siema_lukas():
    return render_template("siema-lukas.html")

@app.route('/flaga-dla-ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga-dla-ukrainy.html")

@app.route('/ciekawe-postacie')
def ciekawe_postacie():
    interesting_character_list = [
        'Szewczenko Tanja',
        'Nadija Sawczenko',
        'Witalij Kłyczko',
        'Jurij Bojko',
        'Stepan Bandera',
        'Walery Łobanowski',
        'Wasyl Tacij',
        'Eduard Wahorowski'
    ]
    randomizer_character_list = []

    for i in range(3):
        
        character_name = random.choice(interesting_character_list)
        index = interesting_character_list.index(character_name)
       
        interesting_character_list.pop(index)

        chosen_character_description = character(character_name)
        word_counter = len(chosen_character_description.split())
        info = [character_name, chosen_character_description, word_counter]
        randomizer_character_list.append(info)
        randomizer_character_list.sort(key = lambda x: x[2], reverse = True)
        

    return render_template("ciekawe-postacie.html", randomizer_character_list=randomizer_character_list)


@app.route('/btc')
def btc():
    return render_template("btc.html")

if __name__=="__main__":
    app.run()
