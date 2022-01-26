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

7、git config --global user.email "mingyang.zong@xxx.com"

8、git config --global user.name "mingyang"  

9、commit、push操作
# vscode 每次重新打开后连接github同步问题
1、执行pull

2、线下更新代码

3、执行commit

4、执行push

# 安装jupyterlab&jupyternotebook并添加kernel操作

## 1、激活目标环境（xxx）

conda activate xxx

## 2、安装jupyter notebook、jupyterlab

pip install jupyter notebook

pip install jupyterlab

## 3、查看已有kernel

ipython kernelspec list

## 4、安装ipykernel便于后续添加新kernel

pip install ipykernel

## 5、查看当前目标环境的解释器路径

命令行输入python

import sys

sys.executable

'E:\\Anaconda3-2020.02-Windows-x86_64\\envs\\py37\\python.exe'
记录下来python.exe前面的部分

exit()

## 6、将当前目标环境解释器作为新kernel添加至jupyter notebook&jupyterlab

5中的语句转换为：E:\Anaconda3-2020.02-Windows-x86_64\envs\py37\
命令行执行：

E:\Anaconda3-2020.02-Windows-x86_64\envs\py37\python -m ipykernel install --name py37（py37为环境名称，因人而异）

# pd.read_excel()报错XLRDError: Excel xlsx file; not supported

pip uninstall xlrd

pip install xlrd==1.2.0
