import json
Mydict={
    "intents": [
        {
            "tag": "greeting",
            "patterns": [
                "Hi",
                "Hey",
                "How are you",
                "Is anyone there?",
                "Hello",
                "Good day"
            ],
            "responses": [
                "Hey :-)",
                "Hello, thanks for visiting",
                "Hi there, what can i do for you",
                "Hi there, how can i help?"
            ]
        },
        {
            "tag": "goodbye",
            "patterns": [
                "By By",
                "see you later",
                "byyyy",
                "goodbye",
                "ok then bye",
                "bye"
            ],
            "responses": [
                "Hey :-)",
                "see you later, thanks for visiting",
                "have a nice day",
                "Bye! come back again soon."
            ]
        },
        {
            "tag": "thanks",
            "patterns": [
                "Thanks",

            ],
            "responses": [
                "Happy to help!",
                "Anytime!",

            ]
        },

    ]
}

s=json.dumps(Mydict)
with open('Mydata.json','w') as f:
    f.write(s)