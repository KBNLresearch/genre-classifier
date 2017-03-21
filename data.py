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
import numpy as np
import utilities


class Dataset(object):
    '''
    A training set of labeled articles.
    '''

    def load_training(self, path):
        '''
        Transform tabular data set into NumPy arrays.
        '''
        # Load training data from csv file
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile, delimiter='\t')

            # Get number of examples
            num_examples = sum(1 for row in reader)
            print('Number of examples', num_examples)

            # Get number of features
            num_features = len(utilities.features)
            print('Number of features', num_features)

            dataset = np.ndarray(shape=(num_examples, num_features),
                    dtype=np.float64)
            labels = np.ndarray(shape=(num_examples, ), dtype=np.int32)

            # Add features and label for each article
            csvfile.seek(0)
            reader.next()
            for i, row in enumerate(reader):
                dataset[i, :] = [row[f] for f in utilities.features]
                labels[i] = row['label']

            print('Features:', dataset.shape)
            print('Labels:', labels.shape)
            return dataset, labels

    def generate_training(self, path):
        '''
        Generate training data from a list of labeled articles.
        '''
        with open(path, 'rU') as fh:
            db = csv.DictReader(fh, delimiter='\t')

        with open('data/training.txt', 'wb') as fh:
            fieldnames = ['url', 'label'] + utilities.features
            writer = csv.DictWriter(fh, fieldnames=fieldnames,
                delimiter='\t')
            writer.writeheader()

            for i, row in enumerate(db):

                # Get url
                url = None
                if row['Identifier']:
                    url = row['Identifier']
                elif (row['Prediction'] != 'None' and
                        float(row['Confidence']) > 0.675):
                    url = row['Prediction']
                else:
                    continue
                if not url.endswith(':ocr'):
                    url += ':ocr'

                # Get label
                label = None
                for g in utilities.genres:
                    if row['Genre'] in utilities.genres[g]:
                        label = g
                        break
                if not label:
                    continue

                # If valid training instance found, create new article
                try:
                    art = article.Article(url=url)

                    # Save results
                    fields = {'label': label, 'url': url}
                    for f in utilities.features:
                        fields[f] = art.features[f]
                    writer.writerow(fields)

                except (IOError, AssertionError) as e:
                    print('Error processsing article ' + url + ': '
                        + repr(e))

