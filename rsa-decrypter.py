#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------PLEASE SET SOME VALUES---------

def set_values():
    p=6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151
    q=531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127
    e=65537
    c=953261055124841976672520125012331397330972622347198834845913656589179738125611883468602572551434931192119197475986923769822963910105287247445037038553920670208297190901279941873393839526840847522877497136292428956797380906646624271798166314157667181627381040367345892762782184144819848065377557874809694877535510318529583865811458682674018

    return p, q, e, c

#---------------------------------------


#return GCD(a, b)
def gcd(a, b):
    while not a % b == 0:
        tmp=b
        b = a%b
        a = tmp

    return b

#Extended_Euclidean_algorithm
def extend_gcd(a, b, c):
    if a<0 and b<0:
        a=-a
        b=-b
        c=-c
    
    x1=y2=1
    x2=y1=0
    
    num_a=a
    num_b=b
    
    if a<0:
        x1=-1
        num_a=-num_a
    elif b<0:
        y2=-1
        num_b=-num_b

    g=gcd(num_a, num_b)
    mul=c//g
    
    while not num_a % num_b == 0:
        tmp_x=x2
        tmp_y=y2

        q=num_a//num_b
        
        x2=x1-x2*q
        y2=y1-y2*q
        x1=tmp_x
        y1=tmp_y

        tmp=num_b
        num_b=num_a%num_b
        num_a=tmp

    return x2*mul, y2*mul



#calculate (base^exp) mod n
def solve_exp_mod(base,exp,n):

    expbin=format(exp,'b')
    expbintext=str(expbin)
    
    plaintext=1
    
    for c in expbintext:
        if c=='1':
            plaintext=plaintext*plaintext*base%n
        else:
            plaintext=plaintext*plaintext%n

    return plaintext


        
def main():

    p, q, e, c = set_values()
    
    n=p*q
    en=(p-1)*(q-1)
    
    d,k=extend_gcd(e,en,1)

    # P = C^d mod n
    plaintext=solve_exp_mod(c,d,n)
    
    print("Plain text is ...")
    print("-- dec version --")
    print(plaintext)
    print("-- hex version --")
    print(format(plaintext,'x'))
    
if __name__=="__main__":
    main()
