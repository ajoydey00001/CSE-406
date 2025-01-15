import socket
import random

import importlib
f1 =importlib.import_module("1905038_f1")
f2 = importlib.import_module("1905038_f2")


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


my_socket.bind(("localhost",5000))

my_socket.listen(1)

sock_of_alice , addr_of_alice = my_socket.accept()


received = sock_of_alice.recv(1024).decode()

A,B,Gx,Gy,p,public_key_alice_x,public_key_alice_y = map(int,received.split(','))


print("Received :")
print("A : ",A)
print("B : ",B)
print("Gx : ",Gx)
print("Gy : ",Gy)
print("P : ",p)
print()
print("Public key of Alice :")
print("X : ",public_key_alice_x)
print("Y : ",public_key_alice_y)


private_key_bob = random.getrandbits(256)

public_key_bod = f2.double_and_add_algorithm(Gx,Gy,private_key_bob,p)

my_message = f"{public_key_bod[0]},{public_key_bod[1]}"

sock_of_alice.sendall(my_message.encode())

their_shared_secret_key = f2.double_and_add_algorithm(public_key_alice_x,public_key_alice_y,private_key_bob,p)
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

print()
print(sock_of_alice.recv(1024).decode())

iv_text = sock_of_alice.recv(1024).decode()

iv_list = f1.hex_convertion(iv_text)


cipher_length = int(sock_of_alice.recv(1024).decode())



all_key_list = f1.generate_all_key(hex_shared_key_list)

cipher_list = []
decrypted_list = []


j=0
while j!= cipher_length:
    send_ciphertext = sock_of_alice.recv(1024).decode()
    
    hex_cipher = f1.hex_convertion(send_ciphertext)
    
    cipher_list.append(hex_cipher)
    matrix = f1.create_matrix_column_major(hex_cipher)
    
    new_decrypted = f1.doing_decrypt(all_key_list,matrix)
    
    
    if j == 0:
        new_decrypted = f1.xor_IV_OR_cipher_Plaintext(iv_list,new_decrypted)
    else:
        new_decrypted = f1.xor_IV_OR_cipher_Plaintext(cipher_list[j-1],new_decrypted)

    decrypted_list.append(new_decrypted)

    j+=1

print()
text_decrypted = ""
print("Deciphered Text:")
print("In HEX :",end=" ")
for i in range(len(decrypted_list)):
    for j in range(len(decrypted_list[i])):
        print(str(decrypted_list[i][j]),end=" ")
        text_decrypted += chr(int(decrypted_list[i][j],16))

print()
print()
print("In ASCII : "+text_decrypted)
print()

sock_of_alice.close()
my_socket.close()
