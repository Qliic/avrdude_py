#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from Tkinter import * 

import subprocess
import os

avrdude = os.system('/home/francois/Qliic/avrdude_nano.sh ' + sys.argv[1] )

fenetre = Tk()

label = Label(fenetre, text='nano:'+sys.argv[1])
label.pack()

fenetre.mainloop()
