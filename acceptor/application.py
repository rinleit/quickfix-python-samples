"""FIX Application"""
import sys
import quickfix as fix
import Field
import logging
import time
from Message import (Base,Types)
from logger import setup_logger
# const variable
__SOH__ = chr(1)


setup_logger('logfix', 'Logs/message.log')
logfix = logging.getLogger('logfix')

class Application(fix.Application):
    """FIX Application"""
    sessionID = None
    OrderID = 0

    
    def onCreate(self, sessionID):
        """onCreate"""
        return

    def onLogon(self, sessionID):
        self.sessionID = sessionID
        """onLogon"""
        return

    def onLogout(self, sessionID):
        """onLogout"""
        return

    def toAdmin(self, message, sessionID):
        msg = message.toString().replace(__SOH__, "|")
        logfix.debug("S >> " + msg)
        return

    def fromAdmin(self, message, sessionID):
        msg = message.toString().replace(__SOH__, "|")
        logfix.debug("R >> " + msg)
        return

    def toApp(self, message, sessionID):
        msg = message.toString().replace(__SOH__, "|")
        logfix.debug("S >> " + msg)
        return

    def fromApp(self, message, sessionID):
        msg = message.toString().replace(__SOH__, "|")
        logfix.debug("R >> " + msg)
        self.onMessage(message, sessionID)
        return
    

    def onMessage(message, sessionID):
        '''Processing application message'''
        pass

    def run(self):
        """Run"""
        while 1:
            time.sleep(2)
