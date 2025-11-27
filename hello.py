#已知终值求先值
future_value = float(input('how much you want in your account?: '))
year = int(input('how many years you decide to stock your money?: '))
rate = float(input("what's the interest in the bank or agency you prefer to stock?: "))
present_value = future_value/(1+rate)**year
print('here you are: ', present_value)

