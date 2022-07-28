import sys
#def xiugaiwenjian(input1):
zqj11 = ['ad','asd','asda']


data_dir_list = sys.argv
data_dir_list.pop(0)
for i in data_dir_list:
    zqj11[2] = i
    f_gf = open('groundfilter.sh','w')
    for j in zqj11:
        f_gf.writelines(j+'\n')
    f_gf.close
        

#for i in data_dir_list:
   # print(i)
