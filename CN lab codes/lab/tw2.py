import random
import math
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
def generate_prime(bits):
    while True:
        num=random.getrandbits(bits)
        if is_prime(num):
            return num
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def mod_inverse(a,m):
    m0,x0,x1=m,0,1
    while a>1:
        q=a//m
        m,a=a%m,m
        x0,x1=x1-q*x0,x0
    return x1+m0 if x1<0 else x1
def generate_key_pair(bits):
    p=generate_prime(bits)
    q=generate_prime(bits)
    n=p*q
    phi=(p-1)*(q-1)
    while True:
        e=random.randint(2,phi-1)
        if gcd(e,phi)==1:
            break
    d=mod_inverse(e,phi)
    public_key=(n,e)
    private_key=(n,d)
    return public_key,private_key
def encrypt(public_key,message):
    n,e=public_key
    cipher_text=[pow(ord(char),e,n) for char in message]
    return cipher_text
def decrypt(private_key,cipher_text):
    n,d=private_key
    decrypted_message="".join([chr(pow(char,d,n)) for char in cipher_text])
    return decrypted_message
if __name__=="__main__":
    bits=8
    public_key,private_key=generate_key_pair(bits)
    print(f"Generated public key{public_key}\n Generated private key {private_key}")
    message=input("Enter the message")
    encrypted_message=encrypt(public_key,message)
    print(f"Encrypted message{encrypted_message}")
    decrypted_message=decrypt(private_key,encrypted_message)
    print(f"Decryped message{decrypted_message}")
    