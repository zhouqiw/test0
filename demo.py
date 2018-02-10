# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: demo.py
@time: 2018/1/28 下午2:10
"""

from paramiko_client import paramikoClient
import time


client = paramikoClient('config.ini')
# client.conect()
sftp_client = client.get_sftg_client()


#2
def put_callback(size1,size2):
    print(size1,size2)
    # client.run_cmd('df')


def ftp_put(basic_path,target_path,file,func):

    sftp_client.put(basic_path+file,target_path+file,func)


def ftp_get(basic_path,target_path,file,func):
    sftp_client.get(basic_path + file, target_path + file, func)

# sftp_client.put('/Users/zhouqi/Desktop/g/paramiko/config.ini','/Users/zhouqi/Desktop/c/config.ini',put_callback)


a_path ='/Users/zhouqi/Desktop/g/paramiko/'
b_path ='/Users/zhouqi/Desktop/c/'



# ftp_put(a_path,b_path,'demo.py',put_callback)

# ftp_get(b_path,a_path,'3.py',put_callback)

#1
# begin = time.time()
# query_num = 100
# query_frequency = 0.2
#
# while query_num > 0:
#     now = time.time()
#     if now - begin > query_frequency:
#
#         client.run_cmd('date')
#         begin       =     now
#         query_num   =     query_num - 1





# wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocksR.sh && chmod +x shadowsocksR.sh
#
# wget -N --no-check-certificate https://raw.githubusercontent.com/FunctionClub/YankeeBBR/master/bbr.sh && bash bbr.sh install
#
#
#
# Congratulations, ShadowsocksR server install completed!
# Your Server IP        :  104.199.235.185
# Your Server Port      :  456
# Your Password         :  z12345678
# Your Protocol         :  origin
# Your obfs             :  plain
# Your Encryption Method:  aes-256-cfb
# Welcome to visit:https://shadowsocks.be/9.html
# Enjoy it!