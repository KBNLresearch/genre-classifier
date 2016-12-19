#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Genre Classifier
#
# Copyright (C) 2016 Juliette Lonij, Koninklijke Bibliotheek -
# National Library of the Netherlands
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import data
import sys

from sklearn import svm
from sklearn.model_selection import cross_val_score, StratifiedShuffleSplit
from sklearn.externals import joblib

dataset = data.Dataset()

class_weight = {1: 0.5, 2: 1, 3: 1, 4: 1, 5: 1, 6: 0.9, 7: 0.65, 8:1}
clf = svm.SVC(kernel='linear', C=1.5, decision_function_shape='ovr',
        class_weight=class_weight, probability=True)

def generate():
    # Generate new training set bases on the labeled data set
    dataset.generate_training('data/data.txt')

def validate():
    # Load an existing training set
    X_train, y_train = dataset.load_training('data/training.txt')

    # Ten-fold cross-validation with stratified sampling
    cv = StratifiedShuffleSplit(n_splits=10)
    scores = cross_val_score(clf, X_train, y_train, cv=cv)
    print("Accuracy: %0.4f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

def train():
    # Load an existing training set
    X_train, y_train = dataset.load_training('data/training.txt')

    # Train and save model
    clf.fit(X_train, y_train)
    joblib.dump(clf, 'model.pkl')

def predict():
    # Load an existing training set
    X_train, y_train = dataset.load_training('data/training.txt')

    # Load trained model and predict new example
    clf = joblib.load('model.pkl')
    logits = clf.decision_function([X_train[0]])
    proba = clf.predict_proba([X_train[0]])
    print logits
    print proba

if __name__ == '__main__':
    #generate()
    #validate()
    #train()
    predict()
