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
import data
import json
import os
import utilities

from bottle import get
from bottle import request
from bottle import route
from bottle import run

from sklearn.externals import joblib
from sklearn import svm

@get('/')
def index():
    '''
    Return the probability for each genre.
    '''
    if not (request.query.text or request.query.url):
        return 'invoke with ?text= or ?url='

    if request.query.text:
        art = article.Article(text=request.query.text)
    elif request.query.url:
        art = article.Article(url=request.query.url)

    example = [art.features[f] for f in utilities.features]

    abs_path = os.path.dirname(os.path.realpath(__file__))
    clf = joblib.load(abs_path + os.sep + 'model.pkl')
    proba = clf.predict_proba([example])[0]

    resp = {}
    for i, p in enumerate(proba):
        resp[utilities.genres[i + 1][0].split('/')[0]] = str(proba[i])[:6]
    resp = json.dumps(resp)

    if request.query.callback:
        resp = request.query.callback + '(' + resp + ')'

    return resp

if __name__ == '__main__':
    run(host='localhost', port=8090)
