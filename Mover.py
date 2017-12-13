
#!/usr/bin/env python

import nxt.locator
from nxt.motor import *

def spin_around(R2D2):
    m_left = Motor(R2D2, PORT_C)
    m_left.run(100)
    m_right = Motor(R2D2, PORT_B)
    m_right.run(100)
    
    m_left.idle()
    m_right.idle()

R2D2 = nxt.locator.find_one_brick()
spin_around(R2D2)

