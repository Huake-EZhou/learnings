# 匿名函数

python中使用即lambda表达式字来创建匿名函数。lambda表达式来源于λ演算(lambda calculus)。

## 1、函数定义

```
lambda [parameters]: expression
```

说明：

（1）参数是可选的。

（2）expression不能缺。如果缺了，会提示 `SyntaxError: invalid syntax`。

等价于：

```
def <lambda>(parameters):
	return expression
```

## 2、函数调用

匿名函数也是一种函数，既然是函数，也是使用一对圆括号调用的。

```
>>> true = lambda : True
>>> true
<function <lambda> at 0x000001C74B929F70>
>>> true()
True
```

等价于：

```
>>> def true():
...     return True
...
>>> true
<function true at 0x000001EBF82C9F70>
>>> true()
True
```

## 3、带参数的匿名函数

匿名函数写法：

```
lambda x, y: x + y
```

等价于：

```
def my_sum(x, y):
    return x + y
```

# 参考资料

[1]Python官网教程,lambda-expressions: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

[2]Python官网语言参考，Lambdas: https://docs.python.org/3/reference/expressions.html#lambda

[3]wikipedia, lambda calculus:https://en.m.wikipedia.org/wiki/Lambda_calculus#Anonymous_functions