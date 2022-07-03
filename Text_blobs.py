from da_ta import da_ta as s
# Compute accuracy
print("Accuracy: {0}".format(s.cl.accuracy(s.test)))
# Show 5 most informative features
##cl.show_informative_features(5)

##https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
import nltk
nltk.download('punkt')

##with open('train.json', 'r') as fp:
##    cl = NaiveBayesClassifier(fp, format="json")

########import random
########random.seed(1)
########nltk.download('movie_reviews')
########from nltk.corpus import movie_reviews
######### Grab some movie review data
########reviews = [(list(movie_reviews.words(fileid)), category)
########              for category in movie_reviews.categories()
########              for fileid in movie_reviews.fileids(category)]
########random.shuffle(reviews)
########new_train, new_test = reviews[0:100], reviews[101:200]
########
######### Update the classifier with the new training data
########cl.update(new_train)
########
######### Compute accuracy
########accuracy = cl.accuracy(test + new_test)
########print("Accuracy: {0}".format(accuracy))
########
######### Show 5 most informative features
########cl.show_informative_features(5)

# Classify some text
##print(cl.classify("Táo dai quá."))  # "pos"
##print(cl.classify("Tao ghét ăn nho."))   # "neg"
##
while True:
    samgiongzon = input('có gì hot ? ')
    prob_dist = s.cl.prob_classify(samgiongzon)
    print(prob_dist.max())
    print('thời tiết: ', round(prob_dist.prob('thời tiết'), 2))
    print('thời gian: ', round(prob_dist.prob('thời gian'), 2))
    print('tài chính: ', round(prob_dist.prob('tài chính'), 2))

##from textblob import TextBlob
### Classify a TextBlob
##blob = TextBlob("tao 50 tuổi.", classifier=s.cl)
##print(blob)
##print(blob.classify())

##for sentence in blob.sentences:
##    print(sentence)
##    print(sentence.classify())
