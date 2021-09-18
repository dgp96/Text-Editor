import wx
import wx.lib.dialogs
import wx.stc as stc

faces={
	'times':'Times New Roman',
	'mono':'Courier New',
	'helv':'Arial',
	'other':'Comic Sans MS',
	'size':10,
	'size2':8,

}

class MainWindow(wx.Frame):
	def __init__(self,parent,title):   #title is the heading of the text editor,__init__ is a default constructor which gets instantiated without calling it
		self.leftMarginWidth=25

		wx.Frame.__init__(self,parent,title=title,size=(800,600)) #initialises the frame with the parameters of __init__
		self.control=stc.StyledTextCtrl(self,style=wx.TE_MULTILINE | wx.TE_WORDWRAP)
		self.control.CmdKeyAssign(ord('='),stc.STC_SCMOD_CTRL,stc.STC_CMD_ZOOMIN) #Ctrl + is zoom in 
		self.control.CmdKeyAssign(ord('-'),stc.STC_SCMOD_CTRL,stc.STC_CMD_ZOOMOUT) #Ctrl - is zoom out
		
		self.control.SetViewWhiteSpace(False)
		self.control.SetMargins(5,0)#left margin of numbering the lines ka width
		self.control.SetMarginType(1,stc.STC_MARGIN_NUMBER)
		self.control.SetMarginWidth(1,self.leftMarginWidth)#left margin of numbering the lines ka width

		self.CreateStatusBar()
		self.StatusBar.SetBackgroundColour((220,220,220))

		filemenu=wx.Menu()
		menuNew=filemenu.Append(wx.ID_NEW,"&New","Create a new Document")
		menuOpen=filemenu.Append(wx.ID_OPEN,"&Open","Open an existing Document")
		menuSave=filemenu.Append(wx.ID_NEW,"&Save","Save the current Document")
		menuSaveAs=filemenu.Append(wx.ID_NEW,"Save &As","Save a new Document")
		#filemenu.AppendSeperator()
		menuNew=filemenu.Append(wx.ID_NEW,"&New","Create a new Document")

		editmenu=wx.Menu()
		menuUndo=editmenu.Append(wx.ID_UNDO,"&Undo","Undo last action")
		menuRedo=editmenu.Append(wx.ID_REDO,"&New","Redo last action")
		#editmenu.AppendSeperator()
		menuSelectAll=editmenu.Append(wx.ID_SELECTALL,"&Select All","Select Entire Document")
		menuCopy=editmenu.Append(wx.ID_COPY,"&Copy","Copy Selected Text")
		menuCut=editmenu.Append(wx.ID_CUT,"&New","Cut selected text")
		menuPaste=editmenu.Append(wx.ID_PASTE,"&New","Paste from Clipboard")

		prefmenu=wx.Menu()
		menuNew=prefmenu.Append(wx.ID_ANY,"Toggle &Line Numbers","Show/hide line numbers column")

		helpmenu=wx.Menu()
		menuNew=helpmenu.Append(wx.ID_ANY,"&How to...","Get help using the editor")
		#helpmenu.AppendSeperator()
		menuNew=helpmenu.Append(wx.ID_NEW,"&About","Read About the editor")
		
		menuBar=wx.MenuBar()
		menuBar.Append(filemenu,"&File")
		menuBar.Append(editmenu,"&Edit")
		menuBar.Append(prefmenu,"&Preferences")
		menuBar.Append(helpmenu,"&Help")
		self.SetMenuBar(menuBar)

		self.Show()

	def OnNew(self,e):
		self.filename=''
		self.control.SetValue("")

	def OnOpen(self,e):
		try:
			dlg=wx.FileDialog(self,"Choose a file",self.dirname,"","*.*",wx.FD_OPEN)
			if(dlg.ShowModal()==wx.ID_OK)
			   self.filename=dlg.GetFilename()
			   self.dirname=dlg.GetDirectory()
			   




app= wx.App()
frame= MainWindow(None,"My Text Editor")	    
app.MainLoop()