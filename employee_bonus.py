import csv

infile = open('employeepay.csv', 'r')

employee_file = csv.reader(infile, delimiter=',')

#to skip a line if the file contains a header record
next(employee_file)

for record in employee_file:
    ID = record[0]
    first_name = record[1]
    last_name = record[2]
    salary = float(record[3])
    bonus = float(record[4])
    bonus_amt = bonus * salary
    total_pay = bonus_amt + salary 

    print(ID, first_name, last_name, salary, bonus, round(bonus_amt,1), total_pay)

   

    
