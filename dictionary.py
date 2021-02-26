import json
from difflib import get_close_matches


# Load json file
data = json.load(open("data.json"))


# function to get key as input and returns value
def get_definitions():
    word = input("Enter a word to see its definition: ")
    word = word.lower()
    if word in data:
        return data[word]
    else:
        best_match = get_close_matches(word, data.keys(), cutoff=0.8)
        if len(best_match) > 0:
            ys = input("Did you mean %s instead? [y/N]: " % best_match[0])
            if ys.lower() == 'y':
                return data[best_match[0]]
            else:
                return get_definitions()
        else:
            return "Word not found in dictionary."


def print_definitions(definitions):
    if type(definitions) == list:
        for i in range(0, len(definitions)):
            print(f"{i+1}. {definitions[i]}")
    else:
        print(definitions)


# print output
definitions = get_definitions()
print_definitions(definitions)
