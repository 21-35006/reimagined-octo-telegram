f = open('テストデータ.txt', 'r', encoding='UTF-8')
datalist=f.readlines()
f.close()
i=1
f = open('テストデータ.txt', 'r', encoding='UTF-8')
while True:
  data = f.readline()
 
  if data == '':
    break
  if data[-2]=='-':
    print ('サーバアドレス：',data[15:-6])
    sec=int(datalist[i][0:14])-int(data[0:14])
    if sec>9900:
      hour=sec//10000
      sec=sec+hour*60*100
    if sec>99:
      min=sec//100
      sec=sec%100+60*min
    print('故障期間：',sec)

  i+=1
f.close()