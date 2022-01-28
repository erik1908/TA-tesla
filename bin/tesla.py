import sys
sys.path.append('/usr/local/lib/python3.8/site-packages')

import json
import teslapy
from teslapy import Tesla, Vehicle, Battery, SolarPanel

import webview

def custom_auth(url):
    result = ['']
    window = webview.create_window('Login', url)
    def on_loaded():
        result[0] = window.get_current_url()
        if 'void/callback' in result[0].split('?')[0]:
            window.destroy()
    window.loaded += on_loaded
    webview.start()
    return result[0]

with teslapy.Tesla('erik.grasman@umbrio.com', authenticator=custom_auth) as tesla:
    tesla.fetch_token()
    vehicles = tesla.vehicle_list()
    print(vehicles)
#    print(vehicles[0].get_vehicle_data()['vehicle_state']['car_version'])

    
'''
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
'''