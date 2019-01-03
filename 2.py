import urllib.request as getUrl
solution = ""
comment=0
with getUrl.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html") as response:
    page = response.read()
    # page is in binary file and should be translated to ascii
    page = page.decode('ascii')
    #print(page)
    for i in range(0,len(page)-2):
        #print(page[i] + page[i + 1] + page[i + 2])
        if page[i]+page[i+1]+page[i+2] == '<!-':
            comment+=1
        if comment >1:
            if page[i].isalpha():
                solution+=page[i]
print("http://www.pythonchallenge.com/pc/def/%s.html"%solution)
