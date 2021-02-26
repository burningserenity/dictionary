import json
from difflib import get_close_matches


# Load json file
data = json.load(open("data.json"))


# function to get key as input and returns value
def get_definition():
    word = input("Enter a word to see its definition: ")
    word = word.lower()
    if word in data:
        return data[word]
    else:
        best_match = get_close_matches(word, data.keys(), cutoff=0.8)
        if len(best_match) > 0:
            return "Did you mean %s instead?" % best_match[0]
        else:
            return "Word not found in dictionary."


# print output
definition = get_definition()
print(definition)
