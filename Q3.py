f = open('テストデータ.txt', 'r', encoding='UTF-8')
datalist=f.readlines()
datalist.append("000000000000000")
f.close()
i=1
count=0
N=int(input('故障とみなす回数Nを入力して下さい。:'))
m=int(input('過負荷状態とみなす平均回数mを入力して下さい。:'))
t=int(input('過負荷状態とみなす平均応答時間tを入力して下さい。:'))
seclist=list()
f = open('テストデータ.txt', 'r', encoding='UTF-8')
while True:
  data = f.readline()
 
  if data == '':
    break
  sec=int(datalist[i][0:14])-int(data[0:14])  
  if sec>9900:
    hour=sec//10000
    sec=sec+hour*60*100
  if sec>99:
    min=sec//100
    sec=sec%100+60*min
  seclist.insert(0,sec)
  if len(seclist)>m:
    seclist.pop(-1)   
  if data[-2]=='-':
    count+=1   
    if count>=N:
      print ('サーバアドレス：',data[15:-6])
    print('故障期間：',sec)
  if (sum(seclist)/m)>=t:
    print('サーバが過負荷状態です。')
    print('過負荷状態期間',sum(seclist))
  i+=1
f.close()