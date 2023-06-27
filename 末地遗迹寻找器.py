import math;
import sympy;
a = float(input("输入角度.注意！不要输入90，-90，0，180，-180，如果角度是这个，请选择近似值。如90近似89"))
x = float(input("输入X坐标"))
y = float(input("输入z坐标"))
tsqk = 0
if -90<a<0:
    jd = abs(a)
    ka = 90 - jd
    k = math.tan(ka*3.14/180)
    zf = 1
elif -180<a<-90:
    jd = abs(a)
    ka = jd - 90
    k = math.tan(ka*3.14/180) * -1
    zf = 1
elif 0<a<90:
    ka = 90 - a
    k = math.tan(ka*3.14/180) * -1
    zf = 0
elif 90<a<180:
    ka = a - 90
    k = math.tan(ka*3.14/180)
    zf = 0
else:
    print("玩个锤子，看不懂！（检查你的角度等问题！如输错了超过180，输了个乱七八糟的东西，输了个符号等）")
if tsqk == 0:
    b = y - (k * x)
    g = sympy.Symbol("g")
    mx = sympy.solve((g*k+b)**2-3200521+g**2,g)
    
    print(ka,k,b)

    if zf == 1:
        if mx[0] > 0:
            print("x:",mx[0])
            print("z:",(mx[0]*k+b))
        else:
            print("x:",mx[1])
            print("z:",(mx[1]*k+b))
    elif zf == 0:
        if mx[0] < 0:
            print("x:",mx[0])
            print("z:",(mx[0]*k+b))
        else:
            print("x:",mx[1])
            print("z:",(mx[1]*k+b))

