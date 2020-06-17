import urllib.request
import json
import time
import random

proxy_addr='122.241.72.191:808' #设置代理相关代码
def use_proxy(url,proxy_addr):
    req=urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(req).read().decode('utf-8','ignore')
    return data

def get_containerid(url): #获取containerID
    data=use_proxy(url,proxy_addr)
    content=json.loads(data).get('data')
    for data in content.get('tabsInfo').get('tabs'):
        if data.get('tab_type')=='weibo':
            containerid=data.get('containerid')
    return containerid

def get_userInfo(uid): #获取博主的信息
    global pro_info
    url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+uid
    data=use_proxy(url,proxy_addr)
    content=json.loads(data).get('data')
    description=content.get('userInfo').get('description')
    profile_url=content.get('userInfo').get('profile_url')
    verified=content.get('userInfo').get('verified')
    follow=content.get('userInfo').get('follow_count')
    name=content.get('userInfo').get('screen_name')
    followers=content.get('userInfo').get('followers_count')
    pro_info=('name:'+name+'\n'+'profile URL：'+profile_url+'\n'+'verified status：'+str(verified)+'\n'+'description：'+description+'\n'+'follow count：'+str(follow)+'\n'+'followers count：'+str(followers)+'\n')

def get_weibo(id,file): #获取微博内容
    page,c=1,1 #页码计数
    while 1:
        url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+uid
        weibo_url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+uid+'&containerid='+get_containerid(url)+'&page='+str(page)
        try:
            data=use_proxy(weibo_url,proxy_addr)
            content=json.loads(data).get('data')
            cards=content.get('cards') #当页微博总数
            if len(cards)<=0:
                break
            else:
                for j in range(len(cards)):
                    card_type=cards[j].get('card_type')
                    if card_type==9:
                        mblog=cards[j].get('mblog')
                        attitudes_count=mblog.get('attitudes_count')
                        comments_count=mblog.get('comments_count')
                        created_at=mblog.get('created_at')
                        reposts_count=mblog.get('reposts_count')
                        scheme=cards[j].get('scheme')
                        text=mblog.get('text')
                        if text!='转发微博':
                            with open(file,'a',encoding='utf-8') as f:
                                if c:
                                    c=0
                                    f.write('uid:'+uid+'\n'+pro_info+'\n')
                                f.write('\n'+'URL：'+str(scheme)+'\n'+'created at：'+str(created_at)+'\n'+'content：'+text+'\n'+'attitudes count：'+str(attitudes_count)+'\n'+'comments count：'+str(comments_count)+'\n'+'reposts count：'+str(reposts_count)+'\n')
                page+=1
        except Exception as e:
            print(e)
            time.sleep(random.random()*6)
            break

if __name__=='__main__':
    uidfile='uidlist.txt'
    uidlist=[]
    with open(uidfile,'r') as uf:
        ls=uf.readlines()
    for i in range(len(ls)):
        s=ls[i]
        lss=s.split()
        if len(lss)>0:
            uidlist.append(lss[0])
    for uid in uidlist:
        try:
            file=uid+'.txt'
            get_userInfo(uid)
            get_weibo(uid,file)
        except Exception as e:
            continue