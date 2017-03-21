# Genre Classifier

Genre classifier for Dutch historical newspaper articles.

## Background

The Genre Classifier was created in collaboration with Frank Harbers (RUG) in the context of his KB Researcher-in-residence project Discerning Journalistic Styles. It is a first attempt to automate the classification of genre of historical newspaper articles by examining textual features such as article length, personal pronouns, adjectives and named entities appearing in the text. The classifier was trained and evaluated using an existing labeled dataset (not publicly available), resulting in a prediction accuracy of approximately 65%.

## Usage

The trained classifier can be applied to a folder of plain text files using the prediction script provided:

`./predict.py [input_dir]`

The features calculated for a single article can be obtained running the article script with the article url as an argument:

`./article.py [article_url]`

## Demo
An online demo visualizing the classifier result for a single article is available at http://www.kbresearch.nl/genre/.
