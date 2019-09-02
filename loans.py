"""Sivenathi Mgudlwa"""

import csv


path = input("please input the csv file name: ")
if len(path) == 0:
    path ="loans.csv"

cand = []    
with open(path)  as csvfile:         # process the csv file to extract data
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV:
        ident = int(row[0])
        amount = int(row[1])
        exp = int(row[2])
        cand.append((ident,amount,exp))
        




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

def Min(ltup, col):                             #Find the minimum from list of tuples given a column
    n = ltup[0]
    for i in range(len(ltup)):
        if( n[col] > ltup[i][col]):
            n = ltup[i]
    return n

"""----------------------------Question 1-------------------------------------------------"""
lst = []
def MaxLoans():                                      
    for i in range(len(cand)):
        if(cand[i][2] < 10):                        # skip all the people with experience less than 10
            continue
        if(Sum(lst,1) < 500000):                    # add all the values until the 500k mark is reached
            lst.append(cand[i])
        
        
        else:
            if(cand[i][1] <= Max(lst,1)[1]):
                lst.remove(Max(lst,1))         
                lst.append(cand[i])

    lst.remove(Max(lst, 1))
   
"""---------------------------Question 2---------------------------------------------------"""    


lst1 = []
def Experience():
    for i in range(len(cand)):
        if(Sum(lst1,1) < 500000):                    # add all the values until the 500k mark is reached
            lst1.append(cand[i])

        else:
            if(cand[i][2] >= Min(lst1,2)[2]):
                lst1.remove(Min(lst1,2))
                lst1.append(cand[i])
    lst1.remove(Min(lst1, 2))            
   



"""------------------------------------------------------------------------------"""

MaxLoans()
Experience()

with open('maximum_number_loans.csv','w', newline='') as csvfile1:          #Output csv file for Question 1
    
    csvwriter = csv.writer(csvfile1, delimiter=',')
    csvwriter.writerow(("id" , "amount", "experience"))

    for tup in lst:
        csvwriter.writerow(tup)
    csvwriter.writerow(("total number of loans",len(lst)))
    csvwriter.writerow(("total amount",Sum(lst, 1)))
    
    
with open('maximum_experience_loans.csv','w', newline='') as csvfile1:      #Output csv file for Quesion 2
    
    csvwriter = csv.writer(csvfile1, delimiter=',')
    csvwriter.writerow(("id" , "amount", "experience"))

    for tup in lst:
        csvwriter.writerow(tup)
    csvwriter.writerow(("total years of experience",Sum(lst1, 2)))
    csvwriter.writerow(("total amount",Sum(lst1, 1)))        
                            

print("Done!")    

                                            
