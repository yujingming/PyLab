#2编程练习
#1.个人资料
print('here will show someone\'s breif informations: ')
name = input ('may i call you?: ')
print('ok,mr/mrs: ',name)
address =input('填写你的地址，包含省/州、市和ZIP')
print(address)
phone_number= input('电话号码：')
print (phone_number)
undergraduated_major= input ('本科专业：')
print (undergraduated_major)
#2.根据销售额求利润
print ('our company\'s profit is 23% of the total sumption')
total_sum = float(input('your company\'s whole income: '))
profit = total_sum*0.23
print ('here is the pure income: ',profit)
#3.土地计算
total_land = float(input('一共有多少平方英尺土地？： '))
ym_land = total_land/43560
print (ym_land,'英亩')
#4.购买总量
price = float(input('please tell me the price of the product:'))#重复多次
tax = price*0.07
addtax_price = price+tax
print(price,tax,addtax_price)
#9.温度转换
C=float(input('现在的摄氏度是多少: '))
F=9*C/5+32
print(F)
#10.配方
num = int(input('how many cookies you want?: '))
sugar = num*1.5/48
butter = num*1/48
mianfen = num*2.75/48
print(f'if you want {num:.1f} cookies you need {sugar:.1f} cups sugars、\n{butter:.1f} cups butters and {mianfen:.1f}cups 面粉') 