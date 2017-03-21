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

import article
import csv
import os
import sys
import utilities

from sklearn.externals import joblib

def predict(input_dir):
    '''
    Get genre probabilities for each text document in input directory.
    '''
    clf = joblib.load('model.pkl')

    with open('results.csv', 'wb') as fh:
        writer = csv.writer(fh, delimiter='\t')
        writer.writerow(['Filename'] + [utilities.genres[g][0].split('/')[0]
            for g in utilities.genres])

        for filename in [f for f in os.listdir(input_dir) if f.endswith('.txt')]:
            with open(input_dir + os.sep + filename) as ifh:
                print('Processing file: ' + filename)

                row = []
                row.append(filename)

                # Read input file
                doc = ifh.read().decode('utf-8')

                # Create article object and calculate features
                art = article.Article(text=doc)
                features = [art.features[f] for f in utilities.features]

                # Get probability for each genre
                proba = clf.predict_proba([features])[0]

                # Save results
                for g in utilities.genres:
                    row.append(str(proba[g - 1])[:6])
                writer.writerow(row)
                print(row[1:])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        predict(sys.argv[1])
    else:
        print('Invoke with ./predict.py [input_dir]')
