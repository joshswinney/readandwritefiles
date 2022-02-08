import csv

infile = open('employeepay.csv', 'r')

employee_file = csv.reader(infile, delimiter=',')

#to skip a line if the file contains a header record
next(employee_file)

outfile = open('employee_bonus.csv', 'w')

for record in employee_file:
    Name = 
    Bonus = 
    Salary = 

    


for record in customer_file:
    Name = record[1] + ' ' + record[2]
    Country = record[4]
    outfile.write(Name + ' ' + Country + '\n')