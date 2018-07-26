import fnmatch
import os
import tarfile
import datetime

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


def main():
    patterns = ['*.txt','*.html']
    now = datetime.datetime.now().strftime("%Y_%m_%d")
    filename = "all_text_{0}.tar.gz".format(now)
    with tarfile.open(filename,'w:gz') as f:
        for item in find_specific_files('.',patterns):
            f.add(item)



if __name__ == '__main__':
    main()
