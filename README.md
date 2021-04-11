# TA-Tesla
This TA uses teslajson to retrieve the following data from your car into your Splunk
- Charger State
- Climate State
- Drive State
- GUI Settings
- Vehicle configuration
- Vehicle state

Feel free to contact me if you got any questions about this TA

### Dependencies
- install teslajson use pip via the command :pip install teslajson
- check where teslajson module is installed (in this example in, /usr/local/lib/python3.8/site-packages)
- edit tesla.py in the bin directory with
  - location of teslajson module (line 2)
  - email address and password (line 7)


### Screenies
Data:
![Scr. Shot 1](/static/data2.png?raw=true "Data types")
![Scr. Shot 1](/static/data1.png?raw=true "Charging data")
Dashboards:
![Scr. Shot 1](/static/screen1.png?raw=true "Dashboard")
![Scr. Shot 1](/static/screen2.png?raw=true "Dashboard")