import csv
import pandas as pd

ent=[]
ent1=[]
m=0
n=0
with open('ttt.txt','r') as csvfile:
    with open('e1.txt','w') as txtfile1:
        with open('e2.txt','w') as txtfile:
            reader=csv.DictReader(csvfile)
            for i in reader:
                if i['Relation']== 'author_is_in_field':
                    if i['Head'] not in ent:
                        txtfile.write(str(m)+' ')
                        txtfile.write(i['Head']+'\n')
                        ent.append(i['Head'])
                        m=m+1
                        print('head:',m)
                    if i['Tail'] not in ent:
                        txtfile.write(str(m) + ' ')
                        txtfile.write(i['Tail'] + '\n')
                        ent.append(i['Tail'])
                        m=m+1;
                        print('tail:',m)
                else:
                    if i['Head'] not in ent1:
                        txtfile1.write(str(n)+' ')
                        txtfile1.write(i['Head']+'\n')
                        ent1.append(i['Head'])
                        n=n+1
                        print('head:',n)
                    if i['Tail'] not in ent1:
                        txtfile1.write(str(n) + ' ')
                        txtfile1.write(i['Tail'] + '\n')
                        ent1.append(i['Tail'])
                        n=n+1;
                        print('tail:',n)


