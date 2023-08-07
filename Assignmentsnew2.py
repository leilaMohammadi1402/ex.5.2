import math
def darag2():
    #a**x+b*x+c
    a=int(input("Enter a:"))
    b=int(input("Enter b :"))
    c=int(input("Enter c :"))

    if a==0:
        print("if a==0 bashad tarif nashodeh mishavad!!!")

    else:   
        delta=(b**2)-(4*a*c)


        if delta<0:
            print(delta," javab nadarad!!!")
        elif delta>0:
            print(delta,"x1:",(-b+(math.sqrt(delta)))/(2*a),"x2:",(-b-(math.sqrt(delta)))/(2*a))
        elif delta==0:
            print(delta,(-b)/(2*a))
darag2()

