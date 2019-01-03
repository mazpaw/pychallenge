import urllib.request
import pickle


with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p') as data:
    data=data.read()
    arr= pickle.loads(data)
    for line in arr:
        for element in line:
            print(element[0]*element[1], end="")
        print(end="\n")

#channel
#http://www.pythonchallenge.com/pc/def/channel.html