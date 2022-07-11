import random
from nltk.corpus import movie_reviews
from textblob.classifiers import NaiveBayesClassifier
random.seed(1)

train = [
    ('Tao thích ăn sandwich.', 'ăn'),
    ('Đây thật là một nơi đáng ngạc nhiên!', 'khen'),
    ('Bia ngon.', 'khen'),
    ('Đây là công việc tốt ngất của tao.', 'giới thiệu'),
    ("Đừng có ăn thịt gà", 'ăn'),
    ('Tao không thích nhà hàng này', 'ăn'),
    ('Tao là người ki bo.', 'giới thiệu'),
    ("Mai tao đi ăn xôi", 'ăn'),
    ('Phong cảnh rất đẹp!', 'khen'),
    ('Vợ tao thích thịt gà.', 'ăn'),
    ]
test = [
    ('Bia nặng quá.', 'ăn'),
    ('Tao là một người khó tính', 'giới thiệu'),
    ]

cl = NaiveBayesClassifier(train)

####### Grab some movie review data
######reviews = [(list(movie_reviews.words(fileid)), category)
######              for category in movie_reviews.categories()
######              for fileid in movie_reviews.fileids(category)]
######random.shuffle(reviews)
######new_train, new_test = reviews[0:100], reviews[101:200]
######
####### Update the classifier with the new training data
######cl.update(new_train)
######
####### Compute accuracy
######accuracy = cl.accuracy(test + new_test)
######print("Accuracy: {0}".format(accuracy))
######
####### Show 5 most informative features
######cl.show_informative_features(5)

# Classify some text
print(cl.classify("Táo dai quá."))  # "pos"
print(cl.classify("Tao ghét ăn nho."))   # "neg"

from textblob import TextBlob
# Classify a TextBlob
blob = TextBlob("tao 50 tuổi"
                "Sếp tao là một thằng ngu.", classifier=cl)
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test)))

# Show 5 most informative features
cl.show_informative_features(5)
