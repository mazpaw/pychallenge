# http://www.pythonchallenge.com/pc/def/map.html

tmp = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#solution 1 first attempt

#chr print sign beneath asci number
#ord print asci number of given sign
print (ord('z'))
print (ord('a'))

for i in tmp:
    if i.isalpha():
        #print chr(ord(i)+2), this cause problem with a and b
        a=ord(i)+2
        if a>122:
            a-=26
            print (chr(a))
        else:
            print (i)

map = "map"

for i in map:
    if i.isalpha():
        #print chr(ord(i)+2), this cause problem with a and b
        a=ord(i)+2
        if a>122:
            a-=26
        print (chr(a))
    else:
        print (i),
print ("\n")

# solution 2 better one
import string
arr1=string.ascii_lowercase

#slices [start:stop:step]
arr2=arr1[2::]+arr1[0:2]
arr3={}
for i in range(0,len(arr1)):
    arr3[arr1[i]]=arr2[i]

translateTab = arr1.maketrans(arr3)
print (tmp.translate(translateTab))


print('http://www.pythonchallenge.com/pc/def/%s.html'%(map.translate(translateTab)))