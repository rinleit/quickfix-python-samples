# QUICKFIX SAMPLE FOR PYTHON #
Established connection by [FIX protocol](https://www.fixtrading.org/standards/)
*Author:* Rin Le.
*Details:* [Configuration](http://www.quickfixengine.org/quickfix/doc/html/configuration.html)

## Requirement
* Python 3.x
* [quickfix 1.15.1](www.quickfixengine.org/)

## Server
```
cd ./acceptor
python server.py server.cfg
```
## Client
```
cd ./initiator
python client.py client.cfg
```

