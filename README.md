# link-prediction
coursework2 of data mining
Knowledge graphs have become very critical resources to support many AI related applications, such as graph analytics, Q&A system, web search, etc. A knowledge graph is a multi-relational graph composed of entities as nodes and relations as different types of edges. An instance of edge is a triplet of fact (head entity, relation, tail entity) (denoted as (h, r, t)).

"This task, as the second project in EE448 course, asks you to infer missing links in an observed academic knowledge graph. To avoid internal information leakage, all the entities are encoded into 8-digit hexadecimal numbers."

 ![image](https://github.com/DanDanZee/link-prediction/edit/master/data/poster.jpg)
data:
train.csv - the training set, triplets are given in the format of (head, relation, tail).
test.csv - the test set. In each query only the head and relation is given and you should predict the possible tails.
sampleSubmission.csv - a sample submission file in the correct format

preprocess data:
entity2id.py - create an txt containing group(entity,id)
r2id.py      - create an txt containing group(relationship,id)

link prediction:
using method of TransE to predict possible new link

mix.py -voter combining results of TransE and TransR

 ![image](https://github.com/DanDanZee/link-prediction/edit/master/data/poster.jpg)
