products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	p = [name,price]
	products.append(p)
print(products)

for p in products:
	print(p[0],'的價格是',p[1])

with open('product.csv','w',encoding='utf-8') as f: #使用編碼才可以正確地寫入中文字（要不然是亂碼）
	f.write('欄位,價格/n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')