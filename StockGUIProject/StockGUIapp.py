import wx
import shutil
from utils.StockCrawler import Crawler

class StockGUI():
    def __init__(self):
        self.bmps_dict = {}
        self.isexist = False
        self.Crawler = Crawler()

        # Setup base frame
        self.frame = wx.Frame(parent = None, title="STOCK GUI")
        self.frame.SetSize(500, 500, 500, 500)
        self.panel = wx.Panel(parent = self.frame, id = wx.ID_ANY)
        
        # Set the stock label
        self.font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.stocks = wx.StaticText(parent = self.panel,
                                    label = "YOUR STOCKS : " + str(self.Crawler.stocks),
                                    pos = (10, 45))
        self.stocks.SetFont(self.font)

        # Set the message label
        self.message = wx.StaticText(parent=self.panel,
                                     label="MESSAGE : No Message",
                                     pos=(10, 60))
        self.message.SetFont(self.font)

        # Set buttons
        button = wx.Button(parent = self.panel, label = "INPUT", pos = (10, 10))
        button.Bind(wx.EVT_BUTTON, self.Input)
        button = wx.Button(parent = self.panel, label = "REMOVE", pos = (100, 10))
        button.Bind(wx.EVT_BUTTON, self.Remove)
        button = wx.Button(parent = self.panel, label = "REFRESH", pos = (190, 10))
        button.Bind(wx.EVT_BUTTON, self.Refresh)
        button = wx.Button(parent = self.panel, label = "HIDE", pos = (280, 10))
        button.Bind(wx.EVT_BUTTON, self.Hide)
        button = wx.Button(parent = self.panel, label = "CLOSE", pos = (370, 10))
        button.Bind(wx.EVT_BUTTON, self.Close)

        # Show the frame
        self.frame.Show()
        self.frame.Centre()

    def Input(self, event):
        # Popup a text box
        text_box = wx.TextEntryDialog(parent = None, message = "Please Input the Stock Code")
        text_box.ShowModal()
        stock_code = text_box.GetValue()
        msg = self.Crawler.addStock(stock_code)
        # Refresh the message label
        self.message.SetLabel(label = f"MESSAGE : {msg}")
        # Refresh the stocks label
        self.stocks.SetLabel(label = "YOUR STOCKS : " + str(self.Crawler.stocks))
        text_box.Destroy()

    def Remove(self, event):
        # Popup a text box
        text_box = wx.TextEntryDialog(parent = None, message = "Please Input the Stock Code")
        text_box.ShowModal()
        stock_code = text_box.GetValue()
        if stock_code in self.Crawler.stocks:
            msg = self.Crawler.delStock(stock_code)
            # Refresh the message label
            self.message.SetLabel(label = f"MESSAGE : {msg}")
        else:
            # Refresh the message label
            self.message.SetLabel(label = "MESSAGE : Stock Code Is Not In Your List")
        # Refresh the stocks label
        self.stocks.SetLabel(label = "YOUR STOCKS : " + str(self.Crawler.stocks))
        text_box.Destroy()

    def Refresh(self, event):
        try:
            self.Crawler.loadImage()
            # Set the interval between images
            interval = 80
            for i in range(0, len(self.Crawler.stocks)):
                # wx.image responsible for image processing like crop, scale, etc.
                image = wx.Image("stock_screenshot/" + self.Crawler.stocks[i] + ".png", wx.BITMAP_TYPE_PNG)
                image = image.GetSubImage(wx.Rect(170, 5, 1115, 185))
                image = image.Scale(450, 80, wx.IMAGE_QUALITY_HIGH)
                # wx.Bitmap responsible for image present
                bitmap = image.ConvertToBitmap()
                if self.Crawler.stocks[i] not in self.bmps_dict:
                    self.bmps_dict[self.Crawler.stocks[i]] = wx.StaticBitmap(parent = self.frame,
                                                                             bitmap = bitmap,
                                                                             pos = (5, interval),
                                                                             size = (10, 10))
                self.bmps_dict[self.Crawler.stocks[i]].SetBitmap(bitmap)
                interval += 85

            self.isexist = True
            # Refresh the message label
            self.message.SetLabel(label = "MESSAGE : Refresh Stocks")

        except Exception as msg:
            # Refresh the message label
            self.message.SetLabel(label = f"MESSAGE : {msg}")

    def Hide(self, event):
        if self.isexist:
            # Refresh the message label
            self.message.SetLabel(label = f"MESSAGE : Hide Stocks Images")
            # Destroy and remove Bitmap objects
            while self.bmps_dict:
                stock_code, bmp = list(self.bmps_dict.items())[-1]
                bmp.Destroy()
                self.bmps_dict.pop(stock_code)
            self.isexist = False
        else:
            # Refresh the message label
            self.message.SetLabel(label = f"MESSAGE : Stock Images Are Not Exist")

    def Close(self, event):
        # Remove screenshot directory
        shutil.rmtree("stock_screenshot/", ignore_errors = True)
        # Close the web driver
        self.Crawler.close()
        # Destroy the base frame
        self.frame.Destroy()

if __name__ == "__main__":
    # Create an application object
    app = wx.App()
    StockGUI()
    # Start the event loop
    app.MainLoop()