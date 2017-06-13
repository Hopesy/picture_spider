#-*- coding:utf-8 -*-
import re
import requests
def dowmloadPic(html,keyword,count):
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 0
    print '找到关键词:'+keyword+'的图片，现在开始下载图片...'
    for each in pic_url:
        print '正在下载第'+str(i+1)+'张图片，图片地址:'+str(each)
        try:
            pic= requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print '【错误】当前图片无法下载'
            continue
        string = 'pictures\\'+keyword+'_'+str(i) + '.jpg'
        #resolve the problem of encode, make sure that chinese name could be store
        fp = open(string.decode('utf-8').encode('cp936'),'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
        if str(i) == str(count):
            print '下载完毕'
            return




if __name__ == '__main__':
    word = raw_input("Input key word: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
    count_picture=raw_input('Input picture count of download：')
    result = requests.get(url)
    dowmloadPic(result.text,word,count_picture)

