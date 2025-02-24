import socket

from local_server import start_service


def main():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("Hostname:  ", host_name)
    print("Host IP: ", host_ip)
    feeding_rate_path = input(f"Enter the path to the excel feeding rate workbook that will be used for "
                              f"data entry on this hot test: ")
    start_service(feeding_rate_path)


if __name__ == "__main__":
    main()
