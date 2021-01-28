data structure: set
---------------------------

# 定义

1、数学上的set^[1]^: In mathematics, a set is a group of objects with stated characteristics。 翻译过来就是一组具有明确特征的对象。Python语言里面的set也是对应数学上的集合，数学中的集合具有三个性质：确定性，互异性，无序性。

2、Python里set^[2]^: A set is an unordered collection with no duplicate elements。没有重复元素的无序集合。从Python的定义中我们也可以看到集合数据类型set是完全符合数学中集合的三个性质的。

# 数据结构

在Python语言中，集合类型set是基于散列表（哈希表）技术实现的数据结构，采用内消解技术解决冲突。

# 操作

集合set所支持的全部操作详见Python标准库参考：https://docs.python.org/3.9/library/stdtypes.html#set

## 创建

创建可以使用花括号{}或者set()函数进行创建。从{}表示方法我们可以联想到数据结构字典dict，因为这两种数据结构的实现都使用了散列表技术。

```
# 创建
basket = {'apple','orange'}
# 创建空集合
basket = set()
```

## 运算

set支持数学上的并集、交集、差集、对称差集运算。

```
# 并集

# 交集

# 差集

# 对称差集
```



## 时间复杂度

| 操作 | 平均时间复杂度 | 说明 |
| ---- | -------------- | ---- |
| in   |                | a    |
|      |                |      |
|      |                |      |

a. 因为集合的实现技术是散列表，查找的查找的平均时间复杂度是O(1)。

# 参考资料

[1] Cambridge Dictionary, set: https://dictionary.cambridge.org/us/dictionary/english/set

[2] Python, set: https://docs.python.org/3.9/tutorial/datastructures.html#sets

