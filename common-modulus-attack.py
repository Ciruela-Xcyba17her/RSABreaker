#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------PLEASE SET (n, e1, e2, c1, c2)--------
def set_values():
    n=
    e1=
    e2=
    c1=
    c2=
    return n, e1, e2, c1, c2
#----------------------------------------------

#return GCD(a, b)
def gcd(a, b):
    while not a % b == 0:
        tmp = b
        b = a % b
        a = tmp

    return b

#Extended_Euclidean_algorithm
def extend_gcd(a, b, c):
    if a < 0 and b < 0:
        a = -a
        b = -b
        c = -c
    
    x1 = y2 = 1
    x2 = y1 = 0
    
    num_a = a
    num_b = b
    
    if a < 0:
        x1 = -1
        num_a = -num_a
    elif b<0:
        y2 = -1
        num_b = -num_b

    g = gcd(num_a, num_b)
    mul = c // g
    
    while not num_a % num_b == 0:
        tmp_x = x2
        tmp_y = y2

        q = num_a // num_b
        
        x2 = x1-x2*q
        y2 = y1-y2*q
        x1 = tmp_x
        y1 = tmp_y

        tmp = num_b
        num_b = num_a%num_b
        num_a = tmp

    return x2*mul, y2*mul

#solve (base^exp) mod n
def solve_exp_mod(base, exp, n):

    if exp >= 0:
        expbin = format(exp, 'b')
        expbintext = str(expbin)
        
        result=1
        
        for c in expbintext:
            if c == '1':
                result = result * result * base % n
            else:
                result = result * result % n

        return result

    else:
        modifiedbase = pow(base, -exp)
        ret, gomi = extend_gcd(modifiedbase, -n, 1);
        return ret

def main():
    n, e1, e2, c1, c2 = set_values()
    s1, s2 = extend_gcd(e1, e2, 1)
    
    M1=solve_exp_mod(c1, s1, n)
    M2=solve_exp_mod(c2, s2, n)
    plaintext = (M1 * M2) % n
    
    print("Plain text is ...")
    print("-- dec version --")
    print(plaintext)
    print("-- hex version --")
    print(format(plaintext, 'x'))
    
if __name__=="__main__":
    main()
