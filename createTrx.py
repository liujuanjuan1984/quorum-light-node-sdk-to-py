import os
import json
import urllib.parse

groupId = '8136923b-8203-4e08-bfe7-50eb3b558e2c'
data = "'{0}'".format(json.dumps({"type":"Note","content":"send from python"}, separators=(',', ':')))
privateKey = '0x8ec0b306e7e3358b7c41d46e46d389e5cfb804d45e3e1cc0b51d0f8347b2489a'
cmd = 'node createTrx.js {0} {1} {2}'.format(groupId, data, privateKey)
nodejs = os.popen(cmd)
m = nodejs.read()
nodejs.close()
print(m)