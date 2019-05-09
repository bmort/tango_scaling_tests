# -*- coding: utf-8 -*-
"""Test Tango device for use with scaling tests."""
import time

from tango.server import Device, attribute
from tango import DevState


class TestDevice2(Device):
    """."""
    _start_time = time.time()

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        """."""
        Device.init_device(self)
        self.set_state(DevState.STANDBY)

    def always_executed_hook(self):
        """."""
        pass

    def delete_device(self):
        """."""
        pass

    # -----------------
    # Attribute methods
    # -----------------

    @attribute(dtype=str)
    def identifier(self):
        """Return the device name"""
        return type(self).__name__


