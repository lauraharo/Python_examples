#Simple dictionary program which saves the dictionary into file: jsondata.json.
import pickle
import os.path
import json

if os.path.exists("./jsondata.json"):
    with open("jsondata.json", "r") as f:
        obj = json.load(f)
        print(obj)

words = {}
while True:
    word = input("To stop program running, type 'break'\nGive a word: ")
    if word == 'break':
        break
    if word in words: # checking if something exists in a dictionary
        print('Translation: '+words[word])
    else:
        define = input("Give a definition: ")
        words[word]=define

with open("jsondata.json", "w") as f:
    json.dump(words, f)
