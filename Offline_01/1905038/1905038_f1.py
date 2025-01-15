
from BitVector import *
import time
import numpy as np
import secrets


Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

round_constant = list([0x00,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36])


def hex_convertion(txt):
    li=[]
    i=0
    while i!=len(txt):
        h = hex(ord(txt[i]))[2:]
        li.append(h)
        i+=1
    return li

def substitution(mtx, flag):
    i=0
    
    while i!=4:
        j=0
        while j != 4:
            if flag:
                k = mtx[i][j].intValue()
                k = InvSbox[k]
                k = BitVector(intVal = k, size = 8)
                mtx[i][j] = k
            else:
                k=mtx[i][j].intValue()
                k = Sbox[k]
                k = BitVector(intVal = k, size = 8)
                mtx[i][j] = k
            j+=1
        i+=1
    return mtx

def create_null_matrix():
    k = [[],[],[],[]]
    return k

def Row_shift(mtx,flag):
    j=0
    while j!= 4:
        match flag:
            case True:
                k = mtx[j][:-j]
                l = mtx[j][-j:]
                mtx[j] =  l +k
            case False:
                k = mtx[j][:j]
                l = mtx[j][j:]
                mtx[j] = l + k
        j+=1
    return mtx

def col_mix(mtx,flag):
    
    st = create_null_matrix()
    
    i=0
    
    while i != 4:
        j=0
        while j != 4:
            k=0
            bt = "00000000"
            temp = BitVector(bitstring = bt)
            while k != 4:
                l=BitVector(bitstring='100011011')
                match flag:
                    case True:
                        l = InvMixer[j][k].gf_multiply_modular(mtx[k][i], l, 8)
                    case False:
                        l = Mixer[j][k].gf_multiply_modular(mtx[k][i], l, 8)
                temp = temp ^ l
                k+=1
            st[j].append(temp)
            j+=1
        i+=1
    return st


def expand_key(rn,klist):
    
    l1=create_null_matrix()
    l2=create_null_matrix()
    i=0
    
    while i!= 4:
        j=0
        while j != 4:
            h = i*4 + j
           
            h=klist[h]
           
            h=BitVector(hexstring=h)
            
            l1[i].append(h)

            j+=1
        i+=1
    
    e1=l1[3][1:]
    e2=l1[3][:1]
    l1[3]=e1 + e2
   
    j=0
    while j!= 4:
        h=l1[3][j].intValue()
        h=Sbox[h]
        h=BitVector(intVal=h,size=8)
        l1[3][j]=h
        j+=1
   
    h=round_constant[rn]
    h=BitVector(intVal=h,size=8)
    l1[3][0] ^= h
    

    j=0
    while j!= 4:
        h=l1[0][j] ^ l1[3][j]
        l2[0].append(h)
        j+=1
    j=0
    while j!=4:
        h=l1[1][j] ^ l2[0][j]
        l2[1].append(h)
        j+=1
    j=0
    while j!=4:
        h=l1[2][j] ^ l2[1][j]
        l2[2].append(h)
        j+=1
    j=0
    l3=[]
    while j!= 4:
        h=klist[3*4+j]
        h=BitVector(hexstring=h)
        l3.append(h)
        j+=1
    j=0
    while j!= 4:
        h=l3[j] ^ l2[2][j]
        l2[3].append(h)

        j+=1
    l4=[]
    j=0
    
    while j!=4:
        k=0
        while k != 4:
            h=l2[j][k].get_bitvector_in_hex()
            l4.append(h)
            k+=1
       
        j+=1
   
    return l4

def generate_all_key(klist):
    temp = []
    all_list=[]
    j=0
    while j!= 16:
        temp.append(klist[j])
        j+=1
    all_list.append(temp)
    j=1
    while j!=11:
        klist = expand_key(j,klist)
    
        temp = []
        k=0
        while k!= 16:
            h=klist[k]
            temp.append(h)
            k+=1
        all_list.append(temp)
        j+=1
    
    return all_list

def create_matrix_column_major(klist):
    
    state = create_null_matrix()
    
    j=0
    
    while j!= 4:
        k=0
        while k != 4:
            h=j*4 + k
            h=klist[h]
            h=BitVector(hexstring=h)

            state[k].append(h)
            k+=1
        j+=1

    return state
def convert_to_text(hlist):
    txt = ""
    for i in range(16):
        txt += chr(int(hlist[i],16))
    return txt

def apply_xor(v1,v2):
    
    temp = create_null_matrix()
   
    j=0
    
    while j!= 4:
        k=0
        while k != 4:
            h=v1[j][k] ^ v2[j][k]
            temp[j].append(h)

            k+=1
        j+=1
    
    return temp

def doing_encrypt(klist,matrix):
    h = apply_xor(matrix,create_matrix_column_major(klist[0]))
    j=1
    while j!= 11:
        h = substitution(h,False)
        h = Row_shift(h,False)
        match j-10 < 0 :
            case True:
                h= col_mix(h,False)

        h = apply_xor(h,create_matrix_column_major(klist[j]))
        j+=1
        
    l1 = []
    j=0
    while j!= 4:
        k=0
        while k != 4:
            hp = h[k][j].get_bitvector_in_hex()
            l1.append(hp)
            k+=1
        j+=1

    return l1

