# QuickFIX Python Samples #
*Established connection by* [FIX protocol](https://www.fixtrading.org/standards/)  
*Author:* Rin Le <rinle.it@gmail.com>.  
*Details:* [Configuration for quickfix](http://www.quickfixengine.org/quickfix/doc/html/configuration.html)  

## Requirements
* Python 3.x
* [QuickFIX Engine 1.15.1](http://www.quickfixengine.org/)

## Installing Requirements
```
pip install -r requirements.txt
```

## Start Project
### Use Docker
```sh
cd ./docker
docker-compose up --build
```

### Not use Docker
- Please edit file in initiator/client.cfg: SocketConnectHost=acceptor to SocketConnectHost=127.0.0.1
```sh
cd ./acceptor
python server.py server.cfg
```
```sh
cd ./initiator
python client.py client.cfg
```


