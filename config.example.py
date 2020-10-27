import os


class StarOS:
    user = 'user'
    password = 'pass'
    # user = os.environ["SCRIPTS_USER"]
    # password = os.environ["SCRIPTS_PASS"]

    all_hosts = [{"hostname": "host1", "host": "1.1.1.1"},
                 {"hostname": "host2", "host": "1.1.1.2"}]

    asr5000 = [{"hostname": "host1", "host": "1.1.1.1"},
               {"hostname": "host2", "host": "1.1.1.2"}]

    asr5700 = [{"hostname": "host1", "host": "1.1.1.1"},
               {"hostname": "host2", "host": "1.1.1.2"}]

    vpcsi = [{"hostname": "host1", "host": "1.1.1.1"},
             {"hostname": "host2", "host": "1.1.1.2"}]

    ultram = [{"hostname": "host1", "host": "1.1.1.1"},
              {"hostname": "host2", "host": "1.1.1.2"}]

    apngw = [{"hostname": "host1", "host": "1.1.1.1"},
             {"hostname": "host2", "host": "1.1.1.2"}]

    command_list = ["show cpu table",
                    "show card table",
                    "show port utilization table",
                    "show license information full",
                    "show version",
                    "show subscribers ggsn-only data-rate",
                    "show subscribers sgw-only data-rate",
                    "show subscribers data-rate",
                    "show resources session",
                    "show session disconnect-reasons",
                    "show task resources | grep -v good",
                    "show version",
                    "show service all",
                    "show subscribers summary rulebase EMERGENCY",
                    "show subscribers summary rulebase REMERGENCY"]
