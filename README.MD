# Supermassive

Executing Bulk Commands on Multiple StarOS Nodes

  - Choosing a command option
  - Choosing platforms
  - Specifying the waiting time between commands
  - If you chose User Commands - enter your commands through the "+"

### Installation

Git clone from repo
```sh
git clone https://github.com/Zhekazuev/Supermassive.git supermassive
```

Install the dependencies from requirements.txt. 
```sh
cd supermassive
cat requirements.txt
source install.sh
```

Start script
```sh
python supermassive.py
```

Example:
```console
[root@server1 supermassive]# source env/bin/activate
(env) [root@server1 supermassive]# python supermassive.py
1. show cpu table
2. show card table
3. show port utilization table
4. show license information full
5. show version
6. show subscribers ggsn-only data-rate
7. show subscribers sgw-only data-rate
8. show subscribers data-rate
9. show resources session
10. show session disconnect-reasons
11. show task resources | grep -v good
12. show version
13. show service all
14. show subscribers summary rulebase EMERGENCY
15. show subscribers summary rulebase REMERGENCY
16. User commands

Choose the command number: 1
Please choose a platform for receiving commands
    1. ASR5000
    2. ASR5700
    3. VPC-SI
    4. Ultra-M
    5. APN-GW
    6. Any platform
Choose the variant number: 2
Enter the waiting time(default 1 second): 1
10-28-2020 12:26:07 | INFO:
INPUT: 1.1.1.1: ['show card table\n']
OUTPUT:
 show card table
...
10-28-2020 12:26:07 | INFO:
INPUT: 1.1.1.15: ['show card table\n']
OUTPUT:
...
--- 1.8922240734100342 seconds ---
(env) [root@server1 supermassive]# deactivate
[root@server1 supermassive]#
```


License
----
Free Software