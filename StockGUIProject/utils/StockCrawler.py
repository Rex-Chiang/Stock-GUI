import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Crawler:
    def __init__(self):
        self.stocks = []
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument(
                "user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'"
            )

            # Use ChromeDriverManager to download proper chromedriver to cache
            chrome_service = Service(ChromeDriverManager().install())

            self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        except Exception as msg:
            print(f"Got Error During Crawler Initialization : {msg}")

    def addStock(self, stock_code):
        self.stocks.append(str(stock_code))
        return f"Add Stock : {stock_code}"

    def delStock(self, stock_code):
        self.stocks.remove(str(stock_code))
        return f"Remove Stock : {stock_code}"

    def loadImage(self):
        try:
            for stock in self.stocks:
                url = f"https://s.yimg.com/nb/tw_stock_frontend/scripts/StxChart/StxChart.9d11dfe155.html?sid={stock}"
                self.driver.get(url)
                time.sleep(0.5)

                if not os.path.isdir("./stock_screenshot"):
                    os.mkdir("./stock_screenshot")

                self.driver.save_screenshot(f"./stock_screenshot/{stock}.png")
                print(f"Save Screenshot : {stock}")

        except Exception as msg:
            raise Exception(msg)

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    Crawler = Crawler()
    Crawler.loadImage()
    Crawler.close()