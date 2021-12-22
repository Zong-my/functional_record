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

