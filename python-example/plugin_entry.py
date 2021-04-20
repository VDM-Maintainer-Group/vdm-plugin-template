#!/usr/bin/env python3
''' Plugin Template
'''

from pyvdm.interface import SRC_API
from pyvdm.interface import RPCWrapper

class PluginTemplate(SRC_API):

    def onStart(self):
        self.rpc = RPCWrapper.RPCWrapper()
        self.rpc.connect()
        self.iLHandler = self.rpc.getCapability('inotify_lookup')
        self.iLHandler.register('code')
        return 0

    def onStop(self):
        self.iLHandler.unregister('code')
        # self.iLHandler.drop() #(Optional) auto drop when disconnect
        self.rpc.disconnect()
        return 0

    def onSave(self, stat_file):
        with open(stat_file, 'w'):
            self.iLHandler.dump('code')
            # save the status
            pass
        return 0

    def onResume(self, stat_file):
        with open(stat_file, 'r'):
            # read the status
            pass
        return 0

    def onClose(self):
        # close the application
        return 0

    pass
