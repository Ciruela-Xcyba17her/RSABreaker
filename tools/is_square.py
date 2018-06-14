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
    flag, num = is_square(12321)

if __name__ == "__main__":
    main()
