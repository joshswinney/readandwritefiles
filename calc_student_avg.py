import csv

infile = open('student_scores.csv')

student_file = csv.reader(infile, delimiter=',')

outfile = open('student_avg.csv', 'w')

for record in student_file:
    Name = record[0]
    grade1 = int(record[1])
    grade2 = int(record[2])
    grade3 = int(record[3])
    grade_total = grade1 + grade2 + grade3
    grade_avg = grade_total / 3
    outfile.write(Name + ',' + format(round(grade_avg,1)) + '\n')
      