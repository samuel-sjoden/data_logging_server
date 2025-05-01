import socket
import re
from utils import handle_input, handle_output, handle_moisture, handle_water, handle_datalog

# Host address and port number
HOST = "0.0.0.0"
PORT = 12345

# Regex patterns that the client can use to indicate which data they are logging
input_pattern = r"^Input Bucket$"
output_pattern = r"^Output Bucket$"
moisture_pattern = r"Moisture"
water_pattern = r"Water"
datalog_pattern = r"Datalog"


def start_service(workbook_path):
    """
    Starts a server socket on the HOST address at the PORT number
    :param (str) workbook_path: A path to an empty feeding log excel worksheet.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        data, client_addr = server.recvfrom(1024)
        data = data.decode().strip()
        print(f"Received message from {client_addr}: {data}")

        if re.search(input_pattern, data):
            handle_input(server, client_addr, workbook_path)
        elif re.search(output_pattern, data):
            handle_output(server, client_addr, workbook_path)
        elif re.search(moisture_pattern, data):
            handle_moisture(server, client_addr, workbook_path, data)
        elif re.search(water_pattern, data):
            handle_water(server, client_addr, workbook_path, data)
        elif re.search(datalog_pattern, data):
            handle_datalog(server, client_addr, workbook_path, data)
        else:
            server.sendto(f"Invalid Command".ljust(100, '\0').encode(), client_addr)

