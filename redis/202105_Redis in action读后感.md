Redis in action读后感
===

# 问题

## 1、举例无意义

`rpush list-key item`

使用 rpush 命令时，key 的名称是 `list-key`，元素的名称是 `item`，这样做没有问题，但是对于读者来说，`list-key` 和  `item`是抽象的内容，是不方便记忆的。举例的时候，最好使用以下两种方法，一种直接使用官方文档的例子，方便检索；另一种是使用与读者相关联的内容，方便理解与记忆。

示例：`rpush fruit apple `

向 fruit 列表插入一个名为 apple 的元素。

