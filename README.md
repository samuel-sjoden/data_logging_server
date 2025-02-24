# Data Logging Server
For on-site data logging of feeding rate workbooks

## Features
- Rapid recording of feeding rate logs
- Timestamped records and observations
- Ease of custom data collection

## Installation
1. Clone the repository:
```bash
git clone https://github.com/samuel-sjoden/data_logging_server.git
```
2. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Usage
  1. Connect the server host to the Wi-Fi hotspot.
  2. Run main.py
  3. Enter the path to the designated Feeding Rate workbook
  4. Find the server IP address
     Run in the command shell and find the IP4 address
```bash
     ipconfig
```
  5. Connect a client to port number '12345'
  6. Send requests

## Requests
To make a request, the following keywords are required

| Request   | Keyword |
| -------- | ------- |
| Input Bucket  | Input Bucket    |
| Output Bucket | Output Bucket  |
|  Input Moisture Reading   | Moisture    |
|  Datalog   | Datalog    |
