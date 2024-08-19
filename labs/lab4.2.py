import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
#from submission_script import *
#from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':

    classifier = GaussianNB()
    dataset_sample = [list(map(float, row)) for row in dataset_sample]
    train_dataset = dataset_sample[:int(0.85*len(dataset_sample))]
    train_X = [row[:-1] for row in train_dataset]
    train_Y = [row[-1] for row in train_dataset]

    test_dataset = dataset_sample[int(0.85*len(dataset_sample)):]
    test_X = [row[:-1] for row in test_dataset]
    test_Y = [row[-1] for row in test_dataset]

    classifier.fit(train_X, train_Y)
    print(classifier.score(test_X, test_Y))
    test = input().split(" ")
    print(classifier.predict(test))
    print(classifier.predict_proba(test))
"""
import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':

    classifier = GaussianNB()
    dataset = [list(map(float, row)) for row in dataset]
    train_dataset = dataset[:int(0.85*len(dataset))]
    train_X = [row[:-1] for row in train_dataset]
    train_Y = [row[-1] for row in train_dataset]

    test_dataset = dataset[int(0.85*len(dataset)):]
    test_X = [row[:-1] for row in test_dataset]
    test_Y = [row[-1] for row in test_dataset]

    classifier.fit(train_X, train_Y)
    print(classifier.score(test_X, test_Y))
    test = input().split(" ")
    print(int(classifier.predict([test])[0]))
    print(classifier.predict_proba([test]))


    submit_train_data(train_X, train_Y)


    submit_test_data(test_X, test_Y)


    submit_classifier(classifier)

# povtoren import na kraj / ne ja otstranuvajte ovaa linija

"""