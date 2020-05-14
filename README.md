# QuickFIX Python Samples #
* *Established connection by* [FIX protocol](https://www.fixtrading.org/standards/)  
* *Author:* Rin Le <rinle.it@gmail.com>.  
* *Details:* [Configuration for quickfix](http://www.quickfixengine.org/quickfix/doc/html/configuration.html)  

## Requirements
* Python 3.x
* [QuickFIX Engine 1.15.1](http://www.quickfixengine.org/)

## Installing Requirements
```
pip install -r requirements.txt
```

## Run Project
### With Docker
```sh
cd ./docker
docker-compose up --build
```

### Without Docker
```sh
Please modify file path in initiator/client.cfg from SocketConnectHost=acceptor to SocketConnectHost=127.0.0.1
```
```sh
cd ./acceptor
python server.py server.cfg
```
```sh
cd ./initiator
python client.py client.cfg
```


