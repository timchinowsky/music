import wx
import time
 
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
                        
def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


# Run the program
if __name__ == "__main__":
    #app = wx.PySimpleApp()
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()