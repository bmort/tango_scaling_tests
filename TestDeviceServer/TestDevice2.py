# -*- coding: utf-8 -*-
"""Test Tango device for use with scaling tests."""
import sys
import time

from tango.server import Device, device_property, command, attribute, run
from tango import DebugIt, DevState


from release import __version__


class TestDevice2(Device):
    """."""
    _start_time = time.time()
    # version = device_property(dtype=str, default_value=__version__)

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


    # @attribute(dtype=str)
    # @DebugIt()
    # def version(self) -> str:
    #     """."""
    #     return __version__

    # @attribute(dtype=float)
    # @DebugIt()
    # def uptime(self) -> float:
    #     """."""
    #     return time.time() - self._start_time

    # -----------------
    # Commands
    # -----------------

    # @command(dtype_in=str, dtype_out=str)
    # def cmd_str_arg(self, value: str) -> str:
    #     """."""
    #     time.sleep(0.01)
    #     return ''
