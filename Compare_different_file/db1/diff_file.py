import difflib,sys

try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception as e:
    print('Error:'+str(e))
    print('Usage:diff_file.py textfile1 textfile2')
    sys.exit()

def readfile(filename):
    try:
        filehandle = open(filename,'rb')
        text = filehandle.read().splitlines()
        # print('text')
        filehandle.close()
        return str(text)
    except IOError as error:
        print('read file error:'+str(error))
        sys.exit()

if textfile1 == '' or textfile2 == '':
    print('usage:diff_file.py filename1 filename2')
    sys.exit()

text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)



d = difflib.HtmlDiff()
# print(d.make_file(text1_lines,text2_lines))
print(d.make_file(text1_lines,text2_lines))