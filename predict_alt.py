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

import csv
import json
import os
import urllib

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
    input_dir = '/home/jlo010/frame-generator/input/docs'
    url = 'http://www.kbresearch.nl/genre-classifier/?'

    with open('results.csv', 'wb') as res:

        csv_writer = csv.writer(res, delimiter='\t')
	
        for i, filename in enumerate([f for f in os.listdir(input_dir) if f.endswith('.txt')]):
            with open(input_dir + os.sep + filename) as f:
                print('Processing file: ' + filename)
                text = decode(f.read())

		query_string = urllib.urlencode({'text': text.encode('utf-8')})
                data = urllib.urlopen(url + query_string).read().decode('utf-8')
		print(data)

		data = json.loads(data)
		if i == 0:
		    csv_writer.writerow(['Filename'] + [genre for genre in data])
                csv_writer.writerow([filename] + [data[genre] for genre in data])

if __name__ == '__main__':
    main()
