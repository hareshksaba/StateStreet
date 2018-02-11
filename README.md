# Python CSV Parser Project without using built in csv module

#This application uses commandline arguements to perform conversion. Input file, Output file, Field, Multiplier are the arguements. 


usage: currency_convert.py [-h] [--field N FIELD] [--multiplier N MULTIPLIER]
                           [-i inputfile INPUTFILE] [-o outputfile OUTPUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  --field N FIELD       Convert CSV field N
  --multiplier N MULTIPLIER
                        Multiply currency value by N for the current
                        conversion rate
  -i inputfile INPUTFILE
                        Read from input file (or stdin)
  -o outputfile OUTPUTFILE
                        Write to output file (or stdout)

#To Run Use the below command
python currency_convert.py --field 2 --multiplier 0.8 -i data.csv -o data-fr2.csv 

