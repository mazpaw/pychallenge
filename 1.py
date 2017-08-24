# http://www.pythonchallenge.com/pc/def/map.html

tmp = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#solution 1 naive one

#chr print sign beneath asci number
#ord print asci number of given sign
print ord('z')
print ord('a')

for i in tmp:
    if i.isalpha():
        #print chr(ord(i)+2), this cause problem with a and b
        a=ord(i)+2
        if a>122:
            a-=26
        print chr(a),
    else:
        print i,
print "\n"

map = "map"

for i in map:
    if i.isalpha():
        #print chr(ord(i)+2), this cause problem with a and b
        a=ord(i)+2
        if a>122:
            a-=26
        print chr(a),
    else:
        print i,
print "\n"

# solution 2 better one
import string
tab1=string.ascii_lowercase

print tab1[2::]
#slices [start:stop:step]
tab2=tab1[2::]+tab1[0:2]
print tab2

translateTab = string.maketrans(tab1,tab2)
print tmp.translate(translateTab)
print "map".translate(translateTab)

# www.pythonchallenge.com/pc/def/ocr.html