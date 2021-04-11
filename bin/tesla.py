import sys
sys.path.append('/usr/local/lib/python3.8/site-packages')

import teslajson
import json

c = teslajson.Connection('YOUREMAIL', 'YOURPASSWORD')
v = c.vehicles[0]
v.wake_up()
i = v.data_request('charge_state')
j = v.data_request('drive_state')
k = v.data_request('climate_state')
l = v.data_request('gui_settings')
m = v.data_request('vehicle_state')
q = v.data_request('vehicle_config')
i = json.dumps(i)
j = json.dumps(j)
k = json.dumps(k)
l = json.dumps(l)
m = json.dumps(m)
q = json.dumps(q)

print("{ \"charger_state\":" + i + ",\"drive_state\":" + j + ",\"climate_state\":" + k + ",\"gui_settings\":" + l + ",\"vehicle_state\":" + m + ",\"vehicle_config\":" + q + "}")