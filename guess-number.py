#猜數字1~100
#判別大小並提示比答案大或小
#猜對就停止
 #使用者可自訂範圍
import random
count = 0
start = input('請輸入開始值: ')
end = input('請輸入結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
while True:
	count += 1 #快速寫法，count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了!! ')
		print('這是你猜的第', count , '次')
		break
	elif num > r:
		print('再小一點 ')
	elif num < r:
		print('再大一點 ')
	print('這是你猜的第', count , '次')