import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
#from submission_script import *
#from dataset_script import dataset
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    encoder = OrdinalEncoder()
    classifier = CategoricalNB()
    encoder.fit([row[:-1] for row in dataset_sample])

    train_data = dataset_sample[:int(0.75*len(dataset_sample))]
    train_X = [row[:-1] for row in train_data]
    train_Y = [row[-1] for row in train_data]

    train_X = encoder.transform(train_X)

    test_data = dataset_sample[int(0.75*len(dataset_sample)):]
    test_X = [row[:-1] for row in test_data]
    test_Y = [row[-1] for row in test_data]

    test_X = encoder.transform(test_X)

    classifier.fit(train_X, train_Y)

    print(classifier.score(test_X, test_Y))
    test = list(input().split(" "))
    test = encoder.transform([test])
    predicted = classifier.predict(test)
    probability = classifier.predict_proba(test)
    print(predicted[0])
    print(probability)
"""
import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    encoder = OrdinalEncoder()
    classifier = CategoricalNB()
    encoder.fit([row[:-1] for row in dataset])

    train_data = dataset[:int(0.75*len(dataset))]
    train_X = [row[:-1] for row in train_data]
    train_Y = [row[-1] for row in train_data]

    train_X = encoder.transform(train_X)

    test_data = dataset[int(0.75*len(dataset)):]
    test_X = [row[:-1] for row in test_data]
    test_Y = [row[-1] for row in test_data]

    test_X = encoder.transform(test_X)

    classifier.fit(train_X, train_Y)
    
    print(classifier.score(test_X, test_Y))
    test = list(input().split(" "))
    test = encoder.transform([test])
    predicted = classifier.predict(test)
    probability = classifier.predict_proba(test)
    print(predicted[0])
    print(probability)
    
    submit_train_data(train_X, train_Y)
    submit_test_data(test_X, test_Y)
    submit_classifier(classifier)
    submit_encoder(encoder)

"""
