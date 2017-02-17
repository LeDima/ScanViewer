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

from wxFormScavViewer import MainFrame

class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out=aWxTextCtrl
 
    def write(self,string):
        self.out.WriteText(string)

class MainClass(MainFrame):
    def __init__( self, parent ):
        MainFrame.__init__( self, parent )
#       self.OnTimer(None)
        self.timer = wx.Timer(self, -1)
        # update clock digits every second (1000ms)
        self.timer.Start(500)
        self.ser = self.open_serial_port('COM1')
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        #redir=RedirectText(self.m_textCtrl3)
        #sys.stdout=redir
        #self.Centre()
    
    def OnTimer(self, event):
        #print(3)
        #print(self.ser)
        try:
            data_to_send = self.write_serial_port(self.ser, "#01")
            print(type(data_to_send[0]))
            data_to_send = [float(data_to_send[i:i+7]) for i in range(56) if i%7==0]
            print(type(data_to_send[0]))
            with open('DataSave.txt', mode='w', encoding='utf-8') as f:
                json.dump(data_to_send, f, indent=2)
        except:
            data_to_send=[i for i in range(8)]
       
        print(type(data_to_send[0]))
        with open('DataSave.txt', 'r', encoding='utf-8') as f:
            entry = json.load(f) 
        print(entry)
        #print(type(data_to_send))
        #print(data_to_send[0])
        #print(4)
        # get current time from computer
        #print(type(self.ser))
       
        # time string can have characters 0..9, -, period, or space
        #self.m_textCtrl3.SetValue(str(sys.stdout))
        if data_to_send[0]> 0:
            self.m_textCtrl1.SetBackgroundColour(wx.RED)
        
        self.m_textCtrl1.SetValue(str(data_to_send[0]))

    def open_serial_port(self,serial_name):
        try:
            s = serial.Serial(serial_name, 9600)
            s.timeout = .01;  # Timeout: 20 ms
        except serial.SerialException:
            sys.stderr.write("Error opening the port {}".format(serial_name))
            sys.exit(1)
        print('Serial port connected')
        return s

    def write_serial_port(self,s, cmd):
        data = b""
        print(3)
        #print(cmd.encode("iso-8859-15"))
        CRC = format(sum([ord(ss) for ss in cmd]),'02X')
        #print(CRC.encode("iso-8859-15"))
        #print(CRC.encode("iso-8859-15"))
        #print(cmd)
        
        #i=0
        while b"\r" not in data:
            cmd = cmd.encode("iso-8859-15") + CRC.encode("iso-8859-15") + b"\r"
            s.write(cmd)
            data += s.read(60)
        #    print(data)
        #    i+=1
        #   if i>=2:
        #        data="-100"
        #        break
        #print(data)
        #CRC2= format(sum([ord(ss) for ss in data[:-3].decode("iso-8859-15")]),'02X')[-2:]
        #print(CRC2)
        #if data[-3:-1] == format(sum([ord(ss) for ss in data[:-3]]),'02X')[-2:]:
        if data[-3:-1].decode("iso-8859-15") == format(sum([ord(ss) for ss in data[:-3].decode("iso-8859-15")]),'02X')[-2:]:
            data=data[1:-3].decode("iso-8859-15")
        #    print(4)
        else:
            data=None
        #print(data)
        return data




            
if __name__ == "__main__":	
    app = wx.App()
    wnd = MainClass(None)
    print(1)
    wnd.Show(True)
    print(2)
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
