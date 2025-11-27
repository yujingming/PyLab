num_stock = 2000
buyprice = 40
pay_buy = num_stock*buyprice
fee_buy = pay_buy*0.03
sell_price = 42.75
earn_sell = num_stock*sell_price
fee_sell = earn_sell*0.03
finall_income = earn_sell-pay_buy-fee_buy-fee_sell
print(f'购入股票所支付的金额：{pay_buy:.2f},支付给经纪人的佣金：{fee_buy:.2f}\n卖出股票的金额{earn_sell:.2f},支付给经纪人的佣金：{fee_sell:.2f}')
print(f'最后盈亏{finall_income:.2f}')