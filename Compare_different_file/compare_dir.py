import os,sys
import filecmp
import re
import shutil
difflist = []

def compareme(dir1,dir2):
    '''need to backup counts source file'''
    dircomp = filecmp.dircmp(dir1,dir2)
    only_in_one = dircomp.left_only     #source file on left
    diff_in_one = dircomp.diff_files    #not match file
    # dirpath = os.path.abspath(dir1) #define source dir path

    #将更新文件名或者目录加到difflist
    [difflist.append(os.path.abspath(os.path.join(dir1,x))) for x in only_in_one]
    [difflist.append(os.path.abspath(os.path.join(dir1,x))) for x in diff_in_one]

    if len(dircomp.common_dirs) > 0: #判断是否有相同的子目录
        for item in dircomp.common_dirs: #递归子目录
            compareme(os.path.abspath(os.path.join(dir1,item)),os.path.abspath(os.path.join(dir2,item)))
        return difflist

def main():
    if len(sys.argv) > 2:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    else:
        print('Usage:',sys.argv[0],'source_dir backup_dir')
        sys.exit()

    source_files = compareme(dir1,dir2)
    dir1 = os.path.abspath(dir1)

    if not dir2.endswith('/'):
        dir2 = dir2+'/'
    dir2 = os.path.abspath(dir2)
    destiantion_files = []
    createdir_bool = False

    for item in source_files:
        '''遍历需要同步的文件'''
        destiantion_dir = re.sub(dir1,dir2,item)
        destiantion_files.append(destiantion_dir)
        if os.path.isdir(item):
            if not os.path.exists(destiantion_dir):
                os.makedirs(destiantion_dir)
                createdir_bool = True
    #print(destiantion_files)
    if createdir_bool:
        destiantion_files =[]
        source_files = []
        source_files = compareme(dir1,dir2)
        for item in source_files:
            destiantion_dir = re.sub(dir1,dir2,item)
            destiantion_files.append(destiantion_dir)
    
    print('update item:')
    print(source_files)
    copy_pair = zip(source_files,destiantion_files) #将源目录和备份目录文件清单拆分成元组
    for item in copy_pair:
        print(item)
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0],item[1])

if __name__ == '__main__':
    main()
