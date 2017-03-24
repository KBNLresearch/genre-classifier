# Genre Classifier

Genre classifier for Dutch historical newspaper articles.

## Background

The Genre Classifier was created in collaboration with Frank Harbers (RUG) in the context of his KB Researcher-in-residence project Discerning Journalistic Styles. It is a first attempt to automate the classification of historical newspaper articles according to genre by examining features such as article length, personal pronouns, adjectives and named entities appearing in the text. The classifier was trained and evaluated using an existing labeled dataset (not publicly available), resulting in a prediction accuracy of approximately 65%.

## Usage

The trained classifier can be applied to a folder of utf-8 encoded plain text files using the prediction script provided:

`./predict.py [input_dir]`

To view the features calculated for a single article run the article script with the article url as an argument:

`./article.py [article_url]`

## Demo
An online demo visualizing the classifier result for a single article is available at http://www.kbresearch.nl/genre/.
