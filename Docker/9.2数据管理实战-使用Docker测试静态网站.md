# 说明

1、该实例为《The Docker Book》第5章内容，这里只是用于演示，部分修改。

# 创建Dockerfile

## 1、windows

```
D:\>mkdir sample
D:\>cd sample
D:\sample>type nul>Dockerfile
```

## 2、linux

```
root@iZwz94kwqu5mk9oxpv2m2tZ:/home/dockerproject# mkdir sample
root@iZwz94kwqu5mk9oxpv2m2tZ:/home/dockerproject# cd sample
root@iZwz94kwqu5mk9oxpv2m2tZ:/home/dockerproject/sample# touch Dockerfile
```

# 编写Dockerfile

windows系统可以使用Notepad之类的工具进行编写，Linux系统使用vim进行操作。Dockerfile具体内容如下：

```
FROM ubuntu:18.04
LABEL maintainer="test"
ENV refreshed_at 2020-04-09

RUN apt-get -qq update && apt-get -qq install nginx

RUN mkdir -p /var/www/html/website
ADD nginx/nginx.conf /etc/nginx/sites-enabled

EXPOSE 83
```

# 创建Nginx配置文件

## 1、windows

```
D:\sample>mkdir nginx  && cd nginx
D:\sample\nginx>touch nginx.conf
```

## 2、linux

```
root@iZwz94kwqu5mk9oxpv2m2tZ:/home/dockerproject/sample# mkdir nginx && cd nginx
root@iZwz94kwqu5mk9oxpv2m2tZ:/home/dockerproject/sample/nginx# touch nginx.conf
```

# 编写Nginx配置文件

windows系统可以使用Notepad之类的工具进行编写，Linux系统使用vim进行操作。nginx.conf内容如下：

```
user www-data;
worker_processes 4;
pid /run/nginx.pid;
daemon off;

server {
  listen 0.0.0.0:83;
  server_name _;

  root /var/www/html/website;
  index  index.html index.htm;
  
  access_log      /var/log/sweeneys/sample/access.log;
  error_log      /var/log/sweeneys/sample/error.log;
}
```

说明：
（1）_含义：

# 构建新的Nginx镜像

## 1、windows

```
D:\sample>docker build -t sweeneys/nginx .
Sending build context to Docker daemon  3.584kB
Step 1/7 : FROM ubuntu:18.04
 ---> 4e5021d210f6
Step 2/7 : LABEL maintainer="test"
 ---> Using cache
 ---> ac2edafd3dc8
Step 3/7 : ENV refreshed_at 2020-04-09
 ---> Using cache
 ---> a61b46d30c96
Step 4/7 : RUN apt-get -qq update && apt-get -qq install nginx
 ---> Using cache
 ---> b854ec714aa8
Step 5/7 : RUN mkdir -p /var/www/html/website
 ---> Using cache
 ---> 5526f67aef88
Step 6/7 : ADD nginx/nginx.conf /etc/nginx/sites-enabled
 ---> Using cache
 ---> 775196dbc84b
Step 7/7 : EXPOSE 83
 ---> Using cache
 ---> 780f0c1dc62d
Successfully built 780f0c1dc62d
Successfully tagged sweeneys/nginx:latest
SECURITY WARNING: You are building a Docker image from Windows against a non-Windows Docker host. All files and directories added to build context will have '-rwxr-xr-x' permissions. It is recommended to double check and reset permissions for sensitive files and directories.
```

说明：

（1）sweeneys: 我自己的registry，你需要替换成你自己的。

（2）nginx: 镜像名(image name)。

（3）.：注意这个点不要漏，表示当前目录（即构建上下文）。

（4）如上所示，每一个指令都会生成一个镜像，后面的指令基于前面生成的镜像进行操作。最终的镜像ID为780f0c1dc62d。

（5）如果要查看某个镜像的构建步骤和层级，可以使用 `history`命令。从最后一层开始，追溯到基础镜像。

```
D:\sample>docker history 780f0c1dc62d
IMAGE         CREATED          CREATED BY                     SIZE  COMMENT
780f0c1dc62d  15 minutes ago   /bin/sh -c #(nop)  EXPOSE 83   0B
775196dbc84b  15 minutes ago   /bin/sh -c #(nop) ADD...       287B
...
```

## 2、linux

```
root@iZwz94kwqu5mk9oxpv2m2tZ:/home/dockerproject/sample# docker build -t sweeneys/nginx .
```

# index.html

上面的步骤已经完成镜像创建，那么接下来的操作就是基于该镜像构建一个容器。先创建一个index.html文件。

## 1、创建

（1）windows

```
D:\sample>mkdir website && cd website
D:\sample\website>type nul>index.html
```

（2）linux

```
root@iZwz94kwqu5mk9oxpv2m2tZ:/home/dockerproject/sample# mkdir website && cd website
root@iZwz94kwqu5mk9oxpv2m2tZ:/home/dockerproject/sample/website# touch index.html
```

## 2、编写

windows系统可以使用Notepad之类的工具进行编写，Linux系统使用vim进行操作。index.html内容如下：

```
<head>
  <title>Test website</title>
</head>
<body>
  <h1>This is a test website</h1>
</body>
```

# 构建容器

## 1、windows

```

```



## 2、linux

（1）写法一：使用--mount标志（推荐）

```
docker run -d -p 83 --name website --mount type=bind,source="$(pwd)"/website,\
> target=/var/www/html/website sweeneys/nginx nginx
```

# 参考资料

[1]James Turnbull, 《The Docker Book》:https://github.com/turnbullpress/dockerbook-code

[2]James Turnbull, github:https://github.com/turnbullpress/dockerbook-code