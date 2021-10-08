from urllib.request import urlretrieve
link = input('Enter Download Link : ')
fileName=input('Enter File Name :')

urlretrieve(link,'image/'+fileName+'.jpg')
