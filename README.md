# QUICKFIX EXAMPLE FOR PYTHON #
Established connection by [FIX protocol](https://www.fixtrading.org/standards/)  
*Author:* Rin Le <rinle.it@gmail.com>.  
*Details:* [Configuration](http://www.quickfixengine.org/quickfix/doc/html/configuration.html)  

## Requirements
* Python 3.x
* [QuickFIX Engine](www.quickfixengine.org/)

## Installing Requirements
```
pip install -r requirements.txt
```

## Start Project 
### Server
```
cd ./acceptor
python server.py server.cfg
```
### Client
```
cd ./initiator
python client.py client.cfg
```
