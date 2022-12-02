from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import os 


class Chater__bot:
    def __init__(
        self,
        name="Samgiongzon",
        storage_adapter=None,
##        storage_adapter='chatterbot.storage.SQLStorageAdapter',
##        storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
        logic_adapters=[
##            'chatterbot.logic.MathematicalEvaluation',
##            'chatterbot.logic.TimeLogicAdapter',
            'chatterbot.logic.BestMatch',
            ],
        database_uri=None,  # This database will be a temporary in-memory database
##        database_uri='sqlite:///database.sqlite3',
##        database_uri='mongodb://localhost:27017/chatterbot-database',
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace',
            'chatterbot.preprocessors.unescape_html',
            'chatterbot.preprocessors.convert_to_ascii',
            ],
        trainlists=None,
##        trainlists=[
##            "Hi, can I help you",
##            "Who are you?",
##            "I am your virtual assistant. Ask me any questions...",
##            "Where do you operate?",
##            "We operate from Singapore",
##            "What payment methods do you accept?",
##            "We accept debit cards and major credit cards",
##            "I would like to speak to your customer service agent",
##            "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday",
##            "What payment methods do you offer?",
##            "We accept debit cards and major credit cards",
##            "How to contact customer service agent",
##            "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday",
##            ]
        ):
        self.chatbot = ChatBot(
            name,
            storage_adapter=storage_adapter,
            logic_adapters=logic_adapters,
            read_only=True,
            preprocessors=preprocessors,
            ) if storage_adapter is not None else ChatBot(
            name,
            logic_adapters=logic_adapters,
            read_only=True,
            preprocessors=preprocessors,
            )
        if trainlists is not None:
            self.trainlists = trainlists
            self.trai_n()

    def trai_n(self):
        trainer = ListTrainer(self.chatbot)

        for stt in range(0, len(self.trainlists), 2):
            trainer.train(self.trainlists[stt:stt+2])
##        for trainlist in self.trainlists:  
##            trainer.train(trainlist)

        trainer_corpus = ChatterBotCorpusTrainer(self.chatbot)
##        trainer_corpus.train('chatterbot.corpus.english')

        trainer.export_for_training('./db_export.json')
##        trainer.export_for_training('./tmp/save_training.pickle')

    @staticmethod
    def savemode_l(cl=None):
        import cPickle
        if cl is not None:
            with open('./tmp/save_training.pickle','wb') as save_training:
                cPickle.dump(cl,save_training)  # SAVE TRAINED CLASSIFIER
        else:
            with open('./tmp/save_training.pickle','rb') as load_training:
                cl = cPickle.load(load_training) # LOAD TRAINED CLASSIFIER
##                [new_cl.prob_classify("love food").prob('pos'),new_cl.prob_classify("love food").prob('neg')]
            return cl
        
    def run(self):
        print('Type something to begin...')
        while True:
            try:
                user_input = input()
                bot_response = self.chatbot.get_response(user_input)
                print(bot_response)
            # Press ctrl-c or ctrl-d on the keyboard to exit
            except (KeyboardInterrupt, EOFError, SystemExit):
                break

    def getrespos_e(
        self,
        statements=None,
        ):
        from chatterbot.conversation import Statement
        if statements is None:
            statements=[
                Statement(text='Hello', tags=['label_a']),
                Statement(text='Hi', tags=['label_a']),
                Statement(text='How are you?', tags=['label_a']),
                Statement(text='I like dogs.', tags=['label_b']),
                Statement(text='I like cats.', tags=['label_b']),
                Statement(text='I like animals.', tags=['label_b']),
                ]
        statements = statements 
        
        self.chatbot.storage.create_many(statements)
        # Return a response from "label_a_statements"
        response_from_label_a = self.chatbot.get_response(
            'dog',
            additional_response_selection_parameters={
                'tags': ['label_a']
            }
        )
        print('Response from label_a collection:', response_from_label_a.text)
        
        # Return a response from "label_b_statements"
        response_from_label_b = self.chatbot.get_response(
            'dog',
            additional_response_selection_parameters={
                'tags': ['label_b']
            }
        )
        print('Response from label_b collection:', response_from_label_b.text)


if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), 'data', 'phapluat.txt')) as s:
        trainlists_ = s.read()
    trainlists = trainlists_.split('\n@@@@@@@@')
    samgiongzon = Chater__bot(trainlists=trainlists[:3])
##    samgiongzon = Chater__bot(trainlists=None)
    samgiongzon.run()
