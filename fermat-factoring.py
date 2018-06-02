def is_square(num):

    a = 1
    exp = 0
    
    while a < num:
        a *= 4
        exp += 1
    
    answer = pow(2, exp)
    dist = answer // 2
    
    while True:
        
        num_2 = answer * answer
        
        if num_2 == num:
            return True, answer
        elif num_2 < num:
            answer += dist
        else:
            answer -= dist
        
        if dist==0:
            if num_2 > num:
                return False, answer
            else:
                return False, answer+1
        
        dist //= 2
        

def main():

    # A sample from BKPCTF
    n = 94738740796943840961823530695778701408987757287583492665919730017973847138345511139064596113422435977583856843887008168202003855906708039013487349390571801141407245039011598810542232029634564848797998534872251549660454277336502838185642937637576121533945369150901808833844341421315429263207612372324026271327
    flag, a = is_square(n)
    
    while True:
        flag, b = is_square(a * a - n)
        
        if flag:
            break
        a+=1

    p = a - b
    q = a + b

    print("p=")
    print(p)
    print("q=")
    print(q)

if __name__=="__main__":
    main()
