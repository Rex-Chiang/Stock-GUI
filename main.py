import wx
from Crawler import Crawler

class StockGUI():
    def __init__(self):
        self.Crawler = Crawler()
        self.frame = wx.Frame(None, title="STOCK GUI")
        self.frame.SetSize(500, 500, 500, 500)
        self.panel = wx.Panel(self.frame, wx.ID_ANY)

        button = wx.Button(self.panel, -1, "REFRESH", (10, 10))
        button.Bind(wx.EVT_BUTTON, self.refresh_img)
        button = wx.Button(self.panel, -1, "HIDE", (100, 10))
        button.Bind(wx.EVT_BUTTON, self.Hide)
        button = wx.Button(self.panel, -1, "CLOSE", (190, 10))
        button.Bind(wx.EVT_BUTTON, self.Close)

        [setattr(self, "bmp"+str(x), False) for x in range(1, len(self.Crawler.stocks)+1)]

        self.bmp = [self.bmp1, self.bmp2, self.bmp3, self.bmp4, self.bmp5, self.bmp6]
        # self.isexist = False

        self.frame.Show()
        self.frame.Centre()

    def refresh_img(self, event):
        # if self.isexist:
        #     print("DESTROY")
        #     for bmp in self.bmp:
        #         bmp.Destroy()
        try:
            self.Crawler.LoadImage()
            r = 40
            for i in range(0, len(self.Crawler.stocks)):
                image = wx.Image("/Users/rex/Desktop/StockGUI/dist/main.app/Contents/Resources/img/"+self.Crawler.stocks[i]+".png", wx.BITMAP_TYPE_PNG)

                #size = temp.GetWidth(), temp.GetHeight()

                image = image.GetSubImage(wx.Rect(170, 5, 1115, 100))
                image = image.Scale(450, 40, wx.IMAGE_QUALITY_HIGH)
                temp = image.ConvertToBitmap()

                self.bmp[i] = wx.StaticBitmap(self.frame, -1, temp, pos=(5, r), size=(10,10))
                self.bmp[i].SetBitmap(temp)
                r += 45
            # self.isexist = True
        except:
            # print("GOT SOME ERROR IN LOAD IMAGE")
            self.Crawler.Close()

    def Hide(self, event):
        for bmp in self.bmp:
            bmp.Destroy()

    def Close(self, event):
        self.Crawler.Close()
        self.frame.Destroy()

if __name__ == "__main__":
    app = wx.App()
    StockGUI()
    app.MainLoop()