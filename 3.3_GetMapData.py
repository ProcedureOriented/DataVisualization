#第一组关键词检索
provinces=['河北','山西','江苏','浙江','安徽','福建','江西','河南','湖北','湖南','海南','陕西','甘肃','青海','北京','天津','上海','新疆','宁夏','西藏','云南','辽宁','吉林','山东','广东','广西','贵州','黑龙江','内蒙古','山东','重庆','四川']
keys=['武汉','疫情','战疫','钟南山','医院','口罩','肺炎']
collect=[]
for province in provinces:
    sum1,sum2=0,0
    dizhi='媒体\\'+province+'.txt'
    with open (dizhi,'r',encoding='utf-8') as f:
        content=f.readlines()
        for i in content:
            sum1+=1
            for j in keys:
                result=i.find(j)
                if result==-1:
                    pass
                else:
                    sum2+=1
                    break
    scale=int(sum2/(sum1/3)*100)
    collect.append((province,scale))
print(collect)



#第二组关键词检索
provinces=['河北','山西','江苏','浙江','安徽','福建','江西','河南','湖北','湖南','海南','陕西','甘肃','青海','北京','天津','上海','新疆','宁夏','西藏','云南','辽宁','吉林','山东','广东','广西','贵州','黑龙江','内蒙古','山东','重庆','四川']
keys=['上班','办公室','复工','复产','工作']
collect=[]
for province in provinces:
    sum1,sum2=0,0
    dizhi='媒体\\'+province+'.txt'
    with open (dizhi,'r',encoding='utf-8') as f:
        content=f.readlines()
        for i in content:
            sum1+=1
            for j in keys:
                result=i.find(j)
                if result==-1:
                    pass
                else:
                    sum2+=1
                    break
    scale=int(sum2/(sum1/3)*100)
    collect.append((province,scale))
print(collect)




#第三组关键词检索
provinces=['河北','山西','江苏','浙江','安徽','福建','江西','河南','湖北','湖南','海南','陕西','甘肃','青海','北京','天津','上海','新疆','宁夏','西藏','云南','辽宁','吉林','山东','广东','广西','贵州','黑龙江','内蒙古','山东','重庆','四川']
keys=['开学','返校','复学']
collect=[]
for province in provinces:
    sum1,sum2=0,0
    dizhi='媒体\\'+province+'.txt'
    with open (dizhi,'r',encoding='utf-8') as f:
        content=f.readlines()
        for i in content:
            sum1+=1
            for j in keys:
                result=i.find(j)
                if result==-1:
                    pass
                else:
                    sum2+=1
                    break
    scale=int(sum2/(sum1/3)*100)
    collect.append((province,scale))
print(collect)




#省份关键词检索
import os
dirs='个人'
mylist=os.listdir(dirs)
provinces=['河北','山西','江苏','浙江','安徽','福建','江西','河南','湖北','湖南','海南','陕西','甘肃','青海','北京','天津','上海','新疆','宁夏','西藏','云南','辽宁','吉林','山东','广东','广西','贵州','黑龙江','内蒙古','重庆','四川']
collect=[]
for province in provinces:
    sum1,sum2=0,0
    for uid in mylist:
        with open ('个人\\'+uid,'r',encoding='utf-8') as f:
            content=f.readlines()
            for i in content:
                if i=='\n':
                    sum1+=1
                else:
                    result1=i.find(province)
                    if result1==-1:
                        pass
                    else:
                        sum2+=1
                        break
    collect.append((province,sum2/sum1*100000))
print(collect)




#湖北省各市关键词检索
import os
dirs='个人'
mylist=os.listdir(dirs)
cities=['武汉','黄石','十堰','宜昌','襄阳','鄂州','荆门','孝感','荆州','黄冈','咸宁','随州','恩施','神农架','潜江','天门','仙桃','随州']
collect=[]
for city in cities:
    sum1,sum2=0,0
    for uid in mylist:
        with open ('个人\\'+uid,'r',encoding='utf-8') as f:
            content=f.readlines()
            for i in content:
                if i=='\n':
                    sum1+=1
                else:
                    result1=i.find(city)
                    if result1==-1:
                        pass
                    else:
                        sum2+=1
                        break
    collect.append((city,sum2/sum1*100000))
