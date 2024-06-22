import os
import ipaddress
from datetime import datetime
from mcstatus import JavaServer

start_ip = input("Enter the starting IP: ")
end_ip = input("Enter the ending IP: ")
port = int(input("Enter the port: "))
timeout = int(input("Enter delay time(ms): ")) / 1000

start_ip = ipaddress.IPv4Address(start_ip)
end_ip = ipaddress.IPv4Address(end_ip)

if start_ip > end_ip:
    print("Start IP cannot be greater than End IP")
    exit()

if port < 1 or port > 65535:
    print("Port cannot be less than 1 or greater then 65535")
    exit()

if not os.path.exists("log"):
    os.mkdir("log")

current_ip = start_ip
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
print("\n============================================================")
with open(f"log/{timestamp}.txt", 'w') as file:
    file.write(
        f"Enter the starting IP: {start_ip}\n"
        f"Enter the ending IP: {end_ip}\n"
        f"Enter the port: {port}\n"
        f"Enter delay time(ms): {int(timeout*1000)}\n"
        f"\n============================================================\n"
    )
    while current_ip <= end_ip:
        try:
            server = JavaServer.lookup(f"{current_ip}:{port}", timeout=timeout)
            status = server.status()
            state = f"Server {current_ip}:{port} - Online, Players: {status.players.online}/{status.players.max}, Latency: {round(status.latency)} ms"
            print(state)
            file.write(f"{state}\n")
        except Exception as e:
            print(f"Server {current_ip}:{port} - Offline or Error - {e}")
        current_ip = current_ip + 1
file.close()
