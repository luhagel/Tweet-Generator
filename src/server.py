from flask import Flask
from modules import sentences
from modules import tokenization

app = Flask(__name__)

WORDS = tokenization.get_tokens_from_corpus('src/corpus.yml')

@app.route('/')
def random_sentence():

    return sentences.generate_sentence(WORDS, 10)

if __name__ == "__main__":
    app.run()
