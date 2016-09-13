import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.PMOD[0].rename('S1').input().on()
icestick.PMOD[1].rename('S2').input().on()
icestick.PMOD[2].rename('S3').input().on()
icestick.PMOD[3].rename('S4').input().on()
icestick.D1.on()

main = icestick.main()
I = Array4(main.S1, main.S2, main.S3, main.S4)
O = main.D1

def f(A, B, S0, S1):
    if S1:
        if S0: return A^B
        else:  return A&B
    else:
        if S0: return A|B
        else:  return B

logic = ROM4(f)

wire( logic(I), O )

compile(sys.argv[1], main)

