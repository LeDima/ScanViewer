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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1300,729 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )
		
		self.m_button1 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl1.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		
		sbSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_gridValue = wx.grid.Grid( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_gridValue.CreateGrid( 8, 7 )
		self.m_gridValue.EnableEditing( True )
		self.m_gridValue.EnableGridLines( True )
		self.m_gridValue.EnableDragGridSize( False )
		self.m_gridValue.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridValue.SetColSize( 0, 72 )
		self.m_gridValue.SetColSize( 1, 52 )
		self.m_gridValue.SetColSize( 2, 106 )
		self.m_gridValue.SetColSize( 3, 80 )
		self.m_gridValue.SetColSize( 4, 80 )
		self.m_gridValue.SetColSize( 5, 80 )
		self.m_gridValue.SetColSize( 6, 80 )
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
		sbSizer1.Add( self.m_gridValue, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_gridComment = wx.grid.Grid( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
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
		self.m_gridComment.EnableDragRowSize( True )
		self.m_gridComment.SetRowLabelSize( 0 )
		self.m_gridComment.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_gridComment.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		sbSizer1.Add( self.m_gridComment, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textLOG = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.Point( 0,0 ), wx.Size( -1,-1 ), wx.TE_MULTILINE )
		self.m_textLOG.SetMinSize( wx.Size( -1,150 ) )
		
		sbSizer1.Add( self.m_textLOG, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		self.SetSizer( sbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

