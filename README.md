## Overview
This repository contains a python package to perform english to pig latin translations based on the [rules](#pig-latin-rules) below.

If you would like to check out a simple UI to run the code go here http://35.165.183.118:5000.  The install below will create an executable. Optionally, you can start the server locally.

## Installation
```
git clone https://github.com/steve-federowicz/piglatin.git
pip install ./piglatin
```
## Usage

### From command line
```
piglatin 'Hello, World!'
```

### Via python API
```
from piglatin import translator

translator.translate_phrase('Hello, World!')
```

Optionally, you can run the flask server via the following commands and then access the web UI locally at localhost:5000
```
export FLASK_APP=$(pwd)/piglatin/piglatin/server.py
flask run
```

## Pig Latin Rules

1. General rule: take the first letter of a word, move it to the end, and add "ay". Example: "hello" becomes "ellohay". 

2. A phrase with multiple words should translate each word: "hello world" becomes "ellohay orldway"

3. A word which begins with a vowel keeps its first letter, and just adds "way" to the end of the word: "eat apples" becomes "eatway applesway" 

4. A word which is capitalized should remain capitalized after translation: "Hello world" becomes "Ellohay orldway" 

5. A phrase with punctuation should maintain the position of the punctuation: "Hello, world!" becomes "Ellohay, orldway!" 

6. A word beginning with multiple consonants should move all of them together to the end: "drunk strangers" becomes "unkdray angersstray" 

7. The letters "qu" should stay together when moved to the end of a word: "quickly and quietly" becomes "icklyquay andway ietlyquay" 
