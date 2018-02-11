import unicodedata # This module is used to obtain Euro currency symbol
from babel.numbers import format_decimal # This module is used to comma seperate the numbers
from babel.numbers import format_currency
import argparse


#Use Arg Parse to pick field and operation
parser = argparse.ArgumentParser()
parser.add_argument("--field N",type=int, help="Convert CSV field N",dest="field")
parser.add_argument("--multiplier N",type=float, help="Multiply currency value by N for the current conversion rate",dest="multiplier")
parser.add_argument("-i inputfile",help="Read from input file (or stdin)", dest="inputfile")
parser.add_argument("-o outputfile",help="Write to output file (or stdout)", dest="outputfile")                  
args = parser.parse_args()

#1. Open File read data
with open(args.inputfile, 'r') as f:
    results = []
    #2. Convert data to list because we are not allowed to use csv module
    for line in f:
            data = line.split(',')
            results.append(data[0:])
    for i in range(len(results)):
        if i!=0:
        #3. Change value to cuntry specific value 
            results[i][args.field-1] = (float(results[i][args.field-1])*args.multiplier)  
            #This can further be enhanced to set locale based on input buy adding one more command line arguement 
            #using .encode() to encode the string:
            results[i][args.field-1] = format_decimal(results[i][args.field-1], locale='sv_SE').encode('utf-8')
#4. Write to CSV file with proper currency value
with open(args.outputfile,'w') as f:
    for sublist in results:
        f.write(', '.join(sublist))
        f.write('\n')
#print .decode('utf8')+for'\xe2\x82\xac'mat_decimal(float(results[1][1][0])*.8, locale='sv_SE')
 


 