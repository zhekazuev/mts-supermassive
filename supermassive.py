"""
Original author: Dmitry Sokolov (dsokolov)
Modifications: Eugene Zuev (zhekazuev@gmail.com)
"""
import paramiko
import config
import time


all_names = config.all_names
all_ips = config.all_ips

asr5000_names = config.asr5000_names
asr5000_ips = config.asr5000_ips

asr5700_names = config.asr5700_names
asr5700_ips = config.asr5700_ips

vpcsi_names = config.vpcsi_names
vpcsi_ips = config.vpcsi_ips

ultram_names = config.ultram_names
ultram_ips = config.apn_gw_ips

apn_gw_names = config.apn_gw_names
apn_gw_ips = config.apn_gw_ips

command_list = config.command_list


user = config.user
password = config.password


def command_send(ip, name, command, personal_id, personal_command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=22, username=user, password=password)
    print('Info from ' + name + ':\n')
    chan = ssh.invoke_shell()
    if personal_id == 1:
        for line in personal_command:
            chan.send(line + '\n')
            time.sleep(2)
    else:
        chan.send(command + '\n')
        time.sleep(2)
    output = chan.recv(100000).decode("utf-8")
    print('\n'.join(output.split('\n')[3:]) + '\n' + '*' * 80)
    ssh.close()


def procedure(device_ips, device_names, command, personal_id, personal_command):
    for ip, name in zip(device_ips, device_names):
        command_send(ip, name, command, personal_id, personal_command)


for i, command in zip(range(0,15), command_list):
    print(i, command)
print('20. Other commands\n')

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

if command_number == 20:
    personal_command = input('Enter command. Please for separating new lines use "+": ').split('+')
    personal_id = 1
    command_number = 0
else:
    personal_id = 0

if platform_number == 1:
    procedure(asr5000_ips, asr5000_names, command_list[command_number], personal_id, personal_command)
elif platform_number == 2:
    procedure(asr5700_ips, asr5700_names, command_list[command_number], personal_id, personal_command)
elif platform_number == 3:
    procedure(vpcsi_ips, vpcsi_names, command_list[command_number], personal_id, personal_command)
elif platform_number == 4:
    procedure(ultram_ips, ultram_names, command_list[command_number], personal_id, personal_command)
elif platform_number == 5:
    procedure(apn_gw_ips, apn_gw_names, command_list[command_number], personal_id, personal_command)
elif platform_number == 6:
    procedure(all_ips, all_names, command_list[command_number], personal_id, personal_command)
else:
    print('Procedure was failed. Please check you input data and retry again.')
