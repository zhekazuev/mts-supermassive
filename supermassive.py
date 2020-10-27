"""
Original author: Dmitry Sokolov (dsokolov)
Modifications: Eugene Zuev (zhekazuev@gmail.com)
"""
from client import RemoteClient
from threading import Thread
import paramiko
import config
import time
import re


def command_send(device, commands, pause):
    user = config.StarOS.user
    password = config.StarOS.password
    host = device.get('host')
    commands = [command + "\n" for command in commands]

    try:
        with RemoteClient(host, user, password) as ssh:
            ssh.shell(commands, pause=pause, buffer=20000)
    except paramiko.SSHException as sshException:
        print(f'Error: {sshException}')


def procedure(devices, commands, pause=1.0):
    threads = []
    for device in devices:
        thread = Thread(target=command_send, args=(device, commands, pause))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


def main():
    all_hosts = config.StarOS.all_hosts
    asr5000 = config.StarOS.asr5000
    asr5700 = config.StarOS.asr5700
    vpcsi = config.StarOS.vpcsi
    ultram = config.StarOS.ultram
    apngw = config.StarOS.apngw
    command_list = config.StarOS.command_list

    for i, command in zip(range(1, len(command_list) + 1), command_list):
        print(i, command, sep=". ")
    print(f'{len(command_list) + 1}. User commands\n')

    command_number = int(input('Choose the command number: '))

    print('''Please choose a platform for receiving commands
    1. ASR5000
    2. ASR5700
    3. VPC-SI
    4. Ultra-M
    5. APN-GW
    6. Any platform''')

    platform_number = int(input('Choose the variant number: '))

    pause = float(input("Enter the waiting time(default 1 second): "))

    if command_number == len(command_list) + 1:
        commands = input('Enter command. Please for separating new lines use "+": ').split('+')
    else:
        commands = [command_list[command_number]]

    start_time = time.time()

    if platform_number == 1:
        procedure(asr5000, commands, pause)
    elif platform_number == 2:
        procedure(asr5700, commands, pause)
    elif platform_number == 3:
        procedure(vpcsi, commands, pause)
    elif platform_number == 4:
        procedure(ultram, commands, pause)
    elif platform_number == 5:
        procedure(apngw, commands, pause)
    elif platform_number == 6:
        procedure(all_hosts, commands, pause)
    elif platform_number == 0:
        print('Procedure was failed. Please check you input data and retry again.')
    else:
        print('Procedure was failed. Please check you input data and retry again.')

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
