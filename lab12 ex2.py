LOGGING_PROFILE = ("192.168.1.100", 514)
server_ip, server_port = LOGGING_PROFILE
print("Server IP:", server_ip)
print("Server Port:", server_port)
try:
    LOGGING_PROFILE[0] = "10.0.0.1"
except TypeError as error:
    print("Modification blocked:", error)
print("Final profile:", LOGGING_PROFILE)
