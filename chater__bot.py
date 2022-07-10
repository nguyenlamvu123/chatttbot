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
    read_only=True,
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
        'chatterbot.preprocessors.convert_to_ascii',
        ],
    )
######################################################################################
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
trainer = ListTrainer(chatbot)
trainlists = []

trainlists.append([
    "Hi, can I help you",
    "Who are you?",
    "I am your virtual assistant. Ask me any questions...",
    "Where do you operate?",
    "We operate from Singapore",
    "What payment methods do you accept?",
    "We accept debit cards and major credit cards",
    "I would like to speak to your customer service agent",
    "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
    ])

trainlists.append([
    "What payment methods do you offer?",
    "We accept debit cards and major credit cards",
    "How to contact customer service agent",
    "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
    ])

for trainlist in trainlists:  
    trainer.train(trainlist)

trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train('chatterbot.corpus.english')

trainer.export_for_training('./db_export.json')

print('Type something to begin...')
# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()
        bot_response = chatbot.get_response(user_input)
        print(bot_response)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
######################################################################################
##from chatterbot.conversation import Statement
##label_a_statements = [
##    Statement(text='Hello', tags=['label_a']),
##    Statement(text='Hi', tags=['label_a']),
##    Statement(text='How are you?', tags=['label_a'])
##]
##label_b_statements = [
##    Statement(text='I like dogs.', tags=['label_b']),
##    Statement(text='I like cats.', tags=['label_b']),
##    Statement(text='I like animals.', tags=['label_b'])
##]
##
##chatbot.storage.create_many(
##    label_a_statements + label_b_statements
##)
### Return a response from "label_a_statements"
##response_from_label_a = chatbot.get_response(
##    'dog',
##    additional_response_selection_parameters={
##        'tags': ['label_a']
##    }
##)
##print('Response from label_a collection:', response_from_label_a.text)
##
### Return a response from "label_b_statements"
##response_from_label_b = chatbot.get_response(
##    'dog',
##    additional_response_selection_parameters={
##        'tags': ['label_b']
##    }
##)
##print('Response from label_b collection:', response_from_label_b.text)
