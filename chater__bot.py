##https://github.com/gunthercox/ChatterBot/tree/master/examples
from chatterbot import ChatBot
##import logging
##logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    "Samgiongzon",
##    storage_adapter='chatterbot.storage.SQLStorageAdapter',
####    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
##        'chatterbot.logic.MathematicalEvaluation',
##        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
    ],
##    database_uri='sqlite:///database.sqlite3',
##    database_uri=None,  # This database will be a temporary in-memory database
####    database_uri='mongodb://localhost:27017/chatterbot-database',
##    read_only=True,
    )
######################################################################################
##from chatterbot.trainers import ListTrainer
##trainer = ListTrainer(chatbot)
##
##small_convo = [  
##    'Hi there!',  
##    'Hi',  
##    'How do you do?',  
##    'How are you?',  
##    'I\'m cool.',  
##    'Always cool.',  
##    'I\'m Okay',  
##    'Glad to hear that.',  
##    'I\'m fine',  
##    'I feel awesome',  
##    'Excellent, glad to hear that.',  
##    'Not so good',  
##    'Sorry to hear that.',  
##    'What\'s your name?',  
##    ' I\'m Sakura. Ask me a math question, please.'  
##    ]  
##  
##math_convo_1 = [  
##    'Pythagorean theorem',  
##    'a squared plus b squared equals c squared.'  
##    ]  
##  
##math_convo_2 = [  
##    'Law of Cosines',  
##    'c**2 = a**2 + b**2 - 2*a*b*cos(gamma)'  
##    ]
##list_trainee = ListTrainer(myBot)  
##for i in (small_convo, math_convo_1, math_convo_2):  
##    trainer.train(i)
##trainer.export_for_training('./my_export.json')
##
##print('Type something to begin...')
### The following loop will execute each time the user enters input
##while True:
##    try:
##        user_input = input()
##        bot_response = chatbot.get_response(user_input)
##        print(bot_response)
##    # Press ctrl-c or ctrl-d on the keyboard to exit
##    except (KeyboardInterrupt, EOFError, SystemExit):
##        break
######################################################################################
from chatterbot.conversation import Statement
label_a_statements = [
    Statement(text='Hello', tags=['label_a']),
    Statement(text='Hi', tags=['label_a']),
    Statement(text='How are you?', tags=['label_a'])
]
label_b_statements = [
    Statement(text='I like dogs.', tags=['label_b']),
    Statement(text='I like cats.', tags=['label_b']),
    Statement(text='I like animals.', tags=['label_b'])
]

chatbot.storage.create_many(
    label_a_statements + label_b_statements
)
# Return a response from "label_a_statements"
response_from_label_a = chatbot.get_response(
    'dog',
    additional_response_selection_parameters={
        'tags': ['label_a']
    }
)
print('Response from label_a collection:', response_from_label_a.text)

# Return a response from "label_b_statements"
response_from_label_b = chatbot.get_response(
    'dog',
    additional_response_selection_parameters={
        'tags': ['label_b']
    }
)
print('Response from label_b collection:', response_from_label_b.text)
