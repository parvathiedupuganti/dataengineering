"""f_sample = open("sample.txt")
read_content = f_sample.read();
print(read_content)
f_sample.close()

#f_demo = open("demo.txt",'w')
f_demo = open("demo.txt",'a')
'''f_demo.write("Programming in python by Parag Joshi\n")
f_demo.write("Topics covered \n")
f_demo.write("Datatypes,Modules,control flow \n");
'''
f_demo.write("*"*70)
f_demo.close();
"""

import csv
"""
with open('portfolio.csv',mode='w',newline='') as pfile:
    pfile_writer = csv.writer(pfile,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
    #pfile_writer.writerow("Portfolio List, Parag Joshi")
    pfile_writer.writerow(['Stock Name','Quantity','Stock Price'])
    pfile_writer.writerow(['Infosys',10,2700])
    pfile_writer.writerow(['UST',5,3200])
    """

with open('portfolio.csv',mode='r') as pfile:
    csv_reader = csv.reader(pfile,delimiter=",")
    line_count = 0;
    for row in csv_reader:
        if line_count == 0:
            print(f'{",".join(row)}')
            line_count += 1;
        else:
            print(f'{row[0]}\t{row[1]}\t{row[2]}')
            line_count += 1;
    
        """print(f'{row[0]} {row[1]} {row[2]}')
        line_count += 1;"""
    print(f'Read {line_count-1} shares from the portfolio')

"""data = [
        ['Name','Age','City'],
        ['Parag Joshi','40','Pune,Maharashtra'],
        ['Jane Smith','25','Mumbai']
      ]
with open ('output.csv','w',newline='') as f:
    writer = csv.writer(f,quotechar="'",quoting=csv.QUOTE_ALL);
    writer.writerows(data)""" 


