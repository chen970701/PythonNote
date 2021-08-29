# a=eval(input("输入一个整数\n"))
# if a>60 and a<100:
#     print("及格了")
# elif a<60:
#     print("不及格")


# for a in range(0,10,2):
#     print(a)

# try:
#     a=eval(input("请输入一个数字"))
# except:
#     print("except") 


##循环如果正常走完 就会进入else 当中间过程被阻拦就不会进入else
# for a in range(0,20,2):
#     print(a)
#     if a==10:
#         break
# else:
#     print("程序正常走完")

# for a in range(0,20,2):
#     print(a)
#     if a==20:
#         break
# else:
#     print("程序正常走完")
print(eval("23.2"))
while(True):
    str=input("输入:\n")
    if str.isalnum():
        print("所有字符都是数字或字母")
    if str.isdigit():
        print("所有字符都是数字")
    if str.isalpha():
        print("所有字符都是字母")
    if str.isspace():
        print("所有字符都是空白字符") # \t、\n、\r
    if str.isdecimal():
        print("decimal")

        
