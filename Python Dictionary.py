import json
from difflib import get_close_matches
data=json.load(open('data.json'))
def explain(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        choice=input('did you mean {0} instead? Enter Y if yes or try another word:' .format(get_close_matches(w,data.keys())[0]))
        option=choice.upper()
        if option=='Y':
            return data[get_close_matches(w,data.keys())[0]]
        else:
            return "Try another word!!!"
    else:
        return ("The Word doesn't exist")

word=input("Enter Your Word:")
output=explain(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)