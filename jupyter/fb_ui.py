# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class AccCtrl
###########################################################################

class AccCtrl ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Accompaniment", pos = wx.DefaultPosition, size = wx.Size( 928,646 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		self.m_timer2 = wx.Timer()
		self.m_timer2.SetOwner( self, wx.ID_ANY )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Track\nAlbum\nArtist", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer16.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap1.SetMinSize( wx.Size( -1,64 ) )
		
		bSizer16.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 50 ) 
		bSizer16.Add( self.m_gauge1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_bitmap2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button_next = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button_next, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button_last = wx.Button( self, wx.ID_ANY, u"Last", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button_last, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button_pause = wx.Button( self, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button_pause, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button_play = wx.Button( self, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button_play, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer16, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Effect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer2.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		m_choice_algorithmChoices = [ u"Synth hit", u"Synth wave", u"Cymbals" ]
		self.m_choice_algorithm = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_algorithmChoices, 0 )
		self.m_choice_algorithm.SetSelection( 0 )
		bSizer18.Add( self.m_choice_algorithm, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_rhythmChoices = [ u"Synth hit", u"Synth wave", u"Cymbals" ]
		self.m_choice_rhythm = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_rhythmChoices, 0 )
		self.m_choice_rhythm.SetSelection( 0 )
		bSizer18.Add( self.m_choice_rhythm, 0, wx.ALL, 5 )
		
		m_choice_harmonyChoices = [ u"Synth hit", u"Synth wave", u"Cymbals" ]
		self.m_choice_harmony = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_harmonyChoices, 0 )
		self.m_choice_harmony.SetSelection( 0 )
		bSizer18.Add( self.m_choice_harmony, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		bSizer50 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Delay, ms", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer50.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_slider20 = wx.Slider( self, wx.ID_ANY, 10, 0, 50, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer50.Add( self.m_slider20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.Add( bSizer50, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button_sync = wx.Button( self, wx.ID_ANY, u"Sync", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button_sync, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer3.Add( bSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Ctl1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_slider2 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_VERTICAL )
		bSizer4.Add( self.m_slider2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_checkBox1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer3.Add( bSizer4, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Ctl2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer41.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_slider21 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_VERTICAL )
		bSizer41.Add( self.m_slider21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox11 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_checkBox11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer3.Add( bSizer41, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Ctl3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer42.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_slider22 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_VERTICAL )
		bSizer42.Add( self.m_slider22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox12 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.m_checkBox12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer3.Add( bSizer42, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer43 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Ctl4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer43.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_slider23 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_VERTICAL )
		bSizer43.Add( self.m_slider23, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox13 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.m_checkBox13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer3.Add( bSizer43, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer44 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Ctl5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer44.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_slider24 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_VERTICAL )
		bSizer44.Add( self.m_slider24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox14 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.m_checkBox14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer3.Add( bSizer44, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer45 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Ctl6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer45.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_slider25 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_VERTICAL )
		bSizer45.Add( self.m_slider25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox15 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer45.Add( self.m_checkBox15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer3.Add( bSizer45, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer46 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Ctl7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		bSizer46.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_slider26 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_VERTICAL )
		bSizer46.Add( self.m_slider26, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox16 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer46.Add( self.m_checkBox16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer3.Add( bSizer46, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText_t1 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_t1.Wrap( -1 )
		bSizer17.Add( self.m_staticText_t1, 0, wx.ALL, 5 )
		
		self.m_staticText_t2 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_t2.Wrap( -1 )
		bSizer17.Add( self.m_staticText_t2, 0, wx.ALL, 5 )
		
		self.m_staticText_t3 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_t3.Wrap( -1 )
		bSizer17.Add( self.m_staticText_t3, 0, wx.ALL, 5 )
		
		self.m_staticText_t4 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_t4.Wrap( -1 )
		bSizer17.Add( self.m_staticText_t4, 0, wx.ALL, 5 )
		
		self.m_staticText_t5 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_t5.Wrap( -1 )
		bSizer17.Add( self.m_staticText_t5, 0, wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer17, 0, 0, 5 )
		
		self.m_gauge_t1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_t1.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_t1, 0, wx.ALL, 5 )
		
		self.m_gauge_t2 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_t2.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_t2, 0, wx.ALL, 5 )
		
		self.m_gauge_t3 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_t3.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_t3, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer13.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.m_gauge_n1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_n1.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_n1, 0, wx.ALL, 5 )
		
		self.m_gauge_n2 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_n2.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_n2, 0, wx.ALL, 5 )
		
		self.m_gauge_n3 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_n3.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_n3, 0, wx.ALL, 5 )
		
		self.m_gauge_n4 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_n4.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_n4, 0, wx.ALL, 5 )
		
		self.m_gauge_n5 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_n5.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_n5, 0, wx.ALL, 5 )
		
		self.m_gauge_n6 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_n6.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_n6, 0, wx.ALL, 5 )
		
		self.m_gauge_n7 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_n7.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_n7, 0, wx.ALL, 5 )
		
		self.m_gauge_n8 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_n8.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_n8, 0, wx.ALL, 5 )
		
		self.m_gauge_n9 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_n9.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_n9, 0, wx.ALL, 5 )
		
		self.m_gauge_n10 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_n10.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_n10, 0, wx.ALL, 5 )
		
		self.m_gauge_n11 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_n11.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_n11, 0, wx.ALL, 5 )
		
		self.m_gauge_n12 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		self.m_gauge_n12.SetValue( 0 ) 
		bSizer13.Add( self.m_gauge_n12, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer13.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE )
		bSizer13.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

	