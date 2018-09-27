import csv
import pandas as pd

rel=[]
m=0
with open('train.csv','r') as csvfile:
    with open('relation2id2.txt','w') as txtfile:
        reader=csv.DictReader(csvfile)
        for i in reader:
            if i['Relation'] not in rel:
                txtfile.write(str(m)+' ')
                txtfile.write(i['Relation']+'\n')
                rel.append(i['Relation'])
                m=m+1
