# def myPrint(st:str):
#     print(st.center(20,"#"))
# myPrint("hello green")

# def add(a,b:int=10):
#     return a+b
# print(add(10,20)) 
# print(add(a=30)) #可以传参指定名称

# def multi(a,b):
#     return a+b,a*b #可以return多个值
# c,d=multi(1,2)
# print(c,d)

t=4
def double(a):
    global t  #声明全局变量 相当于在全局外部声明了t=2
    t=2
    return t*a
print(double(23),t)


k=30
def addk(t):
    k=10+t
    return(k)
print(addk(7),k)