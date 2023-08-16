from mcstatus import JavaServer

start_ip = input("Enter the starting IP: ")
end_ip = input("Enter the ending IP: ")
port = int(input("Enter the port: "))

def increment_ip(ip):
    parts = list(map(int, ip.split(".")))
    parts[-1] += 1
    for i in range(3, 0, -1):
        if parts[i] == 256:
            parts[i] = 0
            parts[i-1] += 1
    return ".".join(map(str, parts))

current_ip = start_ip
while current_ip != end_ip:
    # print(current_ip)
    server = JavaServer.lookup((f"{current_ip}:{port}"))
    try:
        status = server.status()
        print(f"Server {current_ip}:{port} - Online, Players: {status.players.online}/{status.players.max}, Latency: {round(status.latency)} ms")
    except Exception as e:
        print(f"Server {current_ip}:{port} - Offline or Error - {e}")

    current_ip = increment_ip(current_ip)

# print(end_ip)  # Print the final IP

# Ping test for the final IP
server = JavaServer.lookup(f"{end_ip}:{port}")
try:
    status = server.status()
    print(f"Server {end_ip}:{port} - Online, Players: {status.players.online}/{status.players.max}, Latency: {round(status.latency)} ms")
except Exception as error:
    print(f"Server {end_ip}:{port} - Offline or Error - {error}")
