# Stock GUI

## Overview
This project retrieve stocks information from Yahoo. Users could customize the stock code list by using the *INPUT* and *REMOVE* buttons on GUI, and use the *REFRESH* button to get the instant stock information. If users need to hide the stock information on GUI in some situation, they can use the *HIDE* button instead of shutting down the app. Finally, if need to shutdown the app, just use the *CLOSE* button on GUI.

## Developing
**Built With:**
* Python3
* Selenium
* wxPython
* Py2app

## Tests
```
cd Stock-GUI
python3 -m venv StockGUIEnv
source StockGUIEnv/bin/activate
pip3 install -r requirements.txt
cd StockGUIProject
py2applet --make-setup StockGUIapp.py
python3 setup.py py2app
./dist/StockGUIapp.app/Contents/MacOS/StockGUIapp
```

## Demo
<img width="500" height="500" src=https://github.com/Rex-Chiang/Stock-GUI/blob/main/Demo.gif>
