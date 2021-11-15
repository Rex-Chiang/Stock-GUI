import wx
from utils.StockCrawler import Crawler

class StockGUI():
    def __init__(self):
        self.bmps_dict = {}
        self.isexist = False
        self.Crawler = Crawler()
        self.frame = wx.Frame(parent = None, title="STOCK GUI")
        self.frame.SetSize(500, 500, 500, 500)
        self.panel = wx.Panel(parent = self.frame, id = wx.ID_ANY)

        self.font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.stocks = wx.StaticText(parent = self.panel,
                                    label = "YOUR STOCKS : " + str(self.Crawler.stocks),
                                    pos = (10, 45))

        self.stocks.SetFont(self.font)

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
        text_box = wx.TextEntryDialog(parent = None, message = "Please Input the Stock Code")
        text_box.ShowModal()
        stock_code = text_box.GetValue()
        self.Crawler.addStock(stock_code)

        self.stocks.Destroy()
        self.stocks = wx.StaticText(parent=self.panel,
                                    label="YOUR STOCKS : " + str(self.Crawler.stocks),
                                    style=wx.FONTSTYLE_ITALIC,
                                    pos=(10, 45))

        self.stocks.SetFont(self.font)

        text_box.Destroy()

    def Remove(self, event):
        text_box = wx.TextEntryDialog(parent = None, message = "Please Input the Stock Code")
        text_box.ShowModal()
        stock_code = text_box.GetValue()
        self.Crawler.delStock(stock_code)

        self.stocks.Destroy()
        self.stocks = wx.StaticText(parent=self.panel,
                                    label="YOUR STOCKS : " + str(self.Crawler.stocks),
                                    style=wx.FONTSTYLE_ITALIC,
                                    pos=(10, 45))

        self.stocks.SetFont(self.font)

        text_box.Destroy()

    def Refresh(self, event):
        try:
            self.Crawler.loadImage()
            interval = 65
            for i in range(0, len(self.Crawler.stocks)):
                # wx.image responsible for image processing like crop, scale, etc.
                image = wx.Image("stock_screenshot/" + self.Crawler.stocks[i] + ".png", wx.BITMAP_TYPE_PNG)
                image = image.GetSubImage(wx.Rect(170, 5, 1115, 100))
                image = image.Scale(450, 40, wx.IMAGE_QUALITY_HIGH)
                # wx.Bitmap responsible for image present
                bitmap = image.ConvertToBitmap()
                if self.Crawler.stocks[i] not in self.bmps_dict:
                    self.bmps_dict[self.Crawler.stocks[i]] = wx.StaticBitmap(parent = self.frame,
                                                                             bitmap = bitmap,
                                                                             pos = (5, interval),
                                                                             size = (10, 10))

                self.bmps_dict[self.Crawler.stocks[i]].SetBitmap(bitmap)
                interval += 45

            self.isexist = True

        except Exception as msg:
            print(f"GOT SOME ERROR IN LOAD IMAGE : {msg}")

    def Hide(self, event):
        if self.isexist:
            print("HIDE STOCKS IMAGES")
            while self.bmps_dict:
                stock_code, bmp = list(self.bmps_dict.items())[-1]
                bmp.Destroy()
                self.bmps_dict.pop(stock_code)
            self.isexist = False
        else:
            print("STOCKS IMAGES IS NOT EXIST")

    def Close(self, event):
        print("CLOSE")
        self.Crawler.close()
        self.frame.Destroy()

if __name__ == "__main__":
    # Create an application object
    app = wx.App()
    StockGUI()
    # Start the event loop
    app.MainLoop()