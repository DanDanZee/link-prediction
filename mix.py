import csv
import re
id=1
with open('tryofn150m4.csv')as f1:
    with open('my_29th_submission.csv')as f2:
        with open('tryofn200m2.csv')as f3:
            with open('my_45th_submission.csv')as f4:
                with open('tryofn215m3.csv') as f5:
                    with open('tryofn225m2.csv') as f6:
                        with open('tryofn215m2.csv') as f7:
                            with open('tryofn225m3.csv') as f8:
                                with open('testofmix11.csv','w',newline="") as tm:
                                    writer=csv.writer(tm)
                                    writer.writerow(["QueryId","ExpectedTail"])
                                    reader=csv.DictReader(f1)
                                    reader2=csv.DictReader(f2)
                                    reader3=csv.DictReader(f3)
                                    reader4=csv.DictReader(f4)
                                    reader5 = csv.DictReader(f5)
                                    reader6 = csv.DictReader(f6)
                                    reader7=csv.DictReader(f7)
                                    reader8=csv.DictReader(f8)

                                    for i,j,k,p,ff5,ff6,ff7,ff8 in zip(reader,reader2,reader3,reader4,reader5,reader6,reader7,reader8):
                                        ent = {}
                                        a=i['ExpectedTail']
                                        t1=a.split(' ')
                                        t2=re.split('[\t\s]',j['ExpectedTail'])
                                        t3=k['ExpectedTail'].split(' ')
                                        t4=p['ExpectedTail'].split(' ')
                                        t5=ff5['ExpectedTail'].split(' ')
                                        t6 = ff6['ExpectedTail'].split(' ')
                                        t7=ff7['ExpectedTail'].split(' ')
                                        t8 = ff8['ExpectedTail'].split(' ')
                                        #print("t2:",t2)
                                        bb=0
                                        for b in t4:
                                            print("b:", b)
                                            ent[b] = -4+bb
                                            bb+=1

                                        for m in t1:
                                            if ent.__contains__(m):
                                                ent[m]-=1
                                            else:
                                                ent[m]=0
                                        nn=0
                                        for n in t2:
                                            #print("n:",n)
                                            if ent.__contains__(n):
                                                ent[n]-=2
                                            else:
                                                ent[n]=-2+nn
                                            nn+=1

                                        for tt3 in t3:
                                            print("tt3:",tt3)
                                            if ent.__contains__(tt3):
                                                ent[tt3]-=1
                                            else:
                                                ent[tt3]=0


                                        for tt5 in t5:
                                            if ent.__contains__(tt5):
                                                ent[tt5]-=1
                                            else:
                                                ent[tt5]=0

                                        for tt6 in t6:
                                            if ent.__contains__(tt6):
                                                ent[tt6]-=1
                                            else:
                                                ent[tt6]=0
                                        for tt7 in t7:
                                            if ent.__contains__(tt7):
                                                ent[tt7]-=1
                                            else:
                                                ent[tt7]=0
                                        for tt8 in t8:
                                            if ent.__contains__(tt8):
                                                ent[tt8]-=1
                                            else:
                                                ent[tt8]=0



                                        print('ent:',ent)
                                        items=ent.items()
                                        backitems = [[v[1], v[0]] for v in items]
                                        backitems.sort()
                                        result=[ backitems[i][1] for i in range(0,len(backitems))]
                                        print('key:',result[0],'value:',ent[result[0]])
                                        print('key:', result[1], 'value:', ent[result[1]])
                                        print('key:', result[2], 'value:', ent[result[2]])
                                        print('done')
                                        writer.writerow([id,result[0]+' '+result[1]+' '+result[2]])
                                        id+=1
                                        #print("value:",vv)




