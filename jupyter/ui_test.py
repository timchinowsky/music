import time
import fb_ui
import urllib2, cStringIO
import sys
import time
import os
import gc
import matplotlib
matplotlib.use('WXAgg')
#import matplotlib.cm as cm
#import matplotlib.cbook as cbook
#from matplotlib.backends.backend_wxagg import Toolbar, FigureCanvasWxAgg
#from matplotlib.figure import Figure
import numpy as np
import wx
import wx.xrc as xrc
import analysis as an

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

import accomp

spotify = an.spotify_ctrl()
frame = []
plotpanel = None
last_track_id = None
track_name = None

class CanvasPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		self.figure = Figure()
		self.axes1 = self.figure.add_subplot(211)
		self.axes2 = self.figure.add_subplot(212)
		self.canvas = FigureCanvas(self, -1, self.figure)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
		self.SetSizer(self.sizer)
		# self.Fit()

	def draw(self, track_id=None):
		global spotify, track_name
		if track_id is None:
			t = np.arange(0.0, 3.0, 0.01)
			s = np.sin(2 * np.pi * t)
			self.axes1.plot(t, s)
		else:
			keys = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
			modes =['minor', 'major']
			a=spotify.audio_analysis(track_id)
			n_bars = len(a['bars'])
			n_segments = len(a['segments'])
			n_beats = len(a['beats'])
			n_tatums = len(a['tatums'])
			# print n_bars,'bars, ', n_segments, 'segments,', n_beats, 'beats,', n_tatums, 'tatums'
			bar_starts = [ k['start'] for k in a['bars'] ]
			bar_ends = [ k['start']+k['duration'] for k in a['bars'] ]
			segment_starts = [ k['start'] for k in a['segments'] ]
			segment_ends = [ k['start']+k['duration'] for k in a['segments'] ]
			beat_starts = [ k['start'] for k in a['beats'] ]
			beat_ends = [ k['start']+k['duration'] for k in a['beats'] ]
			tatum_starts = [ k['start'] for k in a['tatums'] ]
			tatum_ends = [ k['start']+k['duration'] for k in a['tatums'] ]
			bar_y=0
			segment_y=1
			beat_y=2
			tatum_y=3
			delta_y=0.5
			self.axes1.clear()
			self.axes1.plot([bar_starts, bar_ends], [[bar_y]*len(bar_starts), [bar_y+delta_y]*len(bar_starts)],'b-')
			self.axes1.plot([segment_starts, segment_ends], [[segment_y]*len(segment_starts), [segment_y+delta_y]*len(segment_starts)], 'g-')
			self.axes1.plot([beat_starts, beat_ends], [[beat_y]*len(beat_starts), [beat_y+delta_y]*len(beat_starts)], 'r-')
			self.axes1.plot([tatum_starts, tatum_ends], [[tatum_y]*len(tatum_starts), [tatum_y+delta_y]*len(tatum_starts)], 'c-')
			self.axes1.set_title('Bars, segments, beats, tatums for '+track_name)
			
			self.axes1.text(0,bar_y+delta_y/2, 'Bars', horizontalalignment='right')
			self.axes1.text(0,segment_y+delta_y/2, 'Segments', horizontalalignment='right')
			self.axes1.text(0,beat_y+delta_y/2, 'Beats', horizontalalignment='right')
			self.axes1.text(0,tatum_y+delta_y/2, 'Tatums', horizontalalignment='right')
			
			sec = an.analysis_get(a, 'sections')

			sec_ends = list(np.array(sec['start']) + np.array(sec['duration']))
			self.axes2.clear()
			self.axes2.plot([sec['start'],sec_ends], [sec['key'], list(np.array(sec['key'])+0)])
			for s,k,m in zip(sec['start'],sec['key'],sec['mode']):
				self.axes2.text(s,k,keys[k]+' '+modes[m])
			self.axes2.set_title('Section times and keys')
			self.axes2.set_xlabel('Time, s')
			self.axes2.set_ylabel('Key')
		



def main():
	global frame, plotpanel
	
	accomp.start()
	
	ex = wx.App()
	f = fb_ui.AccCtrl(None)
	frame = f
	f.Bind(wx.EVT_TIMER, update, f.m_timer1)
	
	sizer = f.GetSizer()

	# matplotlib panel itself
	
	panel = CanvasPanel(f)
	panel.draw()
	plotpanel=panel
	
	# wx boilerplate
	sizer.Add(panel, 1, wx.EXPAND)
	f.SetSizer(sizer)
	f.Fit()
	f.m_timer1.Start(1000)
	f.Show()
	ex.MainLoop()    

string = ''
url =  ''
def update(obj):
	global spotify, frame, string, url, last_track_id, track_name
	d = spotify.current_playback()
	current_track_id = d['item']['id']

	track_name = d['item']['name']
	caption = current_track_id+'\n'+d['item']['name']+'\n'+d['item']['album']['name']+'\n'+ ', '.join([a['name'] for a in d['item']['album']['artists']])
	smallest = min([i['height'] for i in d['item']['album']['images']])
	image_url = [i['url'] for i in d['item']['album']['images'] if i['height']==smallest][0]
	url= image_url
	track_id = d['item']['id']
	stream = cStringIO.StringIO(urllib2.urlopen(image_url).read())
	bmp = wx.BitmapFromImage( wx.ImageFromStream( stream ))

	frame.m_staticText1.SetLabel(caption)
	frame.m_bitmap1.SetBitmap(bmp)
	if not current_track_id==last_track_id:
		last_track_id=current_track_id
		accomp.setup(current_track_id)
		accomp.play()
		plotpanel.draw(current_track_id)
	
	
	
class PlotPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent, -1)

		self.fig = Figure((5, 4), 75)
		self.a = self.fig.add_subplot(111)
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
		self.lines = self.a.plot([1,2,3,4,5], [1,4,9,16,25], 'ko')
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