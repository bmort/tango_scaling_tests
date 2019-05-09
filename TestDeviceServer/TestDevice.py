# -*- coding: utf-8 -*-
"""Test Tango device for use with scaling tests."""
import time

from tango.server import Device, device_property, command, attribute
from tango import DevState


from release import __version__


class TestDevice(Device):
    """."""
    _start_time = time.time()
    version = device_property(dtype=str, default_value=__version__)

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        """."""
        # start_time = time.time()
        Device.init_device(self)
        # print('{} {}'.format(self.get_name(), time.time() - start_time))
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
    def version(self):
        """Return the device version."""
        return __version__

    @attribute(dtype=str)
    def identifier(self):
        """Return the device name"""
        return type(self).__name__

    @attribute(dtype=float)
    def uptime(self):
        """."""
        return time.time() - self._start_time

    @attribute(dtype=str)
    def attr001(self):
        return ''

    @attribute(dtype=str)
    def attr002(self):
        return ''

    @attribute(dtype=str)
    def attr003(self):
        return ''

    @attribute(dtype=str)
    def attr004(self):
        return ''

    @attribute(dtype=str)
    def attr005(self):
        return ''

    @attribute(dtype=str)
    def attr006(self):
        return ''

    @attribute(dtype=str)
    def attr007(self):
        return ''

    @attribute(dtype=str)
    def attr008(self):
        return ''

    @attribute(dtype=str)
    def attr009(self):
        return ''

    @attribute(dtype=str)
    def attr010(self):
        return ''

    @attribute(dtype=str)
    def attr011(self):
        return ''

    @attribute(dtype=str)
    def attr012(self):
        return ''

    @attribute(dtype=str)
    def attr013(self):
        return ''

    # -----------------
    # Commands
    # -----------------

    @command(dtype_in=str, dtype_out=str)
    def cmd_str_arg(self, value: str) -> str:
        """."""
        time.sleep(0.01)
        return value
