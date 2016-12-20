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
import utilities

from sklearn.externals import joblib

def decode(s):
    encodings = ['utf-8', 'iso-8859-1']
    decoded = ''
    for e in encodings:
        try:
            decoded = s.decode(e)
            break
        except UnicodeDecodeError:
            continue
    return decoded

def main():
    clf = joblib.load('model.pkl')

    input_dir = '/Users/Juliette/Documents/Code/frame-generator/input/docs'

    with open('results.csv', 'wb') as res:
        csv_writer = csv.writer(res, delimiter='\t')
        for filename in [f for f in os.listdir(input_dir) if f.endswith('.txt')]:
            with open(input_dir + '/' + filename) as f:
                print('Processing file: ' + filename)
                doc = decode(f.read())
                art = article.Article(text=doc)
                features = [art.features[f] for f in utilities.features]
                genre_id = clf.predict([features])[0]
                genre = utilities.genres[genre_id][0].split('/')[0]
                proba = clf.predict_proba([features])[0][genre_id - 1]
                csv_writer.writerow([filename, genre, proba])
                print('Genre: ' + genre + ', probability: ' + str(proba))

if __name__ == '__main__':
    main()
