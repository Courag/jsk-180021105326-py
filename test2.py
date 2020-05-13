string="Hello"
num=123456.789
print("你好对应的英文是：{:20}".format(string))
print("你好对应的英文是：{:>20}".format(string))
print("你好对应的英文是：{:^20}".format(string))
print("你好对应的英文是：{:*^20}".format(string))
print("你好对应的英文是：{:2}".format(string))
print("你好对应的英文是：{:.2}".format(string))

print("数字对应显示是：{:.2f}".format(num))
print("数字对应显示是：{:,}".format(num))
print("数字对应显示是：{:@^20,.1f}".format(num))
print("数字对应显示是：{:,.2f}".format(num))

print("数字的百分制显示是：{:%}".format(num))
print("数字的百分制显示是：{:.2%}".format(num))
print("数字的百分制显示是：{:e}".format(num))

num=123456
print("数字的二进制显示是：{:b}".format(num))
print("数字的十进制显示是：{:d}".format(num))
print("数字的八进制显示是：{:o}".format(num))
print("数字的十六进制大写显示是：{:X}".format(num))
print("数字的十六进制小写显示是：{:x}".format(num))


