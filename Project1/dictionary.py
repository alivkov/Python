import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Y for yes and N for no: " % get_close_matches(w, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.lower() == "n":
            return "The word does not exist. Please try again."
        else:
            return "Your query is BS."
    else:
        return 'The word does not exist. Please check.'

while True:
    word = input('Enter a word:')
    output = translate(word)
    if word == "**q":
        break
    else:
        if type(output) == list:
            for i in output:
                print(i)
        else:
            print(output)
