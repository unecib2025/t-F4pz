#1

ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "192.168.1.10"]
result = set(ips)
print(result)

#2

blocked = {"root", "admin", "test"}
blocked.add("hacker")
blocked.remove("test")
print(blocked)

#3

blocked_ports = {21, 22, 23, 25}
port = 22
print("Порт запрещён" if port in blocked_ports else "Порт разрешён")

#4

known = {"mal.com", "bad.net"}
new = {"bad.net", "xevil.org"}
result = new - known
print(result)

#5

white = {"alice", "bob", "root"}
black = {"root", "admin"}
result = white & black
print(result)

#6

A = {"CVE-1", "CVE-2"}
B = {"CVE-2", "CVE-3"}
result = A | B
print(result)

#7

admin = {"read", "write", "delete"}
user = {"read", "download"}
result = admin ^ user
print(result)

#8

all_pass = ["123", "qwerty", "test", "123", "qwerty", "admin"]
forbidden = {"test"}
result = set(all_pass) - forbidden
print(result)

#9

global_ips = { "10.0.0.1", "10.0.0.2", "192.168.1.1" }
local_ips = { "10.0.0.2", "10.0.0.3" }
local_ips.intersection_update(global_ips)
print(local_ips)

#10

logs = ["scan", "debug_mode", "scan", "connect", "debug_info"]
result = {cmd for cmd in logs if "debug" not in cmd}
print(result)