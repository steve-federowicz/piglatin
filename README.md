## Overview
This repository contains a python package to perform english to pig latin translations based on the [rules](#pig-latin-rules) below.

If you would like to check out a simple UI to run the code go here.  The install below will also spawn a local server available at localhost:5000.

## Installation and usage
```
git clone 
pip install ./piglatin
piglatin "Hello, World!"


```

## Pig Latin Rules

1. General rule: take the first letter of a word, move it to the end, and add "ay". Example: "hello" becomes "ellohay". 

2. A phrase with multiple words should translate each word: "hello world" becomes "ellohay orldway"

3. A word which begins with a vowel keeps its first letter, and just adds "way" to the end of the word: "eat apples" becomes "eatway applesway" 

4. A word which is capitalized should remain capitalized after translation: "Hello world" becomes "Ellohay orldway" 

5. A phrase with punctuation should maintain the position of the punctuation: "Hello, world!" becomes "Ellohay, orldway!" 

6. A word beginning with multiple consonants should move all of them together to the end: "drunk strangers" becomes "unkdray angersstray" 

7. The letters "qu" should stay together when moved to the end of a word: "quickly and quietly" becomes "icklyquay andway ietlyquay" 
