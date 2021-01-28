# 一、python中使用redis

# 1、安装redis-py

```
pip install redis
```

## 2、示例

```
# -*- coding:utf-8 -*-
import redis

redis = redis.Redis(host='localhost', port=6379, db=0)
redis.set('foo', 'bar')
res = redis.get('foo')
print(res)  # b'bar'
```

## 参考资料

 [1]redis-py包：https://pypi.org/project/redis/