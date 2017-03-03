# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 09:43:39 2017

@author: LeDima
"""
import wx
#import wx.xrc
#import wx.grid
import serial
import sys
import json

from wxFormScavViewer import MainFrame

class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out=aWxTextCtrl
 
    def write(self,string):
        self.out.WriteText(string)

class MainClass(MainFrame):
    def __init__( self, parent ):
        MainFrame.__init__( self, parent )
        
        redir=RedirectText(self.m_textLOG)   # Redirect print() to m_textLOG 
        sys.stdout=redir
        
        self.ValueDate=[self.m_textCtrlGUN1X,
                        self.m_textCtrlGUN1Y,
                        self.m_textCtrlGUN2X,
                        self.m_textCtrlGUN2Y,
                        self.m_textCtrlGUN3X,
                        self.m_textCtrlGUN3Y,
                        self.m_textCtrlGUN4X,
                        self.m_textCtrlGUN4Y]
        self.ButtonGET=[self.m_buttonGET1,
                        self.m_buttonGET2,
                        self.m_buttonGET3,
                        self.m_buttonGET4]

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
            for j in range(5):
                self.m_gridValue.SetCellFont(i,j+2,wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ))
            self.m_gridValue.SetCellFont(i,0, wx.Font( wx.NORMAL_FONT.GetPointSize()+5, 70, 90, 92, False, wx.EmptyString ) )
            self.m_gridValue.SetCellFont(i,1, wx.Font( wx.NORMAL_FONT.GetPointSize()+3, 70, 90, 92, False, wx.EmptyString ) )
              
        try:
            with open('ConfigandDate.txt', 'r', encoding='utf-8') as f:
                self.MainDict = json.load(f) 
        except (OSError, IOError):
            self.NewMainDict={'SerialName':'COM1'
                              ,'SerialSpeed':9600
                              ,'SerialTimeout':.1
                              ,'PeriodDate':500
                              ,'ICPCONAdres':'01'
                              ,'BeamDate':[[0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]
                                          ,[0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]
                                          ,[0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]
                                          ,[0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]]
                              ,'Comment':['Comment 1','Comment 2','Comment 3','Comment 4']
                              ,'Precision':[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
                              ,'SetValue':1
                             }
            with open('ConfigandDate.txt', mode='w', encoding='utf-8') as f:
                    json.dump(self.NewMainDict, f, indent=2)
            with open('ConfigandDate.txt', 'r', encoding='utf-8') as f:
                self.MainDict = json.load(f)
        f.close()
        
        #self.m_buttonGET1.SetBackgroundColour
        
        self.ser = self.open_serial_port(self.MainDict['SerialName'])
        
        self.timer = wx.Timer(self, -1)
        self.timer.Start(self.MainDict['PeriodDate'])   # update clock digits every second ('PeriodDate' ms)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        
        self.m_textCtrlComm1.SetValue(self.MainDict['Comment'][0])
        self.m_textCtrlComm2.SetValue(self.MainDict['Comment'][1])
        self.m_textCtrlComm3.SetValue(self.MainDict['Comment'][2])
        self.m_textCtrlComm4.SetValue(self.MainDict['Comment'][3])
        
       
        for i in range(8):
            for j in range(4):
                self.m_gridValue.SetCellValue(i,j+3,format(self.MainDict['BeamDate'][j][i], '+.03f'))
        
        self.ButtonGET[self.MainDict['SetValue']-1].SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
        
        self.SetValuePre=self.MainDict['SetValue']
        for i in range(8):
                self.m_gridValue.SetCellBackgroundColour(i,self.SetValuePre+2,wx.LIGHT_GREY)
        
    def OnTimer(self, event):
 
        self.data_to_send = self.write_serial_port(self.ser, "#"+self.MainDict['ICPCONAdres'])
        self.dataFloat =[float(self.data_to_send[i:i+7]) for i in range(56) if i%7==0]
        
        for i in range(8):
            self.m_gridValue.SetCellValue(i,2,format(self.dataFloat[i], '+.03f'))
       
        #print(self.dataFloat)
        for i in range(8):
            DiffValues = self.dataFloat[i]-self.MainDict['BeamDate'][self.MainDict['SetValue']-1][i]
            #if dataFloat[i]<=self.MainDict['ICPCONAdres']
            if DiffValues<-self.MainDict['Precision'][i]:
                self.ValueDate[i].SetBackgroundColour(wx.GREEN)
            elif DiffValues>self.MainDict['Precision'][i]:
                self.ValueDate[i].SetBackgroundColour(wx.RED)
            else:
                self.ValueDate[i].SetBackgroundColour(wx.YELLOW)
                            
            if i%2==0:
                self.ValueDate[i].SetValue("X="+format(DiffValues, '+.03f'))
            else:
                self.ValueDate[i].SetValue("Y="+format(DiffValues, '+.03f'))
        
        
    def onSaveCommentClick( self, event ):
        self.MainDict['Comment'][0]= self.m_textCtrlComm1.GetValue()
        self.MainDict['Comment'][1]= self.m_textCtrlComm2.GetValue()
        self.MainDict['Comment'][2]= self.m_textCtrlComm3.GetValue()
        self.MainDict['Comment'][3]= self.m_textCtrlComm4.GetValue()
        
        self.SaveDate()
            
    def onGetClick( self, event ):
        self.timer.Stop()
        row = event.GetId()
        dlg = wx.MessageDialog(None, "Do you want read SET" + str(row-999) + " value ?" 
                               ,"Read new value"
                               ,wx.YES_NO)
        if (dlg.ShowModal() == wx.ID_YES):
            self.SetValueNow=row-999
            self.MainDict['SetValue']=self.SetValueNow
            
            self.ButtonGET[self.SetValueNow-1].SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
            self.ButtonGET[self.SetValuePre-1].SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
            
            for i in range(8):
                self.m_gridValue.SetCellBackgroundColour(i,self.SetValueNow+2,wx.LIGHT_GREY)
                self.m_gridValue.SetCellBackgroundColour(i,self.SetValuePre+2,wx.WHITE)
            
            self.SetValuePre=self.SetValueNow
           
        self.SaveDate()    
        
        dlg.Destroy()
        self.timer.Start(self.MainDict['PeriodDate']) 

        
    def onColumClick(self, event):
        self.timer.Stop()
        
        row = event.GetCol()
        dlg = wx.MessageDialog(None, "Do you want save new value in SET" + str(row-2) + "?" 
                               ,"Save new position"
                               ,wx.YES_NO)
        if (dlg.ShowModal() == wx.ID_YES):
            for i in range(8):
                self.MainDict['BeamDate'][row-3][i]= self.dataFloat[i]
        self.SaveDate()

        dlg.Destroy()
        
        for i in range(8):
            for j in range(4):
                self.m_gridValue.SetCellValue(i,j+3,format(self.MainDict['BeamDate'][j][i], '+.03f'))
        
        self.timer.Start(self.MainDict['PeriodDate']) 
        
           
    def SaveDate(self):
        with open('ConfigandDate.txt', mode='w', encoding='utf-8') as f:
            json.dump(self.MainDict, f, indent=2)
        f.close()  

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
        #print(cmd1)
        i=0
        while b"\r" not in data:
            s.write(cmd1)
            data += s.read(60)
            s.flushInput()
            i+=1
            if i>=2:
                print("Error connected device")
                break
            else:
                print(data)
        
        if data[-3:-1].decode("iso-8859-15") == format(sum([ord(ss) for ss in data[:-3].decode("iso-8859-15")]),'02X')[-2:]:
            data=data[1:-3].decode("iso-8859-15")
        else:
            if i<2:
                print("Error CRC ")
            data='+0.0000+0.0000+0.0000+0.0000+0.0000+0.0000+0.0000+0.0000'
                      
        return data
           
if __name__ == "__main__":	
    app = wx.App()
    wnd = MainClass(None)
    wnd.Show(True)
    try:
        app.MainLoop()
    except Exception:
        print("Error opening the port {}")
        exit()
