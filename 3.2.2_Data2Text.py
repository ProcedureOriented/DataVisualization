import os
import re
class blg:#定义博客类
    def __init__(self,mon,day,con,nam,atc,coc,rec):#月，日，内容，博主，点赞，评论，转发
        self.mon=mon
        self.day=day
        self.con=re.sub(r'<(.*?)>','',con)#去除多余内容
        self.con=self.con.replace("content：",'')
        self.nam=nam
        self.atc=atc
        self.coc=coc
        self.rec=rec
def cmpa(a,b):#自定义匹配函数，用作多个信息的同时匹配，具体在（1）处
    for i in b:
        if a.find(i)!=-1:
            return True
    return False
lis=[]
with open('data.txt','r',encoding='utf-8')as f:
    while True:
        s=f.readline()
        t=re.match(r'name:(.*)',s)#匹配博主
        if s=='0' or s=='0\n' or s=='':#匹配前文所述，表示所有数据结尾的单行0
            break
        if t:#匹配到具体博主后，开始匹配博客
            na=s.replace('name:','')#博主名称只在单一uid的搜索结果下的第一段出现一次
            #print(na)
            q=f.readline()
            while True:
                p=f.readline()
                if p=='0'or p=='0\n' or p=='' or p=='-1\n':#出现单行-1，该博主匹配结束，匹配下一博主
                    break
                if re.match(r'URL：',p):#博客以第一行URL为起始，后接第二行时间，第三行内容，第四五六行赞/评论/转发
                    t=f.readline()#时间
                    t=t.replace('created at：','')
                    tls=t.split('-')
                    if len(tls)!=2:#有两种情况会导致拆分出的不是月日两个。一是近一天内的信息，二是其他年份的信息，都不需要考虑
                        continue
                    mm=int(tls[0])
                    dd=int(tls[1])#分解为月、日
                    cont=f.readline()#内容
                    #print (cont)
                    atco=f.readline()
                    while atco.find('attitudes count：')==-1:#防止特殊情况下内容不止一行，读完内容后才能记录赞的信息
                        cont+=cont+atco
                        atco=f.readline()
                    coco=f.readline()
                    reco=f.readline()
                    aa=int(atco.replace('attitudes count：',''))
                    cc=int(coco.replace('comments count：',''))#评论
                    rr=int(reco.replace('reposts count：',''))#转发
                    bg=blg(mm,dd,cont,na,aa,cc,rr)
                    lis.append(bg)#全博文组成一个大列表
                    #print(bg.nam)#出错时确定错误位置用
        t=None
ls=[]
for i in range(1,6):
    for j in range(1,32):
        for k in lis:
            if k.mon==i:
                if k.day==j:
                    ls.append(k)#将博主为主的排列变为时间为主
with open('list.txt',encoding='utf-8')as f:
    wlst=f.readlines()#导入关键词
n=len(ls)
with open('result.txt','w',encoding='utf-8')as f:
    for i in wlst:#逐词反复匹配时间为主排列方式，博主为次排列方式的博客 列表
        f.write('关键词: %s'%i)
        j=0
        t=i.replace('\n','')
        b=t.split()
        while j<n:#按博客搜索关键词
            if cmpa(ls[j].con,b):#查到有关键词的博客，则就地开始对其发帖日的统计，这样开始可以避免输出没有相关微博的日子的统计结果。
                m=ls[j].mon
                d=ls[j].day
                f.write('日期：%d-%d\n'%(m,d))
                t1,t2,t3,t4=0,0,0,0#开始对当日博客数、点赞数、评论数、转发数的统计
                h=j#由于计数以0而非1开始，故需重新从j而非j+1开始统计
                while h<n and ls[h].mon==m and ls[h].day==d :#条件为当日
                    if cmpa(ls[h].con,b):#（1）
                        t1+=1
                        t2+=ls[h].atc
                        t3+=ls[h].coc
                        t4+=ls[h].rec
                        f.write('内容：%s博主：%s 点赞数：%d，评论数：%d，转发数：%d\n\n'%(ls[h].con,ls[h].nam,ls[h].atc,ls[h].coc,ls[h].rec))
                    h+=1
                f.write('本日共博客数：%d，点赞数：%d，评论数：%d，转发数：%d\n\n'%(t1,t2,t3,t4))
                j=h#当日统计完成后，进入下一条博客，它属于新的一天
            else:
                j=j+1#没有关键词的情况下，使while循环继续进行
print ("complete")