print(collect)





#全国各地积极关键词检索
provinces=['河北','山西','江苏','浙江','安徽','福建','江西','河南','湖北','湖南','海南','陕西','甘肃','青海','北京','天津','上海','新疆','宁夏','西藏','云南','辽宁','吉林','山东','广东','广西','贵州','黑龙江','内蒙古','山东','重庆','四川']
positivekeys=['积极','努力','赢','红火','恢复','胜','有望','一定','终于','认真','行动','加油','致敬','坚持','分享']
collect=[]
for province in provinces:
    sum1,sum2=0,0
    dizhi='媒体\\'+province+'.txt'
    with open (dizhi,'r',encoding='utf-8') as f:
        content=f.readlines()
        for i in content:
            sum1+=1
            for key in positivekeys:
                result=i.find(key)
                if result==-1:
                    pass
                else:
                    sum2+=1
                    break
    scale=int(sum2/(sum1/3)*100)
    collect.append((province,scale))
print(collect)




#全国各地消极关键词检索
provinces=['河北','山西','江苏','浙江','安徽','福建','江西','河南','湖北','湖南','海南','陕西','甘肃','青海','北京','天津','上海','新疆','宁夏','西藏','云南','辽宁','吉林','山东','广东','广西','贵州','黑龙江','内蒙古','山东','重庆','四川']
negativekeys=['发热','紧张','危','急','冲击','骚动','无望','不幸','不能','不要','不会','何时','熬夜','不吃']             
collect=[]
for province in provinces:
    sum1,sum2=0,0
    dizhi='媒体\\'+province+'.txt'
    with open (dizhi,'r',encoding='utf-8') as f:
        content=f.readlines()
        for i in content:
            sum1+=1
            for key in negativekeys:
                result=i.find(key)
                if result==-1:
                    pass
                else:
                    sum2+=1
                    break
    scale=int(sum2/(sum1/3)*100)
    collect.append((province,scale))
print(collect)




#全国各地情绪关键词检索及总情绪度计算
provinces=['河北','山西','江苏','浙江','安徽','福建','江西','河南','湖北','湖南','海南','陕西','甘肃','青海','北京','天津','上海','新疆','宁夏','西藏','云南','辽宁','吉林','山东','广东','广西','贵州','黑龙江','内蒙古','山东','重庆','四川']
positivekeys=['积极','努力','赢','红火','恢复','胜','有望','一定','终于','认真','行动','加油','致敬','坚持','分享']
negativekeys=['发热','紧张','危','急','冲击','骚动','无望','不幸','不能','不要','不会','何时','熬夜','不吃']             
collect=[]
collect1=[]
collect2=[]
for province in provinces:
    sum1,sum2=0,0
    dizhi='媒体\\'+province+'.txt'
    with open (dizhi,'r',encoding='utf-8') as f:
        content=f.readlines()
        for i in content:
            sum1+=1
            for key in positivekeys:
                result=i.find(key)
                if result==-1:
                    pass
                else:
                    sum2+=1
                    break
    scale=int(sum2/(sum1/3)*100)
    collect1.append((province,scale))
for province in provinces:
    sum1,sum2=0,0
    dizhi='媒体\\'+province+'.txt'
    with open (dizhi,'r',encoding='utf-8') as f:
        content=f.readlines()
        for i in content:
            sum1+=1
            for key in negativekeys:
                result=i.find(key)
                if result==-1:
                    pass
                else:
                    sum2+=1
                    break
    scale=int(sum2/(sum1/3)*100)
    collect2.append((province,scale))
for i in range(len(collect1)):
    collect.append((collect1[i][0],collect1[i][1]-collect2[i][1]))
print(collect)
