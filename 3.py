import urllib.request as getUrl
import re
solution = ""
comment=0
with getUrl.urlopen("http://www.pythonchallenge.com/pc/def/equality.html") as response:
    page = response.read()
    # page is in binary file and should be translated to ascii
    page = page.decode('ascii')
    #print(page)
    for i in range(0,len(page)-2):
        #print(page[i] + page[i + 1] + page[i + 2])
        if page[i]+page[i+1]+page[i+2] == '<!-':
            comment+=1
        if comment >0:
           solution +=page[i]

tmp =  (re.findall('[^A-Z][A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]',solution))
solution=""
for signs in tmp:
    solution+=signs[4]
print("http://www.pythonchallenge.com/pc/def/%s.html"%solution)
