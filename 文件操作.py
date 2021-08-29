# from os import close


# a= open("./temp.txt","r+")
# for line in a:
#     print(line)#返回字符串
# a.close()

# b=open("./temp2.txt","w")
# k=["apple\n","banana\n","orange"] #自己加入\n
# b.writelines(k)
# b.writelines("hahaha")
# b.close()


## 存储二维数组到csv 注意要使用字符串 而不能用数字 因为join函数要求是字符串
# ls=[["id","name","age"],["001","green","24"],["002","tob","54"]]
# f=open("temp.csv","w")
# for onel in ls:
#     f.write(",".join(onel)+"\n")
# f.close()

##从csv读取内容并存储到二维数组中
f=open("temp.csv","r")
strlist=f.readlines()
lines=[]
for oneline in strlist:
    lines.append(oneline.strip("\n").split(",")) #strip可以把字符串首尾的指定字符去除
print(lines) 
f.close()