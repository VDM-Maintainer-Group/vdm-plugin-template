#!/usr/bin/env python3
''' Plugin Template
'''

from pyvdm.interface import SRC_API
from pyvdm.interface import CapabilityLibrary

class PluginTemplate(SRC_API):

    def onStart(self):
        self.lib = CapabilityLibrary.CapabilityLibrary()
        self.lib.connect()
        self.iLHandle = self.lib.getCapability('inotify_lookup')
        self.iLHandle.register('code')
        return 0

    def onStop(self):
        self.iLHandle.unregister('code')
        # self.iLHandle.drop() #(Optional) auto drop when disconnect
        self.lib.disconnect()
        return 0

    def onSave(self, stat_file):
        with open(stat_file, 'w'):
            result = self.iLHandle.dump('code')
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
