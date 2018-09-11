import csv

cand = []

with open('loans.csv')  as csvfile:         # process the csv file
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV:
        ident = int(row[0])
        amount = int(row[1])
        exp = int(row[2])
        cand.append((ident,amount,exp))
        

lst = []


def Sum(ltup, col):                             #Function that returns the sum of any given of the column in the list of tuples
    s = 0
    for i in range(len(ltup)):
        s = s + ltup[i][col]

    return s

def Max(ltup,col):                              #Function that returns the tuple with the maximum value of any given column
    n = (0,0,0)
    for i in range(len(ltup)):
        if( n[col] < ltup[i][col]):
            n = ltup[i]

    return n


for i in range(len(cand)):
    if(cand[i][2] < 10):                        # skip all the people with experience less than 10
        continue
    if(Sum(lst,1) < 500000):                    # add all the values until the 500k mark is reached
        lst.append(cand[i])
        
        
    else:
        if(cand[i][1] <= Max(lst,1)[1]):
            print(lst)
            lst.remove(Max(lst,1))         
            lst.append(cand[i])



with open('eggs.csv') as csvfile1:
    csvwriter = csv.writer(csvfile, delimiter=',')
                            
    

                                            
