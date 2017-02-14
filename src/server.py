from flask import Flask
import sentences
app = Flask(__name__)

WORDS = sentences.get_words()

@app.route('/')
def random_sentecne():

    return sentences.generate_sentence(WORDS, 10)
