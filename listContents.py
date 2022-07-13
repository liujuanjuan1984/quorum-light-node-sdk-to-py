import os
import json
import urllib.parse

groupId = '8136923b-8203-4e08-bfe7-50eb3b558e2c'
cmd = 'node listContents.js {0}'.format(groupId)
nodejs = os.popen(cmd)
m = nodejs.read()
nodejs.close()
print(m)