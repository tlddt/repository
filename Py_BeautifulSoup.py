import requests
from bs4 import BeautifulSoup
import time
import re
import os

tempfile = "temp.html"
novelfile = "novel.txt"

urldir = "https://www.wenku8.net/novel/3/3057/"
urlfilelist = ["154787.htm","154788.htm","154832.htm","154833.htm","154872.htm",
               "155041.htm","155042.htm","155086.htm","155089.htm","155189.htm",
               "155190.htm","155191.htm","155192.htm","155193.htm","155194.htm"]
               

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

#生成 html 中繼檔

for x in urlfilelist:

    with open(tempfile,"wb+") as tfile: 
        furl = urldir+x  
        raw = requests.get(furl,headers=header,stream=True)
        
        #raw.encoding = 'ISO-8859-1'
        for chuk in raw.iter_content(chunk_size=1024):
            if chuk:
                tfile.write(chuk)

    print("url readed : {furl}")
    #time.sleep(3)   #延遲get下一個URL

    with open(tempfile,'rb') as tfile:
        content = tfile.read()
        #print(str(content,encoding="ISO-8859-1"))

        soup = BeautifulSoup(content,'html.parser')

        titles = soup.find_all('div',id="title")
        rawdatas = soup.find_all('div',id="content")

        print("tempHTML readed")

        #生成 text 文字檔
        with open(novelfile,"a",encoding="utf-8") as txtfile:

            for title in titles:
                txtfile.write(title.text)
                txtfile.write("\n")

                for data in rawdatas:
                    #if txt.find("wenku8") == -1:
                    txtfile.write(data.text)
                txtfile.write("\n")

            print("text file writed")
        print("text file closed")

    os.remove(tempfile)

    print("delay 3s")
    time.sleep(3)

print("completeled")