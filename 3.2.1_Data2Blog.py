import os
dirs='个人'    #获取个人文件中各个文本名称
mylist=os.listdir(dirs)
lisst=[]
lis=[]
for uid in mylist:
    with open('个人\\'+uid,'r',encoding='utf-8') as f2:
        #print (uid)
        content=f2.readlines()
        for i in content:
            lisst.append(i)
        lisst.append('\n')
        lisst.append('-1')#每个博主的记录结尾处额外写一行-1，帮助主程序分离名称
        lisst.append('\n')
b=0#b用来统计读取的行数，
with open('data.txt','a',encoding='utf-8') as f3:
    for i in lisst:
        f3.write(i)
        b+=1
    f3.write('\n')
    f3.write('0')#总表结尾处添加单独的一行0，作为结束的标志
print(b)

