# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 09:43:39 2017

@author: Dima
"""


import wx
import wx.xrc
import wx.grid
import serial
import sys
import json

from wxFormScavViewerV2 import MainFrame

class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out=aWxTextCtrl
 
    def write(self,string):
        self.out.WriteText(string)

class MainClass(MainFrame):
    def __init__( self, parent ):
        MainFrame.__init__( self, parent )
        
        self.bSizer3.AddSpacer(  40  )
        
        #image_file = 'Schem.JPG'
        #bmp1 = wx.Image(image_file,wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            # image's upper left corner anchors at panel 
            # coordinates (0, 0)
        #self.m_bitmap1(self, -1, bmp1,(0,0), (100,100))
        #self.bitmap1 = wx.StaticBitmap(self, -1, bmp1,(0,0), (100,100))
            # show some image details
        #str1 = "%s  %dx%d" % (image_file, bmp1.GetWidth(),bmp1.GetHeight()) 


        #redir=RedirectText(self.m_textLOG)   # Redirect print() to m_textLOG 
        #sys.stdout=redir
        
        
        for i in range(4):
            setval=["SET 1","SET 2","SET 3","SET 4"]
            self.m_gridComment.SetCellAlignment(wx.ALIGN_CENTRE,i,0)
            self.m_gridComment.SetCellValue(i,0,setval[i])
            self.m_gridComment.SetReadOnly(i,0)
            self.m_gridComment.SetCellFont(i,0, wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
            #self.m_gridComment.SetCellValue(i,1,self.MainDict['Comment'][i])
        for i in range(8):
            if i%2==0:
                self.m_gridValue.SetCellSize(i,0,2,1)
            setval=["1","1","2","2","3","3","4","4"]
            setval2=["X","Y","X","Y","X","Y","X","Y"]
            self.m_gridValue.SetCellValue(i,0,setval[i])
            self.m_gridValue.SetCellValue(i,1,setval2[i])
            self.m_gridValue.SetCellAlignment(wx.ALIGN_CENTRE,i,0)
            self.m_gridValue.SetCellAlignment(wx.ALIGN_CENTRE,i,1)
            for j in range(7): 
                self.m_gridValue.SetReadOnly(i,j)            
            self.m_gridValue.SetCellFont(i,0, wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
            self.m_gridValue.SetCellFont(i,1, wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        
        try:
            with open('ConfigandDate.txt', 'r', encoding='utf-8') as f:
                self.MainDict = json.load(f) 
        except (OSError, IOError):
            self.NewMainDict={'SerialName':'COM1'
                              ,'SerialSpeed':9600
                              ,'SerialTimeout':.1
                              ,'PeriodDate':500
                              ,'ICPCONAdres':'01'
                              ,'BeamDate':[[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001]
                                          ,[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001]
                                          ,[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001]
                                          ,[0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001]]
                              ,'Comment':['Comment 1','Comment 2','Comment 3','Comment 4']
                             }
            with open('ConfigandDate.txt', mode='w', encoding='utf-8') as f:
                    json.dump(self.NewMainDict, f, indent=2)
            with open('ConfigandDate.txt', 'r', encoding='utf-8') as f:
                self.MainDict = json.load(f)
        f.close()
        self.timer = wx.Timer(self, -1)
        self.timer.Start(self.MainDict['PeriodDate'])   # update clock digits every second ('PeriodDate' ms)
        self.ser = self.open_serial_port(self.MainDict['SerialName'])
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.m_gridValue.Bind( wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.onColumClick)
        #self.m_gridValue.Bind
        
    def onColumClick(self, event):
        self.timer.Stop()
        #print ("on select range")#, self.m_gridValue.GetCol())#, evt.GetTopLeftCoords(), evt.GetBottomRightCoords()        
        row = event.GetCol()
        dlg = wx.MessageDialog(None, "Do you want save new value in SET" + str(row-2) + "?" 
                               ,"Save new position"
                               ,wx.YES_NO)
        if (dlg.ShowModal() == wx.ID_YES):
            print("Yes")
            for i in range(8):
                self.MainDict['BeamDate'][row-3][i]= self.dataFloat[i]
        else:
            print("No")
           
        with open('ConfigandDate.txt', mode='w', encoding='utf-8') as f:
                    json.dump(self.MainDict, f, indent=2)
        f.close()       
        
        dlg.Destroy()
        self.timer.Start(self.MainDict['PeriodDate']) 
        
           
            
        
        
        
        #self.m_gridComment.SetCellSize(1,1,2,1)
        #self.m_gridComment.SetCellValue(3,1,'SDFSDF')
        
        
        #self.Centre()
        
    def SaveDate(self):
        pass
    
    def OnTimer(self, event):
        #print(3)
        #print(self.ser)
#        try:
        self.data_to_send = self.write_serial_port(self.ser, "#"+self.MainDict['ICPCONAdres'])
        self.dataStr = [str(self.data_to_send[i:i+7]) for i in range(56) if i%7==0]
        self.dataFloat =[float(self.data_to_send[i:i+7]) for i in range(56) if i%7==0]
#        except:
#            self.dataFloat = [i*1.0 for i in range(8)]
#            self.dataStr = [str(i*1.0) for i in range(8)]
#        
        for i in range(8):
            self.m_gridValue.SetCellValue(i,2,self.dataStr[i])
            for j in range(4):
                self.m_gridValue.SetCellValue(i,j+3,format(self.MainDict['BeamDate'][j][i], '+.04f'))
            
        
        print(self.dataFloat)
#        with open('DataSave.txt', 'r', encoding='utf-8') as f:
#            entry = json.load(f) 
#        print(entry)
        #print(type(data_to_send))
        #print(data_to_send[0])
        #print(4)
        # get current time from computer
        #print(type(self.ser))
       
        # time string can have characters 0..9, -, period, or space
        #self.m_textCtrl3.SetValue(str(sys.stdout))
#        if data_to_send[0]> 0:
#            self.m_textCtrl1.SetBackgroundColour(wx.RED)
#        
#        self.m_textCtrl1.SetValue(str(data_to_send[0]))

    def open_serial_port(self,serial_name):
        try:
            s = serial.Serial(serial_name, self.MainDict['SerialSpeed'])
            s.timeout = self.MainDict['SerialTimeout']; 
        except serial.SerialException:
            sys.stderr.write("Error opening the port {}".format(serial_name))
            sys.exit(1)
        print('Serial port connected')
        return s

    def write_serial_port(self,s, cmd="#01"):
        data = b""
        CRC = format(sum([ord(ss) for ss in cmd]),'02X')
        cmd1 =  cmd.encode("iso-8859-15") + CRC.encode("iso-8859-15") + b"\r"
        print(cmd1)
        i=0
        while b"\r" not in data:
            s.write(cmd1)
            data += s.read(60)
            s.flushInput()
            i+=1
            if i>=2:
                print("Error connected device")
                break
        print(data)
        if data[-3:-1].decode("iso-8859-15") == format(sum([ord(ss) for ss in data[:-3].decode("iso-8859-15")]),'02X')[-2:]:
            data=data[1:-3].decode("iso-8859-15")
        else:
            if i<2:
                print("Error CRC ")
            data='+0.0000+0.0000+0.0000+0.0000+0.0000+0.0000+0.0000+0.0000'
                      
#        print(data)
        return data




            
if __name__ == "__main__":	
    app = wx.App()
    wnd = MainClass(None)
    #print(1)
    wnd.Show(True)
    #print(2)
#    i=0
#    while i < 10:
#        i+=1
#        wx.Sleep(1)
#        wnd.Upgrade()
    try:
        app.MainLoop()
    except Exception:
        print("Error opening the port {}")
        exit()
