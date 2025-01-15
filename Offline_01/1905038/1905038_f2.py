

import random
import time

def point_addition(x1,y1,x2,y2,p):

    match x1 == x2 and y1==y2:
        #point doubling
        case True:
            S = (3*x1*x2 + A) * pow(2*y1,-1,p)
        #point addition
        case False:
            S = (y2-y1) * pow(x2 - x1,-1,p)
    
    x3 = (S*S - x1 - x2)%p
    y3 = (S * (x1 - x3) - y1)%p

    assert (y3 * y3) % p == (pow(x3,3,p) + A*x3 + B) % p
    
    L = []
    L.append(x3)
    L.append(y3)
    return L

def generate_prime():
    p = pow(2, 256)
    p = p - pow(2, 32)
    p = p - pow(2, 9) 
    p = p - pow(2, 8) 
    p = p - pow(2, 7) 
    p = p - pow(2, 6)
    p = p - pow(2, 4)
    p = p - pow(2, 0)
    return p


def double_and_add_algorithm(x,y,k,p):
    result_point=[]
    result_point.append(x)
    result_point.append(y)

    h = bin(k)
    h = h[2:]

    i=1
    while i != len(h):
        #We are doing doubling
        result_point = point_addition(result_point[0],result_point[1],result_point[0],result_point[1],p)

        match h[i] == "1":
            case True:
                result_point = point_addition(result_point[0],result_point[1],x,y,p)
        
        assert (result_point[1]* result_point[1]) % p == (pow(result_point[0],3,p) + A*result_point[0] + B) % p
    
        i+=1
    return result_point


A=0
B=7
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424

p = generate_prime()

assert (Gy * Gy) % p == (pow(Gx , 3 ,p) + A*Gx + B) %p



if __name__ == "__main__":

    List = [128 , 192, 256]
    print()
    print("                        Time                    ")
    print(" K         A (ms)                      B (ms)                    R(ms)")

    for j in range(3):
        time_a = 0
        time_b = 0
        time_shared_key_r = 0

        KA = 0
        KB = 0
        public_key_A =0
        public_key_B = 0
        Secret_key_Alice = 0
        Secret_key_Bob = 0
        

        for i in range(5):
            KA = random.getrandbits(List[j])
            KB = random.getrandbits(List[j])

            time1 = time.time()
            public_key_A = double_and_add_algorithm(Gx,Gy,KA,p)
            time2 = time.time()
            time_a += (time2 - time1)
            
            time1 = time.time()
            public_key_B = double_and_add_algorithm(Gx,Gy,KB,p)
            time2 = time.time()

            time_b += (time2 - time1)

            time1 = time.time()
            R = double_and_add_algorithm(public_key_A[0],public_key_A[1],KB,p)
            time2 = time.time()

            Secret_key_Bob = R
            Secret_key_Alice = double_and_add_algorithm(public_key_B[0],public_key_B[1],KA,p) 
            
            time_shared_key_r +=(time2 - time1)
            
        
        # print("The 5th test :")
        # print("KA :  ",KA)
        # print("KB :  ",KB)
        # print("Public key of Alice :  ",public_key_A)
        # print("Public key of Bob :  ",public_key_B)
        # print()
        # print("Secrete key of Alice :  ",Secret_key_Alice)
        # print()
        # print("Secrete key of Bob :  ",Secret_key_Bob)
        # print()

        
        print(str(List[j])+"    "+str((time_a / 5)*1000)+"    "+str((time_b/5)*1000)+"    "+str((time_shared_key_r / 5)*1000))

        
























