#coding=utf-8
import filecmp
a="/tmp/dir1" #定义左目录
b="/tmp/dir2" #定义右目录
dirobj=filecmp.dircmp(a, b, ['test.py']) #目录比较，忽略test.py文件
#输出对比结果数据报表，详细说明请参考filecmp类方法及属性信息
dirobj.report()
dirobj.report_partial_closure()
dirobj.report_full_closure()
print "left_list："+ str(dirobj.left_list)
print "right_list："+ str(dirobj.right_list)
print "common："+ str(dirobj.common)
print "left_only："+ str(dirobj.left_only)
print "right_only："+ str(dirobj.right_only)
print "common_dirs："+ str(dirobj.common_dirs)
print "common_files："+ str(dirobj.common_files)
print "common_funny："+ str(dirobj.common_funny)
print "same_file："+ str(dirobj.same_files)
print "diff_files："+ str(dirobj.diff_files)
print "funny_files："+ str(dirobj.funny_files)
