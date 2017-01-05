""" Simple Flask server for piglatin translator web UI """
import logging
from piglatin import translator

from flask import Flask, request, render_template

app = Flask(__name__)

logging.basicConfig(filename='server.log', filemode='w', level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/translate', methods=['POST'])
def translate_phrase():
    """
    Receive user input from web form and translate to piglatin.
    """
    user_input = request.form['text']

    logger.info("User input: %s", user_input)

    translated_input = translator.translate_phrase(user_input)

    logger.info("Translated input: %s", translated_input)

    return render_template('translate_form.html', translation=translated_input, user_input=user_input)


@app.route("/")
def layout():
    """
    Layout HTML for main page.
    """
    return render_template('translate_form.html', translation='')



if __name__ == "__main__":
    app.run()
