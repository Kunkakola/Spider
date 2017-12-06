import re
import urllib.request

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    reg = r'src="(.*?\.jpg)"'
    img=re.compile(reg)
    html=html.decode('utf-8')#python3
    imglist=re.findall(img,html)
    x = 0
    for imgurl in imglist:
        try:{
            urllib.request.urlretrieve(imgurl,r'F:\Python\hhhhh\image\%s.jpg'%x)
        }
        except:
            pass
        x = x+1

html = getHtml("https://tieba.baidu.com/p/3910118183")
print(getImg(html))
