#!/usr/bin/env python
import sys, os
import pygtk, gtk, gobject
import pygst
pygst.require("0.10")
import gst
import time

class GTK_Main:
  
	def __init__(self):
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("Input-selector test")
		window.set_default_size(300, 100)
		window.connect("destroy", gtk.main_quit, "WM destroy")
		vbox = gtk.VBox()
		window.add(vbox)
		self.movie_window = gtk.DrawingArea()
		vbox.add(self.movie_window)
		hbox = gtk.HBox()
		vbox.pack_start(hbox, False)
		hbox.set_border_width(10)
		hbox.pack_start(gtk.Label())
		self.button = gtk.Button("1) Press this (After that press Start )")
		self.button.connect("clicked", self.start_stop)
		hbox.pack_start(self.button, False)
		self.button2 = gtk.Button("2) Press Switch (to see if you can seamlessly view the switching)")
		self.button2.connect("clicked", self.exit)
		hbox.pack_start(self.button2, False)
		hbox.add(gtk.Label())
		window.show_all()
    
		self.mySwitch = "sink1"

  # Action
	def start_stop(self, w):
		if self.button.get_label() == "Start":
			self.button.set_label("Stop")
			#self.player.set_state(gst.STATE_PLAYING)
		else:
			#self.player.set_state(gst.STATE_NULL)
			self.button.set_label("Start")

  # Exit
	def exit(self, widget, data=None):
		while True:
			print "Switching to: " + self.mySwitch;     
			if self.mySwitch.startswith("sink0"):
				self.mySwitch = "sink1"
			else:
				self.mySwitch = "sink0"      
			time.sleep(5)
      
GTK_Main()
gtk.gdk.threads_init()
gtk.main()
