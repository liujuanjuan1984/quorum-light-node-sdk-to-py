import os
import json
import urllib.parse

groupId = '8136923b-8203-4e08-bfe7-50eb3b558e2c'
trxId = '981a7295-8442-4eef-bbb5-af83cb65b19b'
cmd = 'node getTrx.js {0} {1}'.format(groupId, trxId)
nodejs = os.popen(cmd)
m = nodejs.read()
nodejs.close()
print(m)