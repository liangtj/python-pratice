import requests
import multiprocessing
import json
import MySQLdb

cnx = MySQLdb.connect(host='10.198.30.113', user='root', port=3306, db='monitor')

cursor = cnx.cursor()
# tb_host tb_buffer_host tb_ip_information
cursor.execute("select * from tb_host limit 1 ")
value = cursor.fetchall()
print(value)

# payload = {
#     'nSysId': 1923423432,
#     'sProposer': 'wadehe',
#     'sDomain': 'abc.fortest.qq.com.',
#     'ip': [
#         '183.232.17.46',
#         '101.226.103.106',
#         '183.60.69.222'
#     ]
# }

# headers = {
#     'Content-Type': 'application/json; charset=utf-8',
#     # 'Accept-Charset': 'UTF-8'
# }

# r = requests.post('http://10.171.101.44:80/cgi-bin/gslb4/get_fault_ip', data=json.dumps(payload), headers=headers)
# print(r.status_code)
# print(r.text)

# payload = {
#   "nSysId": 1923423432, 
#   "sComment": "test", 
#   "sProposer": "wadehe", 
#   "sBusiness": "gslb ", 
#   "nType": 1, 
#   "fault_ip": [
#     "101.226.103.106", 
#     "183.60.69.222", 
#     "112.90.8.115"
#   ]
# }

# headers = {
#     'Content-Type': 'application/json; charset=utf-8',
#     # 'Accept-Charset': 'UTF-8'
# }

# r = requests.post('http://10.171.101.44:80/cgi-bin/gslb4/set_fault_ip', data=json.dumps(payload), headers=headers)
# print(r.status_code)
# print(r.text)