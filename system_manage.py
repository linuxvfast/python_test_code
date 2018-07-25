import os
#
path = os.path.abspath(__file__)
#
# print(os.path.split(path))
# print(os.path.dirname(path))
# print(os.path.basename(path))
# print(os.path.splitext(path)[1])
#
# print(os.path.expanduser('~\mysql'))
# print(os.path.abspath('..'))
# print(os.path.join(os.path.expanduser('~'),'t','a.txt'))
# print(os.path.isabs('.'))
# print(os.path.isabs(path))
# print(os.getcwd())
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(os.path.abspath(os.path.join(os.path.dirname(path),os.path.pardir)))
# print(os.path.getsize(path))
# print(os.path.getatime(path))
# print(os.path.getmtime(path))
# print(os.path.getctime(path))
#
# print([item for item in os.listdir(os.path.expanduser('~')) if os.path.isfile(item)])
# print([item for item in os.listdir(os.path.expanduser('~')) if os.path.isdir(item)])
# print(os.path.abspath(path))
# print({item:os.path.realpath(item) for item in os.listdir(os.path.expanduser('~')) if os.path.isdir(item)})
# print({item :os.path.getsize(item) for item in os.listdir(os.path.expanduser('~')) if os.path.isfile(item)})
#
# print(os.getcwd())
# pth = os.chdir(r'C:\Users\tony')
# print(os.path.abspath(pth))

# os.path.ismount('/dev')

# os.unlink(os.path.join(os.path.dirname(os.path.abspath(__file__)),'outdata.txt'))
# os.remove('outdata.txt')
# os.rmdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'test'))
# os.removedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)),'test'))
# os.mkdir('test')
# print('ok')
# print(os.getcwd())
# os.rename(os.path.join(os.path.dirname(os.path.abspath(__file__)),'test'),'test2')
# print('OK')

# print(os.path.abspath(os.path.join(os.path.dirname(path),os.path.pardir)))
# print(os.pardir)


# import os,sys
#
# def main():
#     sys.argv.append("")
#     filename = sys.argv[1]
#     if not os.path.isfile(filename):
#         raise SystemExit(filename + ' does not exists')
#     elif not os.access(filename, os.X_OK,):
#         os.chmod(filename,777)
#     else:
#         with open(filename) as f:
#             print(f.read())
#
# if __name__ == '__main__':
#     main()


# import os
#
# from collections import Counter
#
# c = Counter()
#
# with open(os.path.expanduser('~/.bash_history')) as f:
#     for line in f:
#         cmd = line.strip().split()
#         if cmd:
#             c[cmd[0]] += 1
#
# print(c.most_common(10))


# import os
#
# print([item for item in os.listdir('.') if item.endswith('.txt')])

#匹配文件
# import os
# import fnmatch
#
# names =os.listdir('.')
# print([name for name in os.listdir('.') if fnmatch.fnmatch(name,'*.txt')])
# print(names)
# print(fnmatch.filter(names,'[a-c]?.txt'))
# print(fnmatch.filter(names,'[a-c]*.txt'))
# print(fnmatch.filter(names,'[!a-c]*.txt'))

# import glob
#
# print(glob.glob('*.txt'))
# print(glob.glob('[a-c]?.txt'))
# print(glob.glob('[a-c]*.txt'))
# print(glob.glob('[!a-c]*.txt'))


# import os
# import fnmatch
#
# images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
# matches = []
#
# for root, dirnames, filenames in os.walk(os.path.dirname(os.path.abspath(__file__))):
#     for extensions in images:
#         for filename in fnmatch.filter(filenames, extensions):
#             matches.append(os.path.join(root, filename))
#
#     for line in dirnames:
#         print(line)
#     if 'test' in dirnames:
#         dirnames.remove('test')
#
# print(matches)



import os
import fnmatch
import time

def is_file_match(filename, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False

def find_specific_files(root, patterns=['*'], exclude_dirs=[]):
    '''
    :param root: 查找的根目录
    :param patterns: 需要匹配的文件
    :param exclude_dirs: 忽略的目录
    :return:
    '''
    for root, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if is_file_match(filename, patterns):
                yield os.path.join(root, filename)

        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)

if __name__ == '__main__':
    #According to the current directory of files and directories
    # for item in find_specific_files('.'):
    #     print(item)

    #According to the current directory of the picture
    # images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
    # for item in find_specific_files('.',images,['test']):
    #     print(item)

    #According to the current directory the ten largest file and Eliminate  db1 directory
    # files = {name: os.path.getsize(name) for name in find_specific_files('.',exclude_dirs=['db1'])}
    # print(files)
    # result = sorted(files.items(),key=lambda d:d[1],reverse=True)[:10]
    # print(result)
    # for i,t in enumerate(result,1):
    #     print(i,t[0],t[1])

    #show the current directory of the old file
    # files = {name:os.path.getmtime(name) for name in find_specific_files('.')}
    # print(files)
    # result = sorted(files.items(),key=lambda d:d[1])[:10]
    # print(result)
    # for i,t in enumerate(result,1):
    #     print(i,t[0],time.ctime(t[1]))

    #show the current directory of the txt file
    # files = [name for name in find_specific_files('.',patterns=['*.txt'])]
    # for i,name in enumerate(files,1):
    #     print(i,name)

    #Similar to the above and Eliminate the jinja2 and db1 and db2 dir
    # files = [name for name in find_specific_files('.',patterns=['*.py'],exclude_dirs=['jinja2','db1','db2'])]
    # for i,name in enumerate(files,1):
    #     print(i,name)

    #remove the current directory and child directory of the png file
    files = [name for name in find_specific_files('.', patterns=['*.png'],exclude_dirs=['img'])]
    for name in files:
        os.remove(name)