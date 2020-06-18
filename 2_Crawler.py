import json,time,random
from urllib import request
proxyIP='122.241.72.191:808'

def proxy(URL_1,proxyIP): #proxy IP setting
    request_URL_1=request.Request(URL_1)
    request_URL_1.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3\
    6 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    proxy_opener=request.build_opener(request.ProxyHandler({'http':proxyIP}),request.HTTPHandler)
    request.install_opener(proxy_opener)
    return request.urlopen(request_URL_1).read().decode('utf-8','ignore')

def cid(URL_2): #containerID getting
    json_2=proxy(URL_2,proxyIP)
    for json_2 in json.loads(json_2).get('data').get('tabsInfo').get('tabs'):
        if json_2.get('tab_type')=='weibo':
            cid=json_2.get('containerid')
    return cid

def infocrawler(uid): #weibo user information crawling
    global userinfo
    URL_3='https://m.weibo.cn/api/container/getIndex?type=uid&value='+uid
    json_3=proxy(URL_3,proxyIP)
    data_3=json.loads(json_3).get('data')
    name=data_3.get('userInfo').get('screen_name')
    profile_url=data_3.get('userInfo').get('profile_url')
    verified=data_3.get('userInfo').get('verified')
    description=data_3.get('userInfo').get('description')
    follow_count=data_3.get('userInfo').get('follow_count')
    followers_count=data_3.get('userInfo').get('followers_count')
    userinfo=('name:'+name+'\n'+'profile URL：'+profile_url+'\n'+'verified status：'+str(verified)+'\
    \n'+'description：'+description+'\n'+'follow count：'+str(follow_count)+'\n'+'followers count：'\
    +str(followers_count)+'\n')

def weibocrawler(product_file,uid): 
    page,bool_0=1,1 #pages counting
    while 1:
        URL_0='https://m.weibo.cn/api/container/getIndex?type=uid&value='+uid
        URL_4=URL_0+'&containerid='+cid(URL_0)+'&page='+str(page)
        try:
            json_4=proxy(URL_4,proxyIP)
            data_4=json.loads(json_4).get('data')
            cards=data_4.get('cards') #weibos counting(on present page)
            if len(cards)<=0: #if there are no weibos, break
                break
            else:
                for j in range(len(cards)):
                    card_type=cards[j].get('card_type')
                    if card_type==9:
                        scheme=cards[j].get('scheme')
                        mblog=cards[j].get('mblog')
                        created_at=mblog.get('created_at')
                        text=mblog.get('text')
                        attitudes_count=mblog.get('attitudes_count')
                        comments_count=mblog.get('comments_count')
                        reposts_count=mblog.get('reposts_count')
                        if text!='转发微博': #filter the weibos which are just reposting others
                            with open(product_file,'a',encoding='utf-8') as f:
                                if bool_0:
                                    bool_0=0
                                    f.write('uid:'+uid+'\n'+userinfo+'\n')
                                f.write('\n'+'URL：'+str(scheme)+'\n'+'created at：'+str(created_at)+'\
                                \n'+'content：'+text+'\n'+'attitudes count：'+str(attitudes_count)+'\n'\
                                +'comments count：'+str(comments_count)+'\n'+'reposts count：'+str(\
                                reposts_count)+'\n')
                page+=1
        except Exception as e:
            print(e)
            time.sleep(random.random()*5)
            break

if __name__=='__main__':
    errorcount=1 #HTTP Error 418 counting
    while errorcount<=100:
        material_file='uidlist.txt'
        uidlist=[]
        with open(material_file,'r') as uf:
            ls=uf.readlines()
        for i in range(len(ls)):
            s=ls[i]
            lss=s.split() #filter
            if len(lss)>0:
                uidlist.append(lss[0])
        for uid in uidlist:
            try:
                product_file=uid+'.txt'
                infocrawler(uid)
                weibocrawler(product_file,uid)
            except Exception as e:
                print(e,'x'+str(errorcount),sep=' ')
                errorcount+=1
                time.sleep(random.random()*5)
                continue