# 安装

## 1、Linux系统

```
$sudo apt install wget
```

## 2、windows系统

windows系统进入到https://eternallybored.org/misc/wget/进行下载并安装（如果exe文件下载后无法安装，就下载zip文件解压，并将解压后文件所在的路径添加到系统环境变量中）。

# 使用

## 1、基本语法

```
wget [option]... [URL]...
```

示例：

```
wget https://github.com/xinhuiqin/dockerbook-code/blob/master/code/5/sample/nginx/nginx.conf
```



wget详细用法参考[官方手册](https://www.gnu.org/software/wget/manual/)。

## 2、下载说明

使用wget下载文件的时候，如果同名文件已经存在，那么wget会使用其它名字继续下载。如：已经存在nginx.conf文件，如果再次下载则命名为nginx.conf.1，nginx.conf.2，...

# 参考资料

[1] Wget:https://www.gnu.org/software/wget/

[2]Wget doc:https://www.gnu.org/software/wget/manual/

