#用求余操作符%换算单位,以最小单位开始从高到低
total_seconds =float(input('tell me how many seconds you want to translate?: '))
hours = total_seconds//3600
minutes = (total_seconds//60)%60
seconds = total_seconds%60
print ('hours:', hours, 'minutes:', minutes, 'seconds: ', seconds)
#长度单位，cm,m,km
total_cm = float(input('tell me the length and i will sum it to you'))
km = total_cm//100000
m = (total_cm//100)%1000
cm = total_cm%100
print('here it is :', km , 'km', m, 'm', cm, 'cm')