def doing_decrypt(klist,matrix):
    h = apply_xor(matrix,create_matrix_column_major(klist[10]))
    
    j=9
    while j!= -1:
        
        h = Row_shift(h,True)
        h = substitution(h,True)
        h = apply_xor(h,create_matrix_column_major(klist[j]))
        match j > 0 :
            case True:
                h= col_mix(h,True)

        j-=1
    l1 = []
    j=0
    while j!= 4:
        k=0
        while k != 4:
            hp = h[k][j].get_bitvector_in_hex()
            l1.append(hp)
            k+=1
        j+=1

    return l1


def xor_IV_OR_cipher_Plaintext(list1, list2):
    l1=[]
    for i in range(16):
        h1= BitVector(hexstring=list1[i])
        h2=BitVector(hexstring=list2[i])
        h = h1 ^ h2

        l1.append(h.get_bitvector_in_hex())
    return l1



if __name__ == "__main__":

    in_stream = open("D:\\CSE406\\OFFLINE_01\\SECU_OFFLINE1\\ajoy\\INPUT.txt","r")
    given_plaintext = in_stream.readline()[:-1]
    given_key = in_stream.readline()
    in_stream.close()

    # given_plaintext = "To demonstrate Sender and Receiver, use TCP Socket Programming. To make things easy,"
    # given_plaintext = "Never Gonna Give you up"
    # given_plaintext = "Two One Nine Twosd"
    # given_key = "Thats my Kung Fu"
    # given_key = "BUET CSE19 Batch"

    if len(given_key) > 16:
        given_key = given_key[:16]
    else:
        given_key =  given_key + "\0" * (16 - len(given_key))
        

    if len(given_plaintext) % 16 !=0:
        h = len(given_plaintext) // 16
        h+=1
        given_plaintext += "\0" * (h*16 - len(given_plaintext))

    print("Key:")
    print("In ASCII : " , end=" ")
    print(given_key)
    print("In Hex :",end=" ")
    hex_key_list=hex_convertion(given_key)
    print(*hex_key_list,sep=" ")
    print()
    print("Plain Text:")
    print("In ASCII:  "+given_plaintext)
    print("In Hex:",end=" ")
    hex_plain_list = hex_convertion(given_plaintext)
    print(*hex_plain_list,sep=" ")

    plain_list = []
    i=0
    while i!= len(given_plaintext):
        plain_list.append(given_plaintext[i:i+16])
        i+=16


    rk_start_time = time.time()
    all_key_list = generate_all_key(hex_key_list)
    rk_end_time = time.time()

    encryption_time = 0
    decryption_time = 0

    #generate random Initial vector
    r_bytes_for_IV = secrets.token_bytes(16)
    iv_list = [format(byte, '02x') for byte in r_bytes_for_IV]
    # iv_list = ['00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00']

    cipher_list = []
    decrypted_list = []
    text_cipher = ""
    text_decrypted = ""

    j=0
    while j!= len(plain_list):
        p_text = plain_list[j]
        # print(p_text)
        hex_p_text = hex_convertion(p_text)
        # print(hex_p_text)

        if j == 0 :
            hex_p_text = xor_IV_OR_cipher_Plaintext(iv_list,hex_p_text)

        else:
            hex_p_text = xor_IV_OR_cipher_Plaintext(cipher_list[j-1],hex_p_text)

        matrix = create_matrix_column_major(hex_p_text)
        time_1 = time.time()
        new_cipher = doing_encrypt(all_key_list,matrix)
        time_2 = time.time()
        encryption_time += (time_2 - time_1)
        cipher_list.append(new_cipher)

        j+=1

    j=0
    while j!= len(cipher_list):
        matrix = create_matrix_column_major(cipher_list[j])
        time_1 = time.time()
        new_decrypted = doing_decrypt(all_key_list,matrix)
        time_2 = time.time()
        decryption_time += (time_2 - time_1)
        if j == 0:
            new_decrypted = xor_IV_OR_cipher_Plaintext(iv_list,new_decrypted)
        else:
            new_decrypted = xor_IV_OR_cipher_Plaintext(cipher_list[j-1],new_decrypted)

        decrypted_list.append(new_decrypted)

        j+=1

    print()
    print("Ciphered Text:")
    print("In HEX:",end=" ")
    for i in range(len(cipher_list)):
        for j in range(len(cipher_list[i])):
            print(str(cipher_list[i][j]),end=" ")
            text_cipher += chr(int(cipher_list[i][j],16))

    print()

    print("In ASCII : "+text_cipher)
    print()

    print("Deciphered Text:")
    print("In HEX :",end=" ")
    for i in range(len(decrypted_list)):
        for j in range(len(decrypted_list[i])):
            print(str(decrypted_list[i][j]),end=" ")
            text_decrypted += chr(int(decrypted_list[i][j],16))

    print()
    print("In ASCII : "+text_decrypted)
    print()

    print("Execution Time Details:")
    print("Key Schedule Time: "+str((rk_end_time - rk_start_time) * 1000)+" ms")
    print("Encryption Time: "+str(encryption_time * 1000)+" ms")
    print("Decryption Time: "+str(decryption_time *1000)+" ms")



    
    