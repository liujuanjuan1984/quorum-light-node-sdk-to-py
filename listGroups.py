import os
import json
import urllib.parse

cmd = 'node listGroups.js'
nodejs = os.popen(cmd)
m = nodejs.read()
nodejs.close()
print(m)