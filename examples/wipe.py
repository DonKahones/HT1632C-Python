
import time

from ht1632cpy import HT1632C


def scroll_message(msg, color, bg):
    msg_length = len(msg) * interface.fontwidth(interface.font6x8)

    start = interface.width()
    end = -msg_length - 1

    for x in xrange(start, end, -1):
        interface.clear()
        interface.box(0, 0, interface.width(), interface.height(), bg)
        interface.putstr(x, 1, msg, interface.font6x8, color, bg)
        interface.sendframe()
        time.sleep(1/30.0)

interface = HT1632C(1, 0)
interface.pwm(15)


print('panel width is' + repr(interface.width()) +'.')
print('panel height is' + repr(interface.height()) + '.')

for x in range(0, 32):
  for y in range(0, 32):
    interface.plot(x,y,interface.GREEN)
    print('pixel at x=' + repr(x) + ', y=' + repr(y) + '...')
    interface.sendframe()

interface.clear()
interface.sendframe()