# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: demo.py
@time: 2018/1/24 下午9:44
"""
import paramiko
import configparser



class paramikoClient:
    def __init__(self,config_str):

        self.config = configparser.ConfigParser()
        self.config.read(config_str)
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sftp_client = None
        self.client_state = 0

    def conect(self):
        try:
            self.client.connect(hostname = self.config.get('ssh','host'),
                                port     = self.config.getint('ssh','port'),
                                username = self.config.get('ssh','username'),
                                password = self.config.get('ssh','password'),
                                timeout  = self.config.getfloat('ssh','timeout'))
        # for i in range(5):

            client_state = 1

        except Exception as e:
            print(e)

            try:
                print('clonsed')
                self.client.close()
                client_state = 0
            except:
                pass


    def run_cmd(self,cmd_str):
        # print('->')

        stdin, stdout, stderr = self.client.exec_command(cmd_str)

        for i in stdout:
            print(i)

    def get_sftg_client(self):
        if self.client_state == 0:
            self.conect()
        if not self.sftp_client:
            self.sftp_client = paramiko.SFTPClient.from_transport(self.client.get_transport())

        return  self.sftp_client


# print('ok')

if __name__ == '__main__':


    client = paramikoClient('config.ini')
    client.conect()
    client.run_cmd('pwd')
    client.run_cmd('echo hello shell')
