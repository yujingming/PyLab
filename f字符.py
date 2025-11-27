#占位符f
name = 'yu jingming'
print(f'hi, {name}')
print(f'my name is {name}, \nit\'s cool right?')
#占位符表达式
print (f'answer1 is {10/2}')
val = 10
print(f'answer2 is {val+12}')#不会改变val的值
#格式说明符{占位符:格式说明符}
#.nf
#以结算工资为例演示
hours = float(input('how many hours have you worked this cirle'))
salary = 20*hours
print(f'congratulations! you got {salary*(1-0.05):.1f} after pay your tax')
#，千位分隔符
#以加油站加油收费为例
volume = float(input('减去免费赠送的5L油后客人加了多少?'))
fee = volume*15.8
print(f'本次加油共收费{fee:,.2f}元，请选择你的支付方式')#四舍五入与分隔符同时使用时，分隔符在前
#%
#以成绩与平均成绩的比例为例
score = float(input('your grade this time in math'))
rate = score/80
print(f'this {rate:.1%} is the difference between you and the whole class,\nif its higher than 1 which means you are not bad')
#指定最小域宽
#显示两列数字
num1 = 123.456 
num2 = 234.567
num3 = 345.678
num4 = 456.789
num5 = 567.890
num6 = 678.901
print(f'{num1:10.2f}{num2:10.2f}')
print(f'{num3:10.2f}{num4:10.2f}')
print(f'{num5:10.2f}{num6:10.2f}')
#居中对齐
name1 = 'howard'
name2 = 'frank'
name3 = 'jimy'
print(f'****{name1:^20}****')
print(f'****{name2:^20}****')
print(f'****{name3:^20}****')
#连接f字符串
name4 = 'sam'
department = "marketing"
position = 'supervisor'
print(f'姓名{name4:^30},'
      f'部门{department:^30}',
      f'职位{position:^30}')#连接的每一个f字符串都应该有f前缀
