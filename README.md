# bishe
环境配置
-----
环境ubuntu16.04 <br>
python3.6 、 Django1.8.2<br>
安装python3后<br>
安装虚拟环境参考博客(https://blog.csdn.net/da953824/article/details/87946504)<br>
下面博客的内容：<br>
安装虚拟环境(须在联网状态下)<br>
$ sudo pip install virtualenv<br>
$ sudo pip install virtualenvwrapper<br>
安装完虚拟环境后，如果提示找不到mkvirtualenv命令，须配置环境变量：

1、创建目录用来存放虚拟环境<br>
mkdir $HOME/.virtualenvs 

2、打开~/.bashrc文件，并添加如下：<br>
export WORKON_HOME=$HOME/.virtualenvs <br>
source /usr/local/bin/virtualenvwrapper.sh

3、运行<br>
source ~/.bashrc

4 创建虚拟环境(ubuntu里须在联网状态下)<br>
$ mkvirtualenv django_py3 -p python3<br>
进入虚拟环境

$ workon django_py3
进入项目目录  req.txt所在目录<br>
安装相应python包
pip install -r req.txt
如果自己安装python包，版本请一致，因为有些PY包会导致django版本的变动
然后将项目目录中的ChineseAnalyzer.py和whoosh_cn_backend.py复制到/home/python/.virtualenvs/bjll_py3/lib/python3.5/site-packages/haystack/backends，<br>前面/home/python/是家目录，.virtualenvs包含所有你创建的虚拟环境，然后一直往下就是你安装haystack的目录，<br>你需要加这两个文件，才能支持中文分词搜素，runserver时才不会出现没有whoosh_cn_backend.py的错误
## 数据库安装
### mysql
安装服务端 <br>
sudo apt-get install mysql-server <br>
安装客户端 <br>
sudo apt-get install mysql-client <br>
安装libmysqlclient，这个在使用开发工具连接数据库使用会用到 <br>
sudo apt-get install libmysqlclient-dev<br>
### redis
Ubuntu上直接sudo apt-get install redis-server <br>
ps -aux|grep redis<br>
让redis服务器可远程登陆，修改redis配置文件，sudo vim /etc/redis/redis.conf<br>
将bind 127.0.0.1注释掉<br>
这里我没注释，因为我的redis并没有远程连接的需求
重启redis服务
sudo /etc/init.d/redis-server restart<br>
如果过段时间服务器报错，可能是服务器内存小，也可能是你的redis内存被别人的程序利用的情况，<br> 如果是第一种可以通过设置配置文件的maxmemory参数设置最大占用内存大小,默认是不设的，然后设置maxmemory-policy删除策略为 allkeys-lru最近最少使用的删除，以避免redis内存不足导致网站报错。<br>
如果是第二种要不设置密码，要不将redis的绑定ip为本地ip<br>
## 测试
在manage.py所在目录下
输入python manage.py runserver 8085
如果看到下面信息，表示正确
February 26, 2019 - 14:14:52
Django version 1.8.2, using settings 'dailyfruit.settings'
Starting development server at http://127.0.0.1:8085/
Quit the server with CONTROL-C
在浏览器上输入123.0.0.1:8085/index 你就会看到主页。<br>
选择注册跳转到注册页面，填入相关信息，去邮箱检查有没激活邮件，点击账号激活，跳转登录页面，输入账号密码就能登录了
## fastdfs与nginx安装

参考这个博客https://blog.csdn.net/MissEel/article/details/80856194
## 
## 服务器部署--uwsgi与nginx
uwsgi.ini和uwsgi2.ini文件,一般改三个socket=127.0.0.1:8000,第二uwsgi的端口要跟第一个不一样。用于与nginx进程间通信；<br>目录chdir=/home/python/你的项目，一般我会放在家目录下，<br>设置虚拟环境的路径virtualenv=/home/python/.virtualenvs/bjll_py3
<br>nginx还是参考我附在项目目录下的nginx.conf，有几个要注意的地方：1.server 80要放最前，其他server放在后面，<br>upstream里面就uwsgi对应两个socket，
正则匹配 / 就是所有url都有这个来处理，通过设置多个location来实现负载均衡。
<br>
<br>
### 最终效果请点击http://www.laizhida.cn 如果有任何问题，请联系我！
