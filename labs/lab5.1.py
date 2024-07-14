import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

if __name__ == '__main__':
    X = int(input())
    X = round(X / 100, 2)

    criterion = input()

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[int(round(1 - X, 2) * len(dataset)):]
    train_x = [t[:-1] for t in train_set]
    train_x = encoder.transform(train_x)
    train_y = [t[-1] for t in train_set]

    test_set = dataset[:int(round(1 - X, 2) * len(dataset))]
    test_x = [t[:-1] for t in test_set]
    test_x = encoder.transform(test_x)
    test_y = [t[-1] for t in test_set]

    classifier = DecisionTreeClassifier(criterion=criterion, random_state=0)
    classifier.fit(train_x, train_y)

    print(f'Depth: {classifier.get_depth()}')
    print(f'Number of leaves: {classifier.get_n_leaves()}')

    print(f'Accuracy: {classifier.score(test_x,test_y)}')

    feature_importances = list(classifier.feature_importances_)
    # print(f'Feature importances: {feature_importances}')

    most_important_feature = feature_importances.index(max(feature_importances))
    print(f'Most important feature: {most_important_feature}')

    least_important_feature = feature_importances.index(min(feature_importances))
    print(f'Least important feature: {least_important_feature}')

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_x, train_y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_x, test_y)

    # submit na klasifikatorot
    submit_classifier(classifier)

    # submit na encoderot
    submit_encoder(encoder)
