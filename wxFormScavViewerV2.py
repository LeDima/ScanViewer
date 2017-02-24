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

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ScanViewer", pos = wx.DefaultPosition, size = wx.Size( 649,757 ), style = wx.DEFAULT_FRAME_STYLE|wx.SIMPLE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 4, 0, 0 )
		
		gSizer1.SetMinSize( wx.Size( 1,1 ) ) 
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3.SetMinSize( wx.Size( 10,10 ) ) 
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )
		
		self.m_textCtrl5 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		sbSizer2.Add( self.m_textCtrl5, 0, 0, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		sbSizer2.Add( self.m_textCtrl4, 0, 0, 5 )
		
		
		bSizer3.Add( sbSizer2, 1, 0, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )
		
		self.m_textCtrl3 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		sbSizer3.Add( self.m_textCtrl3, 0, 0, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		sbSizer3.Add( self.m_textCtrl2, 0, 0, 5 )
		
		
		bSizer3.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		
		gSizer1.Add( bSizer3, 1, wx.ALIGN_RIGHT, 5 )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Schem.bmp", wx.BITMAP_TYPE_ANY ), wx.Point( 0,0 ), wx.Size( 20,100 ), 0 )
		gSizer1.Add( self.m_bitmap1, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer31.SetMinSize( wx.Size( 10,10 ) ) 
		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )
		
		self.m_textCtrl51 = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		sbSizer21.Add( self.m_textCtrl51, 0, 0, 5 )
		
		self.m_textCtrl41 = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		sbSizer21.Add( self.m_textCtrl41, 0, 0, 5 )
		
		
		bSizer31.Add( sbSizer21, 1, 0, 5 )
		
		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )
		
		self.m_textCtrl31 = wx.TextCtrl( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		sbSizer31.Add( self.m_textCtrl31, 0, 0, 5 )
		
		self.m_textCtrl21 = wx.TextCtrl( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		sbSizer31.Add( self.m_textCtrl21, 0, 0, 5 )
		
		
		bSizer31.Add( sbSizer31, 1, wx.EXPAND, 5 )
		
		
		gSizer1.Add( bSizer31, 1, 0, 5 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1.SetMinSize( wx.Size( 1,1 ) ) 
		self.m_buttonGET1 = wx.Button( self, wx.ID_ANY, u"GET1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_buttonGET1, 0, wx.ALL, 5 )
		
		self.m_buttonGET2 = wx.Button( self, wx.ID_ANY, u"GET2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_buttonGET2, 0, wx.ALL, 5 )
		
		self.m_buttonGET3 = wx.Button( self, wx.ID_ANY, u"GET3", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_buttonGET3, 0, wx.ALL, 5 )
		
		self.m_buttonGET4 = wx.Button( self, wx.ID_ANY, u"GET4", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_buttonGET4, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer1, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer8.Add( gSizer1, 1, 0, 5 )
		
		self.m_gridValue = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_gridValue.CreateGrid( 8, 7 )
		self.m_gridValue.EnableEditing( True )
		self.m_gridValue.EnableGridLines( True )
		self.m_gridValue.EnableDragGridSize( False )
		self.m_gridValue.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridValue.SetColSize( 0, 72 )
		self.m_gridValue.SetColSize( 1, 52 )
		self.m_gridValue.SetColSize( 2, 90 )
		self.m_gridValue.SetColSize( 3, 60 )
		self.m_gridValue.SetColSize( 4, 60 )
		self.m_gridValue.SetColSize( 5, 60 )
		self.m_gridValue.SetColSize( 6, 60 )
		self.m_gridValue.EnableDragColMove( False )
		self.m_gridValue.EnableDragColSize( True )
		self.m_gridValue.SetColLabelSize( 30 )
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
		self.m_gridValue.SetLabelFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		# Cell Defaults
		self.m_gridValue.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer8.Add( self.m_gridValue, 0, wx.ALL, 5 )
		
		self.m_gridComment = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_gridComment.CreateGrid( 4, 2 )
		self.m_gridComment.EnableEditing( True )
		self.m_gridComment.EnableGridLines( True )
		self.m_gridComment.EnableDragGridSize( False )
		self.m_gridComment.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridComment.SetColSize( 0, 50 )
		self.m_gridComment.SetColSize( 1, 550 )
		self.m_gridComment.EnableDragColMove( False )
		self.m_gridComment.EnableDragColSize( True )
		self.m_gridComment.SetColLabelSize( 30 )
		self.m_gridComment.SetColLabelValue( 0, u"SET" )
		self.m_gridComment.SetColLabelValue( 1, u"Comment" )
		self.m_gridComment.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_gridComment.SetRowSize( 0, 30 )
		self.m_gridComment.SetRowSize( 1, 30 )
		self.m_gridComment.SetRowSize( 2, 30 )
		self.m_gridComment.SetRowSize( 3, 30 )
		self.m_gridComment.AutoSizeRows()
		self.m_gridComment.EnableDragRowSize( True )
		self.m_gridComment.SetRowLabelSize( 0 )
		self.m_gridComment.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_gridComment.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer8.Add( self.m_gridComment, 0, wx.ALL, 5 )
		
		self.m_textLOG = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( 0,0 ), wx.Size( -1,-1 ), wx.TE_MULTILINE )
		self.m_textLOG.SetMinSize( wx.Size( -1,100 ) )
		
		bSizer8.Add( self.m_textLOG, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

