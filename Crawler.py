import time
from selenium import webdriver

class Crawler:
    def __init__(self):
        # self.driver = webdriver.Safari()
        self.stocks = ["9904", "912000", "8101", "1447", "1409", "00701"]

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(
            'user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"')

        self.driver = webdriver.Chrome(executable_path='/Users/rex/Desktop/StockGUI/chromedriver',
                                       chrome_options=chrome_options)
    def LoadImage(self):
        #print("DOWNLOAD IMAGE")
        for stock in self.stocks:
            url = "https://s.yimg.com/nb/tw_stock_frontend/scripts/StxChart/StxChart.9d11dfe155.html?sid=" + stock
            self.driver.get(url)
            time.sleep(0.5)
            print("SAVE SCREENSHOT")
            self.driver.save_screenshot("/Users/rex/Desktop/StockGUI/dist/main.app/Contents/Resources/img/"+stock+".png")
            # time.sleep(0.5)
            # print("CROP THE IMAGE")
            # img = Image.open("img/"+stock+".png")
            # time.sleep(1)
            # img = img.crop((170, 5, 1115, 100))
            # img = img.resize((450, 40))
            # print("SAVE FINAL IMAGE")
            # img.save("img/"+stock+".png")
        #self.driver.close()

    def Close(self):
        self.driver.close()
