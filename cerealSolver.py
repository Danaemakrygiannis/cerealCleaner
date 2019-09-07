#import modules
import os 
import csv 


#open CSV
cerealCSV= os.path.join(".","resources", "cereal.csv")
with open(cerealCSV, "r", encoding="UTF-8") as csvfile:
   
    #create my csv reader
    csvreader = csv.reader(csvfile,delimiter=",")
    csvHeader= next(csvreader)
    print(f"The header is: {csvHeader}")

    #itireate rows (for loop)
    for row in csvreader:
    #if statment (if the cereal contains 5 or more grams of fibber, print)
        if float(row[7]) >= 5:
            #print row if condition meets
            print(row)
            
#if statement ( if the cereal contains 5 or more grams of fiber, print)

#print row if condition meets






