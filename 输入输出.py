# a=input("输入a\n")
# b=input("输入b\n")
# c=int(a)+int(b)
# print("{}+{}={}".format(a,b,c),end="  (T.T)")

# print(0xffffff)
# a="hello green"
# print(len(a)) 

# eval会解析
# b=123456
# print(eval("b"))#会输出123456
# a=eval(input("输入b\n"))
# print(type(a))

#输出整数和余数
# print(divmod(9,2))

# print(dir("__builtins__"))
# a=1+4j
# print(dir(a))#输出里面的属性方法
# b="abcdefg"
# print(b[1:3]) #开闭尾括
# print(b[3:1:-1]) #最后一个参数是控制步长和方向

#字符串格式化
# name="green"
# record=0xfff00
# grade=0.97426
# # 填充的符号 <左对齐 >右对齐 ^居中对齐 字符串长度 ,千分位 .保留小数位数 d十进制
# print("{0:-<10}:他的记录是{1:,d},他拿了{2:.2}分".format(name,record,grade))

print(chr(97))
print(ord("a"))
print("abc".center(40,"&"))
a="#####hello ## green####"
b=a.strip("#")
print(b)
print(b.join("❤😔❤"))