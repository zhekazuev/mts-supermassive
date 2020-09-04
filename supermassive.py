"""
Original author: Dmitry Sokolov (dsokolov)
Modifications: Eugene Zuev (zhekazuev@gmail.com)
"""
from threading import Thread
import paramiko
import config
import time


class SSH:
    def __init__(self, host, user, password, port=22):
        self.client = None
        self.conn = None
        self.host = host
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        """Open ssh connection."""
        if self.conn is None:
            try:
                self.client = paramiko.SSHClient()
                self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.client.connect(hostname=self.host, port=self.port, username=self.user, password=self.password)
                return self.client
            except paramiko.AuthenticationException as authException:
                print(f"{authException}, please verify your credentials")
            except paramiko.SSHException as sshException:
                print(f"Could not establish SSH connection: {sshException}")

    def shell(self, cmd, pause=5, buffer=1000):
        """"""
        with self.connect().invoke_shell() as shell:
            shell.send(cmd)
            time.sleep(pause)
            output = shell.recv(buffer).decode('utf8')
            return output

    def execute_commands(self, cmd):
        """
        Execute command in succession.

        :param cmd: One command for example: show administrators
        :type cmd: str
        """
        stdin, stdout, stderr = self.client.exec_command(cmd)
        stdout.channel.recv_exit_status()
        response = stdout.readlines()
        return response

    def put(self, localpath, remotepath):
        sftp = self.client.open_sftp()
        sftp.put(localpath, remotepath)
        time.sleep(10)
        sftp.close()
        self.client.close()

    def get(self, remotepath, localpath):
        sftp = self.client.open_sftp()
        sftp.get(remotepath, localpath)
        time.sleep(10)
        sftp.close()
        self.client.close()

    def disconnect(self):
        """Close ssh connection."""
        if self.client:
            self.client.close()


def command_send(device, command, personal_id, personal_command):
    user = config.user
    password = config.password
    ssh = SSH(host=device.get('host'), user=user, password=password)
    if personal_id == 1:
        for line in personal_command:
            output = ssh.shell(f"{line}\n", pause=2)
            delimiter = ("*" * 80)
            info = f"Info from {device.get('hostname')}"
            message = '\n'.join(output.split('\n')[3:])
            text = f"{delimiter}\n{info}\n{message}"
            print(text)
    else:
        output = ssh.shell(f"{command}\n", pause=2)
        delimiter = ("*" * 80)
        info = f"Info from {device.get('hostname')}"
        message = '\n'.join(output.split('\n')[3:])
        text = f"{delimiter}\n{info}\n{message}"
        print(text)
    ssh.disconnect()


class Sender(Thread):
    pass


def procedure(devices, command, personal_id, personal_command):
    threads = []
    for device in devices:
        thread = Thread(target=command_send, args=(device, command, personal_id, personal_command))
        thread.setDaemon(True)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


def main():
    all_hosts = config.all_hosts
    asr5000 = config.asr5000
    asr5700 = config.asr5700
    vpcsi = config.vpcsi
    ultram = config.ultram
    apngw = config.apngw
    command_list = config.command_list

    for i, command in zip(range(1, len(command_list)+1), command_list):
        print(i, command, sep=". ")
    print(f'{len(command_list)+1}. Other commands\n')

    command_number = int(input('Choose the command number: '))

    print('''Please choose a platform for receiving commands
    1. ASR5000
    2. ASR5700
    3. VPC-SI
    4. Ultra-M
    5. APN-GW
    6. Any platform''')

    personal_command = ''
    platform_number = int(input('Choose the variant number: '))

    if command_number == len(command_list) + 1:
        personal_command = input('Enter command. Please for separating new lines use "+": ').split('+')
        personal_id = 1
        command_number = 0
    else:
        personal_id = 0
        command_number -= 1

    if platform_number == 1:
        procedure(asr5000, command_list[command_number], personal_id, personal_command)
    elif platform_number == 2:
        procedure(asr5700, command_list[command_number], personal_id, personal_command)
    elif platform_number == 3:
        procedure(vpcsi, command_list[command_number], personal_id, personal_command)
    elif platform_number == 4:
        procedure(ultram, command_list[command_number], personal_id, personal_command)
    elif platform_number == 5:
        procedure(apngw, command_list[command_number], personal_id, personal_command)
    elif platform_number == 6:
        procedure(all_hosts, command_list[command_number], personal_id, personal_command)
    elif platform_number == 0:
        print('Procedure was failed. Please check you input data and retry again.')
    else:
        print('Procedure was failed. Please check you input data and retry again.')


if __name__ == '__main__':
    main()
