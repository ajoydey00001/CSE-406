import socket
import random
import secrets

import time

import importlib
f1 =importlib.import_module("1905038_f1")
f2 = importlib.import_module("1905038_f2")



# print("A , B , Gx , Gy , p : ",f2.A,f2.B,f2.Gx,f2.Gy,f2.p , sep=" , ")

print("A : ",f2.A)
print("B : ",f2.B)
print("Gx : ",f2.Gx)
print("Gy : ",f2.Gy)
print("p : ",f2.p)
print("Those are sent to Bob")

my_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

my_socket.connect(("localhost",5000))

private_key_alice = random.getrandbits(256)

public_key_alice = f2.double_and_add_algorithm(f2.Gx,f2.Gy,private_key_alice,f2.p)


sending_message = f"{f2.A},{f2.B},{f2.Gx},{f2.Gy},{f2.p},{public_key_alice[0]},{public_key_alice[1]}"

my_socket.sendall(sending_message.encode())


bob_message = my_socket.recv(1024).decode()
public_key_bob_x,public_key_bob_y = map(int,bob_message.split(','))

print()
print()
print("Public Key Bob : ")
print("X : ",public_key_bob_x)
print("Y : ",public_key_bob_y)

their_shared_secret_key = f2.double_and_add_algorithm(public_key_bob_x,public_key_bob_y,private_key_alice,f2.p)
print()

print("Shared Key : ")
print("X : ",their_shared_secret_key[0])
print("Y : ",their_shared_secret_key[1])

hex_shared_key_string = format(their_shared_secret_key[0],'x')

hex_shared_key_list = [hex_shared_key_string[i:i+2] for i in range(0, len(hex_shared_key_string), 2)]

hex_shared_key_list = hex_shared_key_list[:16]
print()
print("Shared Key : ",end=" ")
print(*hex_shared_key_list,sep=" ")

my_socket.sendall(b"You need to be ready , Alice will send you message")


in_stream = open("D:\\CSE406\\OFFLINE_01\\SECU_OFFLINE1\\ajoy\\INPUT.txt","r")
given_plaintext = in_stream.readline()[:-1]
# given_key = in_stream.readline()
in_stream.close()

# given_plaintext = "To demonstrate Sender and Receiver, use TCP Socket Programming. To make things easy,"
# given_plaintext = "Never Gonna Give you up"
# given_plaintext = "Two One Nine Twosd"
# given_key = "Thats my Kung Fu"
# given_key = "BUET CSE19 Batch"

 

if len(given_plaintext) % 16 !=0:
    h = len(given_plaintext) // 16
    h+=1
    given_plaintext += "\0" * (h*16 - len(given_plaintext))


hex_key_list=hex_shared_key_list

print()
print("Plain Text:")
print("In ASCII:  "+given_plaintext)
print("In Hex:",end=" ")
hex_plain_list = f1.hex_convertion(given_plaintext)
print(*hex_plain_list,sep=" ")

plain_list = []
i=0
while i!= len(given_plaintext):
    plain_list.append(given_plaintext[i:i+16])
    i+=16




all_key_list = f1.generate_all_key(hex_key_list)




#generate random Initial vector
r_bytes_for_IV = secrets.token_bytes(16)
iv_list = [format(byte, '02x') for byte in r_bytes_for_IV]


iv_text = f1.convert_to_text(iv_list)


my_socket.sendall(iv_text.encode())



cipher_list = []

text_cipher = ""


j=0
while j!= len(plain_list):
    p_text = plain_list[j]
   
    hex_p_text = f1.hex_convertion(p_text)
    
    if j == 0 :
        hex_p_text = f1.xor_IV_OR_cipher_Plaintext(iv_list,hex_p_text)

    else:
        hex_p_text = f1.xor_IV_OR_cipher_Plaintext(cipher_list[j-1],hex_p_text)

    matrix = f1.create_matrix_column_major(hex_p_text)
    
    new_cipher = f1.doing_encrypt(all_key_list,matrix)
    
    cipher_list.append(new_cipher)

    j+=1



my_socket.sendall(str(len(cipher_list)).encode())
print()
print("Ciphered Text:")
print("In HEX:",end=" ")
for i in range(len(cipher_list)):
    
    for j in range(len(cipher_list[i])):
        print(str(cipher_list[i][j]),end=" ")
        text_cipher += chr(int(cipher_list[i][j],16))
    temp = f1.convert_to_text(cipher_list[i])
    my_socket.sendall(temp.encode())
    time.sleep(0.5)
    
    

print()
print()
print("In ASCII : "+text_cipher)
print()

my_socket.close()

