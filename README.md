# link-prediction
coursework2 of data mining

data:

train.csv - the training set, triplets are given in the format of (head, relation, tail).
test.csv - the test set. In each query only the head and relation is given and you should predict the possible tails.
sampleSubmission.csv - a sample submission file in the correct format

preprocess data:

entity2id.py - create an txt containing group(entity,id)
r2id.py      - create an txt containing group(relationship,id)

link prediction:

using method of TransE to predict possible new link

