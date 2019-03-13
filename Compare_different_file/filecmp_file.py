import filecmp,sys,os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#两个文件对比
# d = filecmp.cmp(BASE_DIR+'\\'+'nginx.conf',BASE_DIR+'\\'+'nginx2.conf',shallow=False)
# print(d)

dir1 = '%s/%s'%(BASE_DIR,'db1')
dir2 = '%s/%s'%(BASE_DIR,'db2')
#多文件对比
results= filecmp.cmpfiles(dir1,dir2,['diff.html','diff_file.py','nginx.conf','nginx.conf.default','aa.txt'],shallow=False)
# print(results)


res = filecmp.dircmp(dir1,dir2,['nginx.conf'])   #方括号中的表示忽略
# res.report()  #只对比指定目录的内容对比
# res.report_partial_closure() #对比指定目录及第一级子目录的内容
res.report_full_closure()  #递归对比所有目录的内容

print('left_list:'+str(res.left_list)) #左目录列表
print('right_list:'+str(res.right_list))#右目录列表
print('common:'+str(res.common))#两个目录共同的
print('left_only:'+str(res.left_only))#仅在左目录
print('right_only:'+str(res.right_only))#仅在右目录
print('common_dirs:'+str(res.common_dirs))#两边都有的子目录
print('common_files:'+str(res.common_files))#两边都有的子文件
print('common_funny:'+str(res.common_funny)) #两个目录都存在的子目录
print('same_files:'+str(res.same_files)) #匹配相同的
print('diff_files:'+str(res.diff_files)) #不匹配的
print('funny_files:'+str(res.funny_files)) #两边都有不能比较的