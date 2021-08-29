# a={1,1,3,"3"}
# print(a)
# print(type(a))

# print(type("str")==str)

# a={1,3,5,7,9}
# b={3,5,8,10}
# print(a&b,a|b,a-b,a^b)  #交集 并集 在a不在b的  a和b特有的
# a.remove(1)
# print(a)
# a.add(11)
# print(a)
# a.clear()
# print(a)

# a="知之为知之，不知为不知"
# print(set(a))

# a=[1,3,4,5,2,1]
# print(max(a))
# print(a[0:4:2])
# print(a+[3,4])#列表拼接


# a=[1,3,5,7,9,11,0,"hh"]
# a.append("green")
# print(a)
# a.pop(0)#不传则删除最后一个
# print(a)
# a.remove(5)#删除指定元素
# print(a)
# del(a[0:2]) #使用del关键字删除长度的列表
# print(a)
# a=a+[1,1,1]
# print(a) 
# print(a.count(1)) #输出1的位置

a={"01":"green","02":"mika","03":"Aaron"}
print(type(a.keys()))
ls=tuple(a.keys())
print(ls)
lsv=tuple(a.values())
for v in lsv:
    print(v)
print(list( a.items()))
print(a.get("01","没有人名"),a.get("04","没有该人名"))#get的第二个参数是查询不到键之后返回的值
print(a.pop("02","无法找到"),a.pop("05","无法找到"),a)
print("{:-<10}green".format("aaaa")) 