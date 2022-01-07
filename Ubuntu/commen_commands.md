# 服务器间的文件传输
scp -r bst_nbeats202107_09_10min_10min_10min_6 ends@10.232.0.37:/home/ends/Documents/zmy/
# 服务器文件在Dockerhub中创建镜像
sudo docker login -u 520521523 docker.io

sudo docker build -t 520521523/villa_eap_2d . 

sudo docker push 520521523/villa_eap_2d
# 文件压缩
tar -zcvf load-forecast-products.tar.gz /home/jovyan/load-forecast-product
# 文件解压
tar -zxvf load-forecast-products.tar.gz /home/jovyan/load-forecast-product/

# 命令行下载文件(以下载anaconda为例)
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2021.11-Linux-x86_64.sh

# ubuntu下报错AttributeError: module 'graphviz.backend' has no attribute 'ENCODING'
方法：更graphviz版本为0.16

pip install graphviz==0.16

# vscode第一次链接github操作

1、电脑本地新建一个文件夹用于clone对应github项目

2、vscode打开本地新建文件夹

3、vscode左下角添加github账号

4、clone对应github文件到本地

5、pull操作

6、线下更新代码

7、commit、push操作
# vscode 每次重新打开后连接github同步问题
1、执行pull

2、线下更新代码

3、执行commit

4、执行push