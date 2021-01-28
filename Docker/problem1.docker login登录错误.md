# 一、环境说明
1、ubuntu:  18.04.2 LTS

2、docker: 19.03.5, build 633a0ea838

# 二、问题描述

使用 `docker login`命令登录 Docker Hub时报错。

```
$ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: sweeneys
Password: 
Error saving credentials: error storing credentials - err: exit status 1, out: `Failed to execute child process “dbus-launch” (No such file or directory)
```

# 三、解决方法

参考：https://github.com/docker/cli/issues/1136

```
$ sudo apt-get install gnupg2 pass
```

说明：

1、[gnupg2](https://launchpad.net/ubuntu/+source/gnupg2): 一种包含数字签名和证书的加密工具。

2、[pass](http://manpages.ubuntu.com/manpages/trusty/man1/pass.1.html): 一种简单的密码管理工具。



