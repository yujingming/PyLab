#狮虎比例
num_lion = int(input('how many lions do we have in this zoo?: '))
num_tiger = int(input('how many tigers do we have in this zoo?: '))
num_all = num_lion+num_tiger
print(f'老虎占比{num_tiger/num_all:.2%}') 
print(f'狮子占比{num_lion/num_all:.2%}')