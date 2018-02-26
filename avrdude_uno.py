#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from Tkinter import * 

import subprocess
import os
os.system('/home/francois/Qliic/avrdude_uno.sh ' + sys.argv[1] )

fenetre = Tk()

label = Label(fenetre, text='uno:'+sys.argv[1])
label.pack()

fenetre.mainloop()
