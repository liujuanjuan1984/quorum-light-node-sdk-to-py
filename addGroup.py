import os
import json
import urllib.parse

seedUrl = urllib.parse.quote("rum://seed?v=1&e=0&n=0&b=Ptpg6HKIRIaTnVw_f3SKvg&c=wPOoSSDCxbk7owipIwJ4nKmRyyN2wRsW1I_vsxZm1dI&g=gTaSO4IDTgi_51DrO1WOLA&k=Aqa6ngNxgrVhf2kQc4nA-0Wr4tsWiaBrshZJPujT5B9g&s=GDLJ-TcXuo95q-CsUFty7pvMIYZRFRQ3VwrparvjKy00wIYSmx5pl4xT4ALb6AVgNei_is5kn1MuXfh9b5wB-QE&t=Fv89llMDYIA&a=%E8%81%8A%E5%A4%A9%E5%AE%A45&y=group_timeline&u=http://103.61.39.166:9003")
nodeToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhbGxvd0dyb3VwcyI6W10sImV4cCI6MTY1OTcwNDI2NCwibmFtZSI6Im5vZGUtYWxsLWdyb3VwcyIsInJvbGUiOiJjaGFpbiJ9.mHeMhunwDGmjnB7PhoKqVrUZI7QbfaGxOPgH2o4WUQo'
cmd = 'node addGroup.js {0} {1}'.format(seedUrl, nodeToken)
nodejs = os.popen(cmd)
m = nodejs.read()
nodejs.close()
print(m)