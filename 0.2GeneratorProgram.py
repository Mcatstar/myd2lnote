# 
# region知识点1：能被 for 循环遍历的对象，被称为：可迭代对象(iterable)
print('1.可迭代对象(iterable)的例子：')
names = ['张三', '李四', '王五']
citys = ('北京', '上海', '深圳')
msg = 'hello'
age = 10
def test():
    pass
try:
    for item in test:
        print(item)
except TypeError as e:
    print(e)

breakpoint()
# endregion

# 知识点2：可迭代对象(iterable) 能调用到 __iter__ 方法。
# region
print('2.可迭代对象(iterable) 调用 __iter__ 方法的例子：')
names = ['张三', '李四', '王五']
citys = ('北京', '上海', '深圳')
msg = 'hello'
age = 10
def test():
    pass

names.__iter__()
citys.__iter__()
msg.__iter__()

print(hasattr(names, '__iter__'))
print(hasattr(citys, '__iter__'))
print(hasattr(msg, '__iter__'))
print(hasattr(age, '__iter__'))
print(hasattr(test, '__iter__'))

breakpoint()
# endregion

# 知识点3：调用 __iter__ 方法会得到：迭代器(iterator)
# 备注1：__iter__ 是一个魔法方法，当调用 iter 函数时，__iter__ 会自动调用。
# 备注2：可迭代对象.__iter__()  等价于  iter(可迭代对象)。
# 备注3：如果 iter(obj) 能得到一个迭代器(iterator)，那 obj 就是可迭代对象。
# region
print('3.可迭代对象(iterable) 调用 __iter__ 方法得到 迭代器(iterator) 的例子：')
names = ['张三', '李四', '王五']
citys = ('北京', '上海', '深圳')
msg = 'hello'

print(names.__iter__())
print(citys.__iter__())
print(msg.__iter__())

print(iter(names))
print(iter(citys))
print(iter(msg))

breakpoint()
# endregion

# 知识点4：迭代器(iterator)拥有 __next__ 方法，每次调用都会根据当前的状态，返回下一个元素。
# 备注1：迭代器.__next__()  等价于  next(迭代器)。
# 备注2：当所有元素全都取出后，若继续调用 __next__ 方法，Python会抛出 StopIteration 异常。
# region
print('4.迭代器(iterator) 调用 __next__ 方法的例子：')
names = ['张三', '李四', '王五']
it = iter(names)
print(it.__next__())
print(it.__next__())
print(it.__next__())
# print(it.__next__())

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

breakpoint()
# endregion

# for循环背后的工作逻辑
print('for循环背后的工作逻辑的例子：')
# region
names = ['张三', '李四', '王五']

# 编写for循环遍历names列表
for item in names:
    print(item)

# for循环背后的逻辑
# 1调用【可迭代对象的__iter__方法】获取到一个迭代器(iterator)
# it = iter(names)
# # 2开启一个无限循环
# while True:
#     try:
#         # 调用__next__方法，获取下一个元素
#         item = next(it)
#         print(item)
#     except StopIteration:
#         # 捕获 StopIteration 异常，随后结束循环
#         break
# breakpoint()
# endregion

# 知识点5：迭代器(iterator)也拥有 __iter__ 方法，并且其返回值是迭代器自身。
# 这么设计的原因如下：让 for 循环也能遍历迭代器（即：为了让 iter(迭代器) 不出错）。
print('5.迭代器(iterator) 也拥有 __iter__ 方法，并且其返回值是迭代器自身的例子：')
# region
names = ['张三', '李四', '王五']

it = iter(names)
print(it)

result = iter(it)
print(result)

x = iter(result)
print(x)

it = iter(names)
for item in it:
    print(item)

breakpoint()
# endregion

# 知识点6：迭代器协议
#   1.能被 iter() 接受
#   2.能被 next() 一步一步取值
