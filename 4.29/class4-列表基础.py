a_list=[1,20,30,1,1,1,1]#列表
print(a_list)
print(a_list[2])#打印第二个元素，从左往右，开头为0
print(a_list[-5])#打印倒数第五个元素，从右往左，开头为-1
print(a_list[1:4])#打印1-4这几个元素
print(a_list[:-2])#从头开始打印到倒数第二个元素
print(a_list[-3:])#从倒数第三个元素到结束
for i in a_list:
    print(i)
t=len(a_list)#计算列表长度
print(t)

q=a_list.index(30)#计算元素位置在哪
print(q)

a=a_list.count(1)#计算某个元素有多少个
print(a)

a_list.sort()#对列表排序
print(a_list)

a_list.sort(reverse=True)#倒排序
print(a_list)