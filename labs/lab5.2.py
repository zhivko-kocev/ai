import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.ensemble import RandomForestClassifier

if __name__ == '__main__':
    col_index = int(input())
    num_trees = int(input())
    criterion = input()
    test_case = list(map(int, input().split(' ')))
    test_case = test_case[:col_index] + test_case[col_index+1:]

    dataset = [data[:col_index] + data[col_index+1:] for data in dataset]

    train_set = dataset[:int(0.85 * len(dataset))]
    train_x = [t[:-1] for t in train_set]
    train_y = [t[-1] for t in train_set]

    test_set = dataset[int(0.85 * len(dataset)):]
    test_x = [t[:-1] for t in test_set]
    test_y = [t[-1] for t in test_set]

    classifier = RandomForestClassifier(criterion=criterion, random_state=0, n_estimators=num_trees)
    classifier.fit(train_x, train_y)

    print(f'Accuracy: {classifier.score(test_x, test_y)}')

    predicted_class = classifier.predict([test_case])[0]
    probabilities = classifier.predict_proba([test_case])[0]

    print(predicted_class)
    print(probabilities)

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_x, train_y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_x, test_y)

    # submit na klasifikatorot
    submit_classifier(classifier)
