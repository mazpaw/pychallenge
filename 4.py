import urllib.request

def getPage(httpAddress):
    with urllib.request.urlopen(httpAddress) as response:
        page = response.read()
        # page is in binary file and should be translated to ascii
        page = page.decode('ascii')
        return page

def readNumber(page):
    splited = page.split(' ')
    for section in splited:
        if section.isdigit():
            return section
            break
    return page

x = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
number = '0'
last = '0'
while number.isdigit() or number == 'Yes. Divide by two and keep going.' :
    last = number
    number = readNumber(getPage(x))
    if 'html' in number:
        print ('http://www.pythonchallenge.com/pc/def/'+number)
        break
    if not number.isdigit():
        last = int(last)/2
        number =('%.0f' % last)
    x='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'%number
