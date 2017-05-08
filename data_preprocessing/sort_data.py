import sys
from collections import Counter


def sort_data_file(file_name):
    nums=[]
    for line in open(file_name):
        line=line.strip().split(' ')
        nums+=line
    c=Counter(nums)
    with open('%s.sorted'%(file_name),'w') as fout:
        for line in open(file_name):
            line=line.strip().split(' ')
            line=sorted(line, key=lambda x:c[x], reverse=True)
            line=' '.join(line)
            fout.write('%s \n'%(line))
    c=sorted(c.items(), key=lambda x:x[1], reverse=True)
    with open('%s.nums'%(file_name),'w') as fout:
        for cc in c:
            fout.write('%s %d\n'%cc)


if __name__=='__main__':
    sort_data_file(sys.argv[1])
