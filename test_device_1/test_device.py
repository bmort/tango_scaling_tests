# -*- coding: utf-8 -*-
"""Test Tango device for use with scaling tests."""
import time

import tango.Device
from tango import server

import release

class TestDevice(tango.Device):
    """."""
    _start_time = time.time()
    version = device_property(dtype=str, default_value=release.__version__)

    def init_device(self):
        """."""
        server.Device.init_device()
        self.set_state(tango.DevState.STANDBY)

    def always_executed_hook(self):
        """."""

    def delete_device(self):
        """."""

    @command(dtype_in=str, dtype_out=str)
    def configure(self, value: str) -> str:
        """."""
        sleep(0.01)
        return ''

    @attribute(dtype=float)
    @DebugIt()
    def uptime(self) -> float:
        """."""
        return time.time() - self._start_time
