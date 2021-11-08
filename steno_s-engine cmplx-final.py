# here we learn how to add a variable in a dictionary.
# and how to later append a value to that variable key.
# variables,strings,keys | tuples,dict - are similar
import  requests
import json
app_key = '70af5239f6b20becd18a2e92e7cbe724'
language = 'en-gb'
app_id = '9f0905e0'

print("Enter your query : \n")
query = str(input())
abbr = {"ASAP": "As soon as possible", "LMK": "Let me know", "TBA": "To be announced", "TBH": "To be honest",
        "TBC": "To be confirmed", "TGIF": "Thank God its Friday", "DIY": "Do it yourself",
        "RSVP": "Please wait(in french)", "BRB": "Be right back", "IMO": "In my opinion", "IDK": "I don't know",
        "AKA": "Also known as", "N/A": "Not available", "IRL": "In real life", "RT": "Retweet",
        "WDYM": "What do you mean", "TBT": "Throwback Thursday", "NBD": "No big deal", "ICYMI": "In case you missed it",
        "FOMO": "Fear of missing out", "NP": "No Problem", "WDYD": "What do you did", "LOL": "Laugh out loud",
        "ROFL": "Rolling on the floor laughing", "LMAO": "Laughing my ass off", "BTW": "By the way",
        'SOS': "Save our ship/soul", "YOLO": "You only live once", 'query': {}}

print(abbr.get(query, "Sorry I don't know that,yet.\n"))

while True:
    print("Enter your query : \n")
    query = str(input())
    print(abbr.get(query, "Sorry I don't know that,yet.\n"))
    if query not in abbr:
        break

conf = str((input("Can you find it and tell me yourself the full form?\n")))
if conf == "Yes":
    FF = str(input("What is it? \n"))
    abbr[query] = FF
    print(str(query)+" means " + abbr[query] + ".")
else:
    conf2 = input("Should I google it for you?\n")
    if conf2=="Yes":
        url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + query.lower()
        r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
        if r:
         mean_json = r.json()
         mean_list = []

         for result in mean_json['results']:
          for lexicalEntry in result['lexicalEntries']:
            for entry in lexicalEntry['entries']:
                for sense in entry['senses']:
                    mean_list.append(sense['definitions'][0])

                print(query + " stands for:")

                for i in mean_list:
                  print(i)
                
    
        else:
          print("Extremely sorry.I didn't find anything.\n")
    
    else:
      print("As you wish,sire.\n")

def stenox():
    app_key = '70af5239f6b20becd18a2e92e7cbe724'
    language = 'en-gb'
    app_id = '9f0905e0'
    print("Enter your query : \n")
    query = str(input())
    abbr = {"ASAP": "As soon as possible", "LMK": "Let me know", "TBA": "To be announced", "TBH": "To be honest",
            "TBC": "To be confirmed", "TGIF": "Thank God its Friday", "DIY": "Do it yourself",
            "RSVP": "Please wait(in french)", "BRB": "Be right back", "IMO": "In my opinion", "IDK": "I don't know",
            "AKA": "Also known as", "N/A": "Not available", "IRL": "In real life", "RT": "Retweet",
            "WDYM": "What do you mean", "TBT": "Throwback Thursday", "NBD": "No big deal",
            "ICYMI": "In case you missed it",
            "FOMO": "Fear of missing out", "NP": "No Problem", "WDYD": "What do you did", "LOL": "Laugh out loud",
            "ROFL": "Rolling on the floor laughing", "LMAO": "Laughing my ass off", "BTW": "By the way",
            'SOS': "Save our ship/soul", "YOLO": "You only live once", 'query': {}}

    print(abbr.get(query, "Sorry I don't know that,yet.\n"))

    while True:
        print("Enter your query : \n")
        query = str(input())
        print(abbr.get(query, "Sorry I don't know that,yet.\n"))
        if query not in abbr:
            break

    conf = str((input("Can you find it and tell me yourself the full form?\n")))
    if conf == "Yes":
        FF = str(input("What is it? \n"))
        abbr[query] = FF
        print(str(query) + " means " + abbr[query] + ".")
    else:
        conf2 = input("Should I google it for you?\n")
        if conf2 == "Yes":
            url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + language + '/' + query.lower()
            r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
            if r:
                mean_json = r.json()
                mean_list = []

                for result in mean_json['results']:
                    for lexicalEntry in result['lexicalEntries']:
                        for entry in lexicalEntry['entries']:
                            for sense in entry['senses']:
                                mean_list.append(sense['definitions'][0])

                            print(query + " stands for:")

                            for i in mean_list:
                                print(i)
                                

            else:
                print("Extremely sorry.I couldn't find anything.\n")
                

        else:
            print("As you wish,sire.\n")

while True:
    stenox()