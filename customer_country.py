import csv

infile = open('customers.csv', 'r')

customer_file = csv.reader(infile, delimiter=',')

#to skip a line if the file contains a header record
next(customer_file)

outfile = open('customer_country.csv', 'w')

for record in customer_file:
    first_name = record[1]
    last_name = record[2]
    Country = record[4]
    outfile.write(first_name + ',' + last_name +',' + Country + '\n')
    
   