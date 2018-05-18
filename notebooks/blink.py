from magma import wire
from mantle import Counter
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.D5.on()

main = icestick.main()

N = 22

counter = Counter(N)
wire(counter.O[N-1], main.D5)

