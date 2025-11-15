import requests
code = "sh600001"
url = f"https://qt.gtimg.cn/q=s_{code}"
text = requests.get(url).text
print("原始文本:", text)
parts = text.split("~")
print("parts的实际内容:", parts)
print("分段后:", parts)
if len(parts) >=4:
    price = parts[3]
    print("提取的价格:",price)
    with open("stock.csv", "w") as f:
        f.write(f"{code},{price}\n")
    print(f" 已保存 {code} 价格 {price}到stock.csv")
else:
    print("数据格式异常,无法提取价格")
