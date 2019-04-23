#猜數字1~100
#判別大小並提示比答案大或小
#猜對就停止
import random

r = random.randint(1, 100)
while True:
	num = input('請猜數字(1-100): ')
	num = int(num)
	if num == r:
		print('你猜中了!! ')
		break
	elif num > r:
		print('再小一點 ')
	elif num < r:
		print('再大一點 ')