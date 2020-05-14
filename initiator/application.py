#!/usr/bin/python
# -*- coding: utf8 -*-
"""FIX Application"""
import sys
# from datetime import datetime
import quickfix as fix
import time
import logging
from model.logger import setup_logger
from model import Field
from model.Message import __SOH__

# Logger
setup_logger('logfix', 'Logs/message.log')
logfix = logging.getLogger('logfix')


class Application(fix.Application):
    """FIX Application"""

    def onCreate(self, sessionID):
        self.sessionID = sessionID
        return
    def onLogon(self, sessionID):
        self.sessionID = sessionID
        return
    def onLogout(self, sessionID): 
        return

    def toAdmin(self, message, sessionID):
        msg = message.toString().replace(__SOH__, "|")
        logfix.info("S >> %s" % msg)
        return
    def fromAdmin(self, message, sessionID):
        msg = message.toString().replace(__SOH__, "|")
        logfix.info("R << %s" % msg)
        return
    def toApp(self, message, sessionID):
        msg = message.toString().replace(__SOH__, "|")
        logfix.info("S >> %s" % msg)
        return
    def fromApp(self, message, sessionID):
        msg = message.toString().replace(__SOH__, "|")
        logfix.info("R << %s" % msg)
        self.onMessage(message, sessionID)
        return

   
    def onMessage(self, message, sessionID):
        """Processing application message here"""
        pass

    def run(self):
        """Run"""
        while 1:
            time.sleep(2)
