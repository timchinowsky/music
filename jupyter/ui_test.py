import time
import fb_ui
import urllib2, cStringIO
import sys
import time
import os
import gc
import matplotlib
matplotlib.use('WXAgg')
import matplotlib.cm as cm
import matplotlib.cbook as cbook
from matplotlib.backends.backend_wxagg import Toolbar, FigureCanvasWxAgg
from matplotlib.figure import Figure
import numpy as np
import wx
import wx.xrc as xrc
import analysis as an

spotify = an.spotify_ctrl()
frame = []
plotpanel = None
def main():
	global frame, plotpanel
	ex = wx.App()
	f = fb_ui.AccCtrl(None)
	frame = f
	f.Bind(wx.EVT_TIMER, update, f.m_timer1)
	
	sizer = f.GetSizer()

	# matplotlib panel itself
	plotpanel = PlotPanel(f.m_panel1)
	plotpanel.init_plot_data()

	# wx boilerplate
	sizer.Add(plotpanel, 1, wx.EXPAND)
	f.SetSizer(sizer)
	
	f.m_timer1.Start(1000)
	f.Show()
	ex.MainLoop()    

string = ''
url =  ''
def update(obj):
	global spotify, frame, string, url
	d = spotify.current_playback()
	caption = d['item']['name']+'\n'+d['item']['album']['name']+'\n'+ ', '.join([a['name'] for a in d['item']['album']['artists']])
	smallest = min([i['height'] for i in d['item']['album']['images']])
	image_url = [i['url'] for i in d['item']['album']['images'] if i['height']==smallest][0]
	url= image_url
	
	stream = cStringIO.StringIO(urllib2.urlopen(image_url).read())
	bmp = wx.BitmapFromImage( wx.ImageFromStream( stream ))

	frame.m_staticText1.SetLabel(caption)
	frame.m_bitmap1.SetBitmap(bmp)
	
	
	
class PlotPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent, -1)

		self.fig = Figure((5, 4), 75)
		self.canvas = FigureCanvasWxAgg(self, -1, self.fig)
		self.toolbar = Toolbar(self.canvas)  # matplotlib toolbar
		self.toolbar.Realize()
		# self.toolbar.set_active([0,1])

		# Now put all into a sizer
		sizer = wx.BoxSizer(wx.VERTICAL)
		# This way of adding to sizer allows resizing
		sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
		# Best to allow the toolbar to resize!
		sizer.Add(self.toolbar, 0, wx.GROW)
		self.SetSizer(sizer)
		self.Fit()

	def init_plot_data(self):
		ERR_TOL = 1e-6
		a = self.fig.add_subplot(111)

		x = np.arange(120.0) * 2 * np.pi / 60.0
		y = np.arange(100.0) * 2 * np.pi / 50.0
		self.x, self.y = np.meshgrid(x, y)
		z = np.sin(self.x) + np.cos(self.y)
		self.im = a.imshow(z, cmap=cm.RdBu)  # , interpolation='nearest')

		zmax = np.amax(z) - ERR_TOL
		ymax_i, xmax_i = np.nonzero(z >= zmax)
		if self.im.origin == 'upper':
			ymax_i = z.shape[0] - ymax_i
		self.lines = a.plot(xmax_i, ymax_i, 'ko')

		self.toolbar.update()  # Not sure why this is needed - ADS

	def GetToolBar(self):
		# You will need to override GetToolBar if you are using an
		# unmanaged toolbar in your frame
		return self.toolbar

	def OnWhiz(self, evt):
		self.x += np.pi / 15
		self.y += np.pi / 20
		z = np.sin(self.x) + np.cos(self.y)
		self.im.set_array(z)

		zmax = np.amax(z) - ERR_TOL
		ymax_i, xmax_i = np.nonzero(z >= zmax)
		if self.im.origin == 'upper':
			ymax_i = z.shape[0] - ymax_i
		self.lines[0].set_data(xmax_i, ymax_i)

		self.canvas.draw()

	def onEraseBackground(self, evt):
		# this is supposed to prevent redraw flicker on some X servers...
		pass
		
		
class MyForm(wx.Frame):
 
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, "Timer Tutorial 1", 
								   size=(500,500))
 
		# Add a panel so it looks the correct on all platforms
		panel = wx.Panel(self, wx.ID_ANY)
 
		self.timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.update, self.timer)
 
		self.toggleBtn = wx.Button(panel, wx.ID_ANY, "Start")
		self.toggleBtn.Bind(wx.EVT_BUTTON, self.onToggle)
 
	def onToggle(self, event):
		btnLabel = self.toggleBtn.GetLabel()
		if btnLabel == "Start":
			print "starting timer..."
			self.timer.Start(1000)
			self.toggleBtn.SetLabel("Stop")
		else:
			print "timer stopped!"
			self.timer.Stop()
			self.toggleBtn.SetLabel("Start")
 
	def update(self, event):
		print "\nupdated: ",
		print time.ctime()
 
def test():
	app = wx.App(False)
	frame = MyForm().Show()
	app.MainLoop()

		
		
class Example(wx.Frame):
		   
	def __init__(self, *args, **kw):
		super(Example, self).__init__(*args, **kw) 
		
		self.InitUI()
		
	def InitUI(self):   

		txt1 = '''I'm giving up the ghost of love
in the shadows cast on devotion
She is the one that I adore
creed of my silent suffocation
Break this bittersweet spell on me
lost in the arms of destiny'''

		txt2 = '''There is something in the way
You're always somewhere else
Feelings have deserted me
To a point of no return
I don't believe in God
But I pray for you'''

		pnl = wx.Panel(self)
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		st1 = wx.StaticText(pnl, label=txt1, style=wx.ALIGN_CENTRE)
		st2 = wx.StaticText(pnl, label=txt2, style=wx.ALIGN_CENTRE)
		
		vbox.Add(st1, flag=wx.ALL, border=5)
		vbox.Add(st2, flag=wx.ALL, border=5)
		pnl.SetSizer(vbox)
		
		self.SetSize((250, 260))
		self.SetTitle('Bittersweet')
		self.Centre()
		self.Show(True)          
			  




# Run the program
if __name__ == "__main__":
	#app = wx.PySimpleApp()
	app = wx.App(False)
	frame = MyForm().Show()
	app.MainLoop()