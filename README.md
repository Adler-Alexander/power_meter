# Power meter
## Visualize and take control over your power usage
This project is to document my journey to read data from the new smart power meters that now are being deployed all around Sweden as well as many other countries in Europe and send this data over https to a collection tool. Note that the script can easily be modified to collect the data in any other form.
The included script is reading the data everytime the meter is sending it (atleast every 10 seconds according to Swedish regulation) and then parsing it before sending it via HTTPS. 

<img width="1108" alt="image" src="https://user-images.githubusercontent.com/13958361/198015794-30402467-f45d-4e6f-8e91-1ca6bedf4e1a.png">
<img width="258" height="239" alt="image" src="https://user-images.githubusercontent.com/13958361/198015866-60a452d2-8844-478f-a78b-ef394c4d40e4.png">


Current version is written to send it's data to Splunk via HTTP Event Collector.
https://docs.splunk.com/Documentation/Splunk/9.0.1/Data/UsetheHTTPEventCollector

## Requirements
A power meter with a P1/HAN port and the port enabled
A Raspberry Pi 2,3 or 4 (might be possible to use a Zero as well, not tested)
R11 or RJ12 contact that can be connected to the powermeter
1 NPN transistor
3 1k resistor

## How to:
1. Solder or wire the components according to this diagram.
<img width="384" alt="image" src="https://user-images.githubusercontent.com/13958361/198014463-de0ba800-b563-4922-88a8-d41feaac70f0.png">

2. Download or clone the power_meter.py script
3. Modify the script and update the included variables such as serial port and collector details.
4. Install the required Python packages
5. Run power_meter.py


Watch as data is coming in and make some nice graphs! You may even be able to lower your power usage based on the data.
