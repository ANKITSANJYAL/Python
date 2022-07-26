import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        print("did you mean %s instead" % get_close_matches(word , data.keys())[0])
        decide = input("y or n")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            print("did you mean %s instead" % get_close_matches(word , data.keys())[1])
            decide2 = input("y or n")
            if decide == "y":
                return data[get_close_matches(word , data.keys())[1]]
            elif decide2 == "n":
                print("word is not available int the data !!! sorry !!!")
        else:
            print("please enter the valid input")
    else:
        print("word not available in data !!! sorry!!!")
repeat = "y"
while repeat == "y":
    word = input("enter the word to translate")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    repeat = input("y or n")