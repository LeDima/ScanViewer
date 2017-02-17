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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1300,729 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.File = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.File, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.AppendItem( self.m_menuItem1 )
		
		self.m_menubar1.Append( self.File, u"File" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )
		
		sbSizer1.SetMinSize( wx.Size( 400,600 ) ) 
		self.m_button1 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl1.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		
		sbSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.Point( 300,200 ), wx.Size( 400,200 ), wx.TE_MULTILINE )
		self.m_textCtrl3.SetMinSize( wx.Size( 400,200 ) )
		
		sbSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		
		self.SetSizer( sbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.fileopen, id = self.m_menuItem1.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def fileopen( self, event ):
		event.Skip()
	

