import csv

ident = []
amount = []
exp = []

with open('loans.csv')  as csvfile:         # process the csv file
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV:
        ident.append(int(row[0]))
        amount.append(int(row[1]))
        exp.append(int(row[2]))
        

indexes = []
lst = []

for i in range(len(exp)):
    if(exp[i] < 10):            # skip all the people with experience less than 10
        continue
    if(sum(lst) < 500000):      # add all the values until the 500k mark is reached
        lst.append(amount[i])
        indexes.append(amount.index(amount[i]))
        print(lst.index(amount[i]), amount[i])
        
        
    else:
        if(amount[i] < max(lst)):
            indexes.remove(lst.index(max(lst)))
            lst.remove(max(lst))
            print(lst, indexes)
            lst.append(amount[i])
            indexes.append(amount.index(amount[i]))
            indexes.append(lst.index(amount[i]))
            print(lst, indexes)
            
                                                
            
print(indexes, '\n')
print(lst)
