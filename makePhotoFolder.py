import wx
import pathlib

basepath = pathlib.Path("P:/")

def makePhotoFolder(folderName, namedSubfolders=True):
    uneditedFolder = basepath / folderName / "unbearbeitet"
    uneditedFolder.mkdir(parents=True)
    if namedSubfolders:
        SteffiFolder = uneditedFolder / "Steffi"
        SteffiFolder.mkdir(parents=True)
        ThomasFolder = uneditedFolder / "Thomas"
        ThomasFolder.mkdir(parents=True)

class makePhotoFolderUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 500))

        self.sizerMain = wx.BoxSizer(wx.VERTICAL)

        self.sizerName = wx.BoxSizer(wx.HORIZONTAL)
        self.inputName = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.stateName = wx.StaticText(self, label="Namen eingeben")
        self.sizerName.Add(self.inputName, 1, wx.ALL | wx.EXPAND, 5)
        self.sizerName.Add(self.stateName, 0, wx.ALL | wx.EXPAND, 5)
        self.sizerMain.Add(self.sizerName, 0, wx.ALL | wx.EXPAND, 5)

        self.checkSubFolder = wx.CheckBox(self, label="Steffi/Thomas Unterordner")
        self.checkSubFolder.SetValue(True)
        self.sizerMain.Add(self.checkSubFolder, 0, wx.ALL | wx.EXPAND, 5)

        self.buttonLos = wx.Button(self, label="Ordner erzeugen")
        self.sizerMain.Add(self.buttonLos, 0, wx.ALL | wx.EXPAND, 5)

        self.Bind(wx.EVT_TEXT, self.checkPath, self.inputName)
        self.Bind(wx.EVT_TEXT_ENTER, self.makePath, self.inputName)
        self.Bind(wx.EVT_BUTTON, self.makePath, self.buttonLos)

        self.SetSizer(self.sizerMain)
        self.Fit()
        self.Show()
    
    def checkPath(self, event):
        if event.String:
            newPath = basepath / event.String
            if newPath.exists():
                self.stateName.SetLabel("Pfad existiert")
                self.stateName.SetBackgroundColour(wx.RED)
            else:
                self.stateName.SetLabel("Pfad OK")
                self.stateName.SetBackgroundColour(self.GetBackgroundColour())
        else:
            self.stateName.SetLabel("Namen eingeben")
            self.stateName.SetBackgroundColour(self.GetBackgroundColour())
    
    def makePath(self, event):
        makePhotoFolder(self.inputName.GetValue(), self.checkSubFolder.GetValue())
        self.inputName.SetValue("")

app = wx.App()
frame = makePhotoFolderUI(None, "Photoordner erzeugen")
app.MainLoop()
