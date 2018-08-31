import  csv,sys
filename = 'msft.csv'
data = []
try:
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        data = [row for row in reader]
except csv.Error as e:
    print('Error reading csv file at line %s'%e)
    sys.exit(-1)

if header:
    print(header)
    print('========')
for datarow in data:
    print(datarow)


print('----------------------------')
import numpy
data = numpy.loadtxt('msft.csv',dtype='string',delimiter=',')
print(data)
