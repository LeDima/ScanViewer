# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

GET1 = 1000
GET2 = 1001
GET3 = 1002
GET4 = 1003

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ScanViewer", pos = wx.DefaultPosition, size = wx.Size( 800,900 ), style = wx.DEFAULT_FRAME_STYLE|wx.SIMPLE_BORDER )
		
		self.SetSizeHintsSz( wx.Size( 800,900 ), wx.Size( 800,900 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		gSizer2 = wx.GridSizer( 2, 0, 0, 0 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"GUN#1" ), wx.VERTICAL )
		
		self.m_textCtrlGUN1X = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"X=+0.0003", wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.m_textCtrlGUN1X.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		sbSizer3.Add( self.m_textCtrlGUN1X, 0, 0, 5 )
		
		self.m_textCtrlGUN1Y = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.m_textCtrlGUN1Y.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		sbSizer3.Add( self.m_textCtrlGUN1Y, 0, 0, 5 )
		
		
		gSizer2.Add( sbSizer3, 1, wx.ALIGN_TOP, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"GUN#2" ), wx.VERTICAL )
		
		self.m_textCtrlGUN2X = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.m_textCtrlGUN2X.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		sbSizer2.Add( self.m_textCtrlGUN2X, 0, 0, 5 )
		
		self.m_textCtrlGUN2Y = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.m_textCtrlGUN2Y.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		sbSizer2.Add( self.m_textCtrlGUN2Y, 0, 0, 5 )
		
		
		gSizer2.Add( sbSizer2, 1, wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer5.Add( gSizer2, 0, wx.EXPAND, 5 )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Schem.bmp", wx.BITMAP_TYPE_ANY ), wx.Point( -1,-1 ), wx.Size( 530,435 ), 0 )
		self.m_bitmap1.SetMinSize( wx.Size( 510,435 ) )
		self.m_bitmap1.SetMaxSize( wx.Size( 520,435 ) )
		
		bSizer5.Add( self.m_bitmap1, 0, wx.EXPAND, 5 )
		
		gSizer21 = wx.GridSizer( 2, 0, 0, 0 )
		
		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"GUN#3" ), wx.VERTICAL )
		
		self.m_textCtrlGUN3X = wx.TextCtrl( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.m_textCtrlGUN3X.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		sbSizer31.Add( self.m_textCtrlGUN3X, 0, 0, 5 )
		
		self.m_textCtrlGUN3Y = wx.TextCtrl( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.m_textCtrlGUN3Y.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		sbSizer31.Add( self.m_textCtrlGUN3Y, 0, 0, 5 )
		
		
		gSizer21.Add( sbSizer31, 1, wx.ALIGN_TOP, 5 )
		
		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"GUN#4" ), wx.VERTICAL )
		
		self.m_textCtrlGUN4X = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.m_textCtrlGUN4X.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		sbSizer21.Add( self.m_textCtrlGUN4X, 0, 0, 5 )
		
		self.m_textCtrlGUN4Y = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.m_textCtrlGUN4Y.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		sbSizer21.Add( self.m_textCtrlGUN4Y, 0, 0, 5 )
		
		
		gSizer21.Add( sbSizer21, 1, wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer5.Add( gSizer21, 0, wx.EXPAND, 5 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1.SetMinSize( wx.Size( 1,1 ) ) 
		self.m_buttonGET1 = wx.Button( self, GET1, u"GET1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonGET1.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		self.m_buttonGET1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1.Add( self.m_buttonGET1, 1, wx.ALL, 5 )
		
		self.m_buttonGET2 = wx.Button( self, GET2, u"GET2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonGET2.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		self.m_buttonGET2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1.Add( self.m_buttonGET2, 1, wx.ALL, 5 )
		
		self.m_buttonGET3 = wx.Button( self, GET3, u"GET3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonGET3.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		self.m_buttonGET3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1.Add( self.m_buttonGET3, 1, wx.ALL, 5 )
		
		self.m_buttonGET4 = wx.Button( self, GET4, u"GET4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonGET4.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		self.m_buttonGET4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1.Add( self.m_buttonGET4, 1, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer1, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		self.m_gridValue = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_gridValue.CreateGrid( 8, 7 )
		self.m_gridValue.EnableEditing( True )
		self.m_gridValue.EnableGridLines( True )
		self.m_gridValue.EnableDragGridSize( False )
		self.m_gridValue.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridValue.SetColSize( 0, 90 )
		self.m_gridValue.SetColSize( 1, 70 )
		self.m_gridValue.SetColSize( 2, 150 )
		self.m_gridValue.SetColSize( 3, 80 )
		self.m_gridValue.SetColSize( 4, 80 )
		self.m_gridValue.SetColSize( 5, 80 )
		self.m_gridValue.SetColSize( 6, 80 )
		self.m_gridValue.EnableDragColMove( False )
		self.m_gridValue.EnableDragColSize( True )
		self.m_gridValue.SetColLabelSize( 35 )
		self.m_gridValue.SetColLabelValue( 0, u"GUN" )
		self.m_gridValue.SetColLabelValue( 1, u"X, Y" )
		self.m_gridValue.SetColLabelValue( 2, u"Present value" )
		self.m_gridValue.SetColLabelValue( 3, u"SET 1" )
		self.m_gridValue.SetColLabelValue( 4, u"SET 2" )
		self.m_gridValue.SetColLabelValue( 5, u"SET 3" )
		self.m_gridValue.SetColLabelValue( 6, u"SET 4" )
		self.m_gridValue.SetColLabelValue( 7, u"Present" )
		self.m_gridValue.SetColLabelValue( 8, u"Present" )
		self.m_gridValue.SetColLabelValue( 9, u"Present" )
		self.m_gridValue.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_gridValue.EnableDragRowSize( True )
		self.m_gridValue.SetRowLabelSize( 0 )
		self.m_gridValue.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.m_gridValue.SetLabelFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
		
		# Cell Defaults
		self.m_gridValue.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_gridValue.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.m_gridValue, 0, wx.ALL, 5 )
		
		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Comment 1", wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer6.Add( self.m_staticText6, 1, wx.EXPAND|wx.TOP, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Comment 2", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer6.Add( self.m_staticText7, 1, wx.EXPAND|wx.TOP, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Comment 3", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer6.Add( self.m_staticText8, 1, wx.EXPAND|wx.TOP, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Comment 4", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer6.Add( self.m_staticText9, 1, wx.EXPAND|wx.TOP, 5 )
		
		
		bSizer51.Add( bSizer6, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrlComm1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,40 ), wx.TE_MULTILINE )
		self.m_textCtrlComm1.SetMaxLength( 256 ) 
		bSizer7.Add( self.m_textCtrlComm1, 0, wx.BOTTOM|wx.EXPAND, 5 )
		
		self.m_textCtrlComm2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,40 ), wx.TE_MULTILINE )
		self.m_textCtrlComm2.SetMaxLength( 256 ) 
		bSizer7.Add( self.m_textCtrlComm2, 0, wx.BOTTOM|wx.EXPAND, 5 )
		
		self.m_textCtrlComm3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,40 ), wx.TE_MULTILINE )
		self.m_textCtrlComm3.SetMaxLength( 256 ) 
		bSizer7.Add( self.m_textCtrlComm3, 0, wx.BOTTOM|wx.EXPAND, 5 )
		
		self.m_textCtrlComm4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,40 ), wx.TE_MULTILINE )
		self.m_textCtrlComm4.SetMaxLength( 256 ) 
		bSizer7.Add( self.m_textCtrlComm4, 0, wx.EXPAND, 5 )
		
		
		bSizer51.Add( bSizer7, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_buttonSaveComment = wx.Button( self, wx.ID_ANY, u"Save\nComment", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSaveComment.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer51.Add( self.m_buttonSaveComment, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer51, 0, wx.EXPAND, 5 )
		
		self.m_textLOG = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( 0,0 ), wx.Size( -1,-1 ), wx.TE_MULTILINE )
		self.m_textLOG.SetMinSize( wx.Size( -1,50 ) )
		
		bSizer8.Add( self.m_textLOG, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_buttonGET1.Bind( wx.EVT_BUTTON, self.onGetClick )
		self.m_buttonGET2.Bind( wx.EVT_BUTTON, self.onGetClick )
		self.m_buttonGET3.Bind( wx.EVT_BUTTON, self.onGetClick )
		self.m_buttonGET4.Bind( wx.EVT_BUTTON, self.onGetClick )
		self.m_gridValue.Bind( wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.onColumClick )
		self.m_buttonSaveComment.Bind( wx.EVT_BUTTON, self.onSaveCommentClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onGetClick( self, event ):
		event.Skip()
	
	
	
	
	def onColumClick( self, event ):
		event.Skip()
	
	def onSaveCommentClick( self, event ):
		event.Skip()
	

