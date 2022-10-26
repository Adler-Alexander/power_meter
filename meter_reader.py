import re
import json
import requests
import time
import serial
# ############Disable HTTPS warning and allow to send data to splunk with out signed ssl cert ################
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
##############################################################################################################

serial_port = serial.Serial(
    "/dev/ttyS0",  # your serial port name,for rasberry pi 2,3 and 4 ttyS0 should be correct, make sure to disable shell via serial before
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=None,
    rtscts=False,
    dsrdtr=False,
    xonxoff=False
)

S_URL = 'https://<change me to splunk hec uri:8088/services/collector/raw'
authHeader = {'Authorization': 'Splunk <change to splunk hec token'}

def splunk_hec(dictionary):
  message = json.dumps(dictionary)
  try:
    x = requests.post(S_URL, headers=authHeader, data=message, verify=False, timeout=1)
  except: # very greedy, could be refined.
    print("Splunk log error")

while True:
  result = str(serial_port.read_until(b'\r\n!')) # Reading data until it reaches \r\n! <- change according to the data from your meter.
  print(result)
  results = re.findall(r'(?<=\()[0-9.]+', result)
  dictionary ={ 
    "time": str(int(time.time())),
    "meter_active_out": results[1],
    "meter_active_in": results[2],
    "meter_reactive_out": results[3],
    "meter_reactive_in": results[4],
    "active_usage_out": results[5],
    "active_usage_in": results[6],
    "reactive_usage_out": results[7],
    "reactive_usage_in": results[8],
    "L1_active_usage_out": results[9],
    "L1_active_usage_in": results[10],
    "L2_active_usage_out": results[11],
    "L2_active_usage_in": results[12],
    "L3_active_usage_out": results[13],
    "L3_active_usage_in": results[14],
    "L1_reactive_usage_out": results[15],
    "L1_reactive_usage_in": results[16],
    "L2_reactive_usage_out": results[17],
    "L2_reactive_usage_in": results[18],
    "L3_reactive_usage_out": results[19],
    "L3_reactive_usage_in": results[20],
    "L1_phase_voltage": results[21],
    "L2_phase_voltage": results[22],
    "L3_phase_voltage": results[23],
    "L1_phase_current": results[24],
    "L2_phase_current": results[25],
    "L3_phase_current": results[26]
  }
  splunk_hec(dictionary)
serial_port.close()
