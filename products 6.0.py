import os

products = []
def read_file(filename):
	if os.path.isfile(filename):
	print('yeah!找到檔案了')
	with open (filename,'r',encoding='utf-8') as f:          
    for line in f:
    	if '商品，價格' in line:
    		continue
    	name,price = line.strip().split(',')
    	product.append([name,price])
    print(products)
    else:
	print('找不到檔案')
	return products

#讓使用者輸入
def user_input(products):
	while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	p = [name,price]
	products.append(p)
	print(products)
	return products

＃印出所有購買紀錄
def print_products(products):
	for p in products:
	print(p[0],'的價格是',p[1])

＃寫入檔案
def write_file(filename, products):
    with open(filename,'w',encoding='utf-8') as f: #使用編碼才可以正確地寫入中文字（要不然是亂碼）
	f.write('欄位,價格/n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

products = read_file('product.csv')
products = user_input(products)
print_products(products)
write_file('product.csv',products)