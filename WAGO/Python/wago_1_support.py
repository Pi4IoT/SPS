#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    Feb 10, 2019 09:48:15 PM CET  platform: Windows NT

import sys
import itertools as it
from pymodbus.client.sync import ModbusTcpClient
import datetime

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

client = ModbusTcpClient(host='192.168.1.50',port=502)
client.connect()
bus = client.read_input_registers(0x2030, 65)

class WagoData:
	def __init__(self, master):
		self.master = master	
		self.updateTemp()
		self.updateTime()
		
	def updateTime(self):
		time = datetime.datetime.now().strftime("Data: %d.%m.%Y  Time:  %H:%M:%S:%f")[:-4]
		w.lblTime.configure(text=time)
		root.after(100, self.updateTime)		
		
	def updateTemp(self):

		response = client.read_holding_registers(0x00,4,unit=1)
		t = response.registers[0]		
		w.lblT1.configure(text=float(t/10.0))
		
		t = response.registers[1]		
		w.lblT2.configure(text=float(t/10.0))
		
		t = response.registers[2]		
		w.lblT3.configure(text=float(t/10.0))
		
		t = response.registers[3]	
		w.lblT4.configure(text=float(t/10.0))
		
		result = client.read_coils(0,4)
		if(result.bits[0]):
			w._img5 = tk.PhotoImage(file="./on.png")
			w.lblInput1.configure(image=w._img5)

		else:
			w._img5 = tk.PhotoImage(file="./off.png")
			w.lblInput1.configure(image=w._img5)
					
		if(result.bits[1]):
			w._img6 = tk.PhotoImage(file="./on.png")
			w.lblInput2.configure(image=w._img6)

		else:
			w._img6 = tk.PhotoImage(file="./off.png")
			w.lblInput2.configure(image=w._img6)
			
		if(result.bits[2]):
			w._img7 = tk.PhotoImage(file="./on.png")
			w.lblInput3.configure(image=w._img7)

		else:
			w._img7 = tk.PhotoImage(file="./off.png")
			w.lblInput3.configure(image=w._img7)
			
		if(result.bits[3]):
			w._img8 = tk.PhotoImage(file="./on.png")
			w.lblInput4.configure(image=w._img8)

		else:
			w._img8 = tk.PhotoImage(file="./off.png")
			w.lblInput4.configure(image=w._img8)
						
		root.after(100, self.updateTemp)
	
def exit():
    root.destroy()

def setOutput1():
	
	w._img1= next(w.images1)
	w.btnOutput1.configure(image=w._img1) 
	if(str(w._img1) == "pyimage12"):  
		client.write_coil(0,False)
	if(str(w._img1) == "pyimage11"):  
		client.write_coil(0,True)		

def setOutput2():
	w._img2= next(w.images2)
	w.btnOutput2.configure(image=w._img2) 
	if(str(w._img2) == "pyimage12"):  
		client.write_coil(1,False)
	if(str(w._img2) == "pyimage11"):  
		client.write_coil(1,True)	

def setOutput3():
	w._img3= next(w.images3)
	w.btnOutput3.configure(image=w._img3) 
	if(str(w._img3) == "pyimage12"):  
		client.write_coil(2,False)
	if(str(w._img3) == "pyimage11"):  
		client.write_coil(2,True)	
def setOutput4():
	w._img4= next(w.images4)
	w.btnOutput4.configure(image=w._img4) 
	if(str(w._img4) == "pyimage12"):  
		client.write_coil(3,False)
	if(str(w._img4) == "pyimage11"):  
		client.write_coil(3,True)	

def init(top, gui, *args, **kwargs):
	global w, top_level, root
	w = gui
	top_level = top
	root = top
	w.image_on = tk.PhotoImage(file='on_slider.png')
	w.image_off = tk.PhotoImage(file='off_slider.png')
	w.images1 = it.cycle([w.image_off, w.image_on])  
	w.images2 = it.cycle([w.image_off, w.image_on])
	w.images3 = it.cycle([w.image_off, w.image_on])
	w.images4 = it.cycle([w.image_off, w.image_on])  
	w._img1= next(w.images1)
	w.btnOutput1.configure(image=w._img1) 
	w._img2= next(w.images2)
	w.btnOutput2.configure(image=w._img2) 
	w._img3= next(w.images3)
	w.btnOutput3.configure(image=w._img3) 
	w._img4= next(w.images4)
	w.btnOutput4.configure(image=w._img4) 
	client.write_coil(0,False)
	client.write_coil(1,False)
	client.write_coil(2,False)
	client.write_coil(3,False) 
	root.attributes("-fullscreen", True)
	root.config(cursor="none")
	WagoData(root)
 
def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import wago_1
    wago_1.vp_start_gui()
    



