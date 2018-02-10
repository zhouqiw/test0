# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: test.py
@time: 2018/2/10 下午9:16
"""

from paramiko_client  import paramikoClient
import  threading
import  time

lock = threading.Lock()
num = 0

def upload_func(localpath,targetpath,file):
    global num
    lock.acquire()
    num = num + 1
    lock.release()

    client = paramikoClient('config.ini')
    client.conect()
    sftp_client = client.get_sftg_client()
    sftp_client.put(localpath+file,targetpath+file)
    print('upload finished')



def download_func(localpath,targetpath,file):
    global num
    lock.acquire()
    num = num + 1
    lock.release()
    client = paramikoClient('config.ini')
    client.conect()
    sftp_client = client.get_sftg_client()
    sftp_client.get(targetpath+file,localpath+file)
    print('download finished')







if __name__ == '__main__':
    begin = time.time()
    a_path = '/Users/zhouqi/Desktop/g/paramiko/'
    b_path = '/Users/zhouqi/Desktop/c/'
    upload_thread = threading.Thread(target=upload_func, args=(a_path,b_path,'2.py',))
    download_thread = threading.Thread(target=download_func,args=(a_path,b_path,'34.py',))
    upload_thread.start()
    upload_thread.join()
    download_thread.start()
    download_thread.join()
    print(num)
    print(time.time()-begin)