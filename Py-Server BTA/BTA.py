print("Processing.....")

import nltk
import random,pickle
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier

from sklearn.naive_bayes import MultinomialNB, GaussianNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC,LinearSVC,NuSVC

from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize

class VoteClassifier(ClassifierI):
    def __init__(self,*classifiers):
        self._classifiers=classifiers
    def classify(self,features):
        votes=[]
        for c in self._classifiers:
            v=c.classify(features)
            votes.append(v)
        return mode(votes)
    def confidence(self,features):
        votes=[]
        for c in self._classifiers:
            v=c.classify(features)
            votes.append(v)
        choice_votes=votes.count(mode(votes))
        conf=choice_votes/len(votes)
        return conf
print("Collecting Data..")

short_pos=open("positive.txt","r").read()
short_neg=open("negative.txt","r").read()
print("Data Collecting")
all_words=[]
documents=[]

allowed_word_types=["J"]
print("Processing Data...")
for r in short_pos.split('\n'):
    documents.append((r,"pos"))
    words=word_tokenize(r)
    pos=nltk.pos_tag(words)
    for w in pos:
        if(w[1][0] in allowed_word_types):
            all_words.append(w[0].lower())
for r in short_neg.split('\n'):
    documents.append((r,"neg"))
    words=word_tokenize(r)
    pos=nltk.pos_tag(words)
    for w in pos:
        if(w[1][0] in allowed_word_types):
            all_words.append(w[0].lower())

##save_documents = open("pickled_algos/documents.pickle","wb")
##pickle.dump(documents, save_documents)
##save_documents.close()

print("Data Processed")
all_words=nltk.FreqDist(all_words)
#print(all_words.most_common(15))
word_features=list(all_words.keys())[:3000]

##save_word_features = open("pickled_algos/word_features5k.pickle","wb")
##pickle.dump(word_features, save_word_features)
##save_word_features.close()
print("Training and Testing")
def find_features(document):
    words=word_tokenize(document)
    features={}
    for w in word_features:
        features[w]=(w in words)
    return features
#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets=[(find_features(rev),category)for (rev,category) in documents]

random.shuffle(featuresets)

training_set=featuresets[:1000]
testing_set=featuresets[1000:]

print("Naive Bayes")
classifier=nltk.NaiveBayesClassifier.train(training_set)
#classifier_f=open("naivebayes.pickle","rb")
#classifier=pickle.load(classifier_f)
#classifier_f.close()
kygo=(nltk.classify.accuracy(classifier,testing_set))*100
print("Original Naive Bayes accuracy:",kygo)
if(kygo>90.0):
    print("This is a must buy product,it is highly recommended")
elif(kygo>75.0):
    print("This is a good product with most positive comments")
elif(kygo>50.0):
    print("This is a average product with mixed comments")
elif(kygo<50.0):
    print("It is recommended not to buy this product")



classifier.show_most_informative_features(15)
#save_classifier=open("naivebayes.pickle","wb")
#pickle.dump(classifier,save_classifier)
#save_classifier.close()

#MNB_classifier=SklearnClassifier(MultinomialNB())
#MNB_classifier.train(training_set)
#print("mnb classifier",(nltk.classify.accuracy(MNB_classifier,testing_set))*100)

print("Bernoulli NB")
Ber_classifier=SklearnClassifier(BernoulliNB())
Ber_classifier.train(training_set)
print("Bernoulli classifier accuracy",(nltk.classify.accuracy(Ber_classifier,testing_set))*100)

#gas_classifier=SklearnClassifier(GaussianNB())
#gas_classifier.train(training_set)
#print("gs classifier",(nltk.classify.accuracy(gas_classifier,testing_set))*100)

print("logistic Regression")
LogisticRegression_classifier=SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression classifier accuracy ",(nltk.classify.accuracy(LogisticRegression_classifier,testing_set))*100)

print("SGDC Classifier")
SGDClassifier_classifier=SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier classifier accuracy",(nltk.classify.accuracy(SGDClassifier_classifier,testing_set))*100)

#SVC_classifier=SklearnClassifier(SVC())
#SVC_classifier.train(training_set)
#print("ber classifier",(nltk.classify.accuracy(SVC_classifier,testing_set))*100)

print("Linear SVC")
LinearSVC_classifier=SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC",(nltk.classify.accuracy(LinearSVC_classifier,testing_set))*100)

print("NuSVC Classifier")
NuSVC_classifier=SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier accuracy",(nltk.classify.accuracy(NuSVC_classifier,testing_set))*100)


print("Voting Classier")
voted_classifier=VoteClassifier(classifier,
                                Ber_classifier,
                                LogisticRegression_classifier,
                                NuSVC_classifier,
                                LinearSVC_classifier,
                                SGDClassifier_classifier)
print("voted_classifier accuracy",kygo)
if(kygo>90.0):
    print("This is a must buy product,it is highly recommended")
elif(kygo>75.0):
    print("This is a good product with most positive comments")
elif(kygo>50.0):
    print("This is a average product with mixed comments")
elif(kygo<50.0):
    print("It is recommended not to buy this product")

def recommendation(text):
    feats=find_features(text)
    return voted_classifier.classify(feats)

print("End of Program")