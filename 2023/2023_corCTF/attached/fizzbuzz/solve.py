from pwn import *

server = remote("be.ax", 31100)

server.recvuntil("n = ")
n = int(server.recvline())
server.recvuntil("e = ")
e = int(server.recvline())
server.recvuntil("ct = ")
ct = int(server.recvline())


r = 2 # make sure r is invertible
to_send = (pow(r, e, n) * (ct % n) ) % n

server.sendline(str(to_send))

server.recvuntil("> ")
flag_r = int(server.recvline())


from Crypto.Util.number import *

flag = flag_r * pow(r, -1, n) % n
print(long_to_bytes(flag)[16:-16])