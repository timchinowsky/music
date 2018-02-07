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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Accompaniment", pos = wx.DefaultPosition, size = wx.Size( 755,546 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Track\nAlbum\nArtist", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap1.SetMinSize( wx.Size( -1,64 ) )
		
		bSizer1.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 50 ) 
		bSizer1.Add( self.m_gauge1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_bitmap2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Effect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer2.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice1Choices = [ u"Synth hit", u"Synth wave", u"Cymbals" ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer2.Add( self.m_choice1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer50 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Delay, ms", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer50.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_slider20 = wx.Slider( self, wx.ID_ANY, 10, 0, 50, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer50.Add( self.m_slider20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.Add( bSizer50, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Sync", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
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
		
		bSizer47 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Ctl8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		bSizer47.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_slider27 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_VERTICAL )
		bSizer47.Add( self.m_slider27, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox17 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer47.Add( self.m_checkBox17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer3.Add( bSizer47, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

