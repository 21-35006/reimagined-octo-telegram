import re
f = open('テストデータ.txt', 'r', encoding='UTF-8')
datalist=f.readlines()
f.close()
i=1
count=0
subnetlist=['空値']
subI=0
N=int(input('故障とみなす回数Nを入力して下さい。:'))
f = open('テストデータ.txt', 'r', encoding='UTF-8')
while True:
  data = f.readline()
  subnet = re.search(r',(.+?),',data).group()
  if data == '' and len(subnetlist)==subI:
    break
  if data == '':
    continue
  if data[-2]=='-':
    if subnet not in subnetlist :
      subnetlist.append(subnet)
    count+=1
    if count>=N and subnetlist[subI]==subnet:
      print (data[15:-6])
      sec=int(datalist[i][0:14])-int(data[0:14])
      if sec>=10000:
        hour=sec//10000
        sec=sec%10000+hour*60*100
      if sec>99:
        min=sec//100
        sec=sec%100+60*min
      print(sec)

  i+=1
  subI+=1
f.close()