import math

'''
ATTENTION:
現時点(2018/05/29)で、小さい整数(例えば(e,n)=(42667,64741))に対してはWiener's Attackは成功します。
しかし、以下のような巨大なeとnに対してはなぜか成功しません。
e=30749686305802061816334591167284030734478031427751495527922388099381921172620569310945418007467306454160014597828390709770861577479329793948103408489494025272834473555854835044153374978554414416305012267643957838998648651100705446875979573675767605387333733876537528353237076626094553367977134079292593746416875606876735717905892280664538346000950343671655257046364067221469807138232820446015769882472160551840052921930357988334306659120253114790638496480092361951536576427295789429197483597859657977832368912534761100269065509351345050758943674651053419982561094432258103614830448382949765459939698951824447818497599
n=109966163992903243770643456296093759130737510333736483352345488643432614201030629970207047930115652268531222079508230987041869779760776072105738457123387124961036111210544028669181361694095594938869077306417325203381820822917059651429857093388618818437282624857927551285811542685269229705594166370426152128895901914709902037365652575730201897361139518816164746228733410283595236405985958414491372301878718635708605256444921222945267625853091126691358833453283744166617463257821375566155675868452032401961727814314481343467702299949407935602389342183536222842556906657001984320973035314726867840698884052182976760066141
'''

#--------PLEASE SET TWO VALUES--------
def set_values():
    e=42667
    n=64741
    return e, n
#--------------------------------------

def fix_den(m, num, den):
    return m * den + num, den

#連分数を単純な分数num/denに直す
def convert_to_a_fraction(cf):
    index = len(cf) - 1
    num = cf[index - 1]
    
    num, den = fix_den(cf[index - 1], 1, cf[index])
    index -= 1
    
    while True:
        if index == 0:
            return num, den
        else:
            num, den = fix_den(cf[index - 1], den, num)
            index -= 1

'''
This function returns
{int(sqrt(num)) ---if num is a square number.
{-1 ---------------if num is not a square number.
'''
def calcSquare(num):

    if num<0:
        return -1

    maximumbase=1

    while maximumbase<=num:
        maximumbase*=10

    answer=0
    success_flag=False

    while maximumbase>=1:
        maximumbase//=2
        square=pow(answer, 2)

        if square==num:
            success_flag=True
            break
        elif square<num:
            answer+=maximumbase
        else:
            answer-=maximumbase
            
    if success_flag:
        return answer
    else:
        return -1


def main():

    e, n = set_values();
    
    success_flag=False

    cf=[]
    k=e
    d=n
    cf.append(e//n)
    
    while True:
        tmp=d
        d=k%d
        k=tmp
        
        cf.append(k//d)
        
        num, den = convert_to_a_fraction(cf)

        #ファイNは整数であるか
        if (e * den - 1)%num==0:
            print("2nd stage.")
            phaiN=(e*den - 1)//num
            b=n-phaiN+1
            c=n

            rt2=pow(b, 2)-4*c
            rt=calcSquare(rt2)
            
            #sqrt(b^2-4ac)を計算
            if rt2>0 and rt!=-1:
                print("3rd stage.")
                
                #解p,qは整数か
                if b%2==rt%2:
                    print("4th stage.")
                    p=(b+rt)//2
                    q=(b-rt)//2
                    
                    print("p=")
                    print(p)
                    print("q=")
                    print(q)
                    success_flag=True
                    break

        if num==e and den==n:
            break

    if success_flag==False:
        print("failed...")

if __name__ == "__main__":
    main()

