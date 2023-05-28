# QuickFIX Python Samples #
* Established connection by [FIX protocol](https://www.fixtrading.org/standards/)  
* Author: Rin Le <rinle.it [a] gmail.com>.  
* Details: [Configuration for quickfix](https://www.quickfixj.org/usermanual/2.3.0/usage/configuration.html)  

## Requirements
* Python 3.x
* [QuickFIX Engine 1.15.1](http://www.quickfixengine.org/)

## Installing Requirements
```
pip install -r requirements.txt
```

## Run Project
### With Docker

Please edit file initiator/client.cfg: Tag SocketConnectHost=acceptor

```sh
cd ./docker
docker-compose up --build
```

### Without Docker

Please edit file initiator/client.cfg: Tag SocketConnectHost=127.0.0.1 <br>
*You must launch the server side first, then launch the client side for the quickfix to establish a standard FIX protocol connection.*

#### Run Server
```sh
cd ./acceptor
python server.py server.cfg
```

#### Run Client
```sh
cd ./initiator
python client.py client.cfg
```


