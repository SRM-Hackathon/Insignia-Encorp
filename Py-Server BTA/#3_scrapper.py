import re
import urllib.request
from bs4 import BeautifulSoup
 
html = urllib.request.urlopen('https://www.amazon.in/ZORO-Mens-Genuine-Leather-Guarantee/dp/B07N5D89F1/ref=bbp_bb_d33a38_st_nGy5_w_0?psc=1&smid=A1I6F6168CKCC7')
soup = BeautifulSoup(html)
data = soup.findAll(text=True)
 
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True
 
result = filter(visible, data)

list1=list(result)
list1=[s.pop('\n')for s in list1]
 
print (list1)

#images=[]
#images=soup.findAll('img')
#for image in images:
    #print(image.get('src'))
#html1 = urllib.request.urlopen('https://www.medicalnewstoday.com/articles/324711.php')
#soup1 = BeautifulSoup(html1)
#data1 = soup.findAll(text=True)

 
#result1 = filter(visible, data1)
 
#print (list(result1))
