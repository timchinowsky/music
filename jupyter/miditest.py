# Utility functions

import sys

from pyo import *


def show(v):
	sys.stderr.write(repr(v)+'\n')

"""	
s = Server()
s.deactivateMidi()
s.boot()
def midicall(status, data1, data2):
	show('%s %s %s' % (status, data1, data2))
listen = MidiListener(midicall, 99)
listen.run()
show('Listening...')
"""


s = Server()
s.setMidiInputDevice(99)
s.boot()
s.start()


m = Midictl(ctlnumber=[7], minscale=250, maxscale=1000)
p = Port(m, .02)
a = Sine(freq=p, mul=.3).out()
a1 = Sine(freq=p*1.25, mul=.3).out()
a2 = Sine(freq=p*1.5, mul=.3).out()