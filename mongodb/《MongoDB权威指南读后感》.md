《MongoDB权威(2)指南》读后感
===

# 原书评价

书中使用了非常非常非常多的集合（collection）——请原谅我这里用了三个非常这种不标准句子语法，只有这样才能表达出我愤怒的心情。作者使用的集合有：analytics， blog，blog.posts，books，coll，foo，games，lists ，mail.list，movies，papers，people，test，testcol，users，。使用多个集合本质上是没有问题的，作者的不合理之处在于：
有些文档（如：mail.list）只使用了一次，如 `db.mailing.list.remove({"opt-out" : true})` ，显得非常的没头没尾，散乱。
有些文档在使用之前也不知道内容具体是什么，如 `db.papers.update({"authors cited" : {"$ne" : "Richie"}},{$push : {"authors cited" : "Richie"}})`，集合在 update 之前都没有创建，如果按照书上的操作，可能就得不到和书上一样的结果，这无形中增加了读者学习的难度。所以读者还得先自己创建 papers 集合，而之前的集合也可以用，为什么非得创建一个只使用一次的集合，而不是直接使用之前的集合呢？显得多此一举。

# 翻译评价

## 问题

1、一些专业属于没有保留英文。

例如“2.6.1基本数据类型 ”一节中，基础数据类型都没有保留英文，这会给读者的理解造成困难，同时也不方便读者去官方文档检索相关的内容——例如数据类型“对象id”，这样解释起来就很生硬，但是如果在后面保留了英文，对象id(ObjectId)，读者就知道了这是什么。

2、 翻译错误1：

3.3.2 节第 5 点——“将数组作为数据集使用”翻译错误。原书的表述是“Using arrays as sets. You might want to treat an array as a set, only adding values if they are not present.” 根据原文的意思，只有值不存在的时候才将值添加到数组中去，这明显是指集合的“唯一性”，所以应该翻译成“将数组作为集合使用”。

3、翻译错误2：

3.3.2 节第 3 点——“数组修改器”翻译错误。原书的表述是“Array operators”，要么翻译为“运算符”，要么翻译为“操作符”，不知道为什么自创的翻译呢？难道以前的翻译已经不足以表达现在的意思了？这样会增加沟通的难度。

