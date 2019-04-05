# -*- coding: utf-8 -*-
#
# This file is part of the Test_device_2 project
#
#
#
# Distributed under the terms of the MIT license.
# See LICENSE.txt for more info.

""" Tango Scaling Test

"""

# PyTango imports
import PyTango
from PyTango import DebugIt
from PyTango.server import run
from PyTango.server import Device, DeviceMeta
from PyTango.server import attribute, command, pipe
from PyTango.server import class_property, device_property
from PyTango import AttrQuality, DispLevel, DevState
from PyTango import AttrWriteType, PipeWriteType
# Additional import
# PROTECTED REGION ID(Test_device_2.additionnal_import) ENABLED START #
# PROTECTED REGION END #    //  Test_device_2.additionnal_import

__all__ = ["Test_device_2", "main"]


class Test_device_2(Device):
    """
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(Test_device_2.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  Test_device_2.class_variable

    # ----------------
    # Class Properties
    # ----------------

    string_class_property = class_property(
        dtype='str',
    )

    # -----------------
    # Device Properties
    # -----------------

    string_device_property = device_property(
        dtype='str',
    )

    # ----------
    # Attributes
    # ----------

    str_attr = attribute(
        dtype='str',
        access=AttrWriteType.READ_WRITE,
    )

    str_attr_polled = attribute(
        dtype='str',
        access=AttrWriteType.READ_WRITE,
    )

    dbl_spec_attr = attribute(
        dtype=('double',),
        max_dim_x=1024,
    )

    dbl_img_attr = attribute(
        dtype=(('double',),),
        max_dim_x=1024, max_dim_y=1024,
    )

    # -----
    # Pipes
    # -----

    test_pipe = pipe(
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        Device.init_device(self)
        # PROTECTED REGION ID(Test_device_2.init_device) ENABLED START #
        # PROTECTED REGION END #    //  Test_device_2.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(Test_device_2.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  Test_device_2.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(Test_device_2.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  Test_device_2.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_str_attr(self):
        # PROTECTED REGION ID(Test_device_2.str_attr_read) ENABLED START #
        return ''
        # PROTECTED REGION END #    //  Test_device_2.str_attr_read

    def write_str_attr(self, value):
        # PROTECTED REGION ID(Test_device_2.str_attr_write) ENABLED START #
        pass
        # PROTECTED REGION END #    //  Test_device_2.str_attr_write

    def read_str_attr_polled(self):
        # PROTECTED REGION ID(Test_device_2.str_attr_polled_read) ENABLED START #
        return ''
        # PROTECTED REGION END #    //  Test_device_2.str_attr_polled_read

    def write_str_attr_polled(self, value):
        # PROTECTED REGION ID(Test_device_2.str_attr_polled_write) ENABLED START #
        pass
        # PROTECTED REGION END #    //  Test_device_2.str_attr_polled_write

    def read_dbl_spec_attr(self):
        # PROTECTED REGION ID(Test_device_2.dbl_spec_attr_read) ENABLED START #
        return [0.0]
        # PROTECTED REGION END #    //  Test_device_2.dbl_spec_attr_read

    def read_dbl_img_attr(self):
        # PROTECTED REGION ID(Test_device_2.dbl_img_attr_read) ENABLED START #
        return [[0.0]]
        # PROTECTED REGION END #    //  Test_device_2.dbl_img_attr_read


    # -------------
    # Pipes methods
    # -------------

    def read_test_pipe(self):
        # PROTECTED REGION ID(Test_device_2.test_pipe_read) ENABLED START #
        return dict(x=0,y=0)
        # PROTECTED REGION END #    //  Test_device_2.test_pipe_read

    # --------
    # Commands
    # --------

    @command(
    dtype_in='str', 
    )
    @DebugIt()
    def test_command_str_arg(self, argin):
        # PROTECTED REGION ID(Test_device_2.test_command_str_arg) ENABLED START #
        pass
        # PROTECTED REGION END #    //  Test_device_2.test_command_str_arg

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(Test_device_2.main) ENABLED START #
    return run((Test_device_2,), args=args, **kwargs)
    # PROTECTED REGION END #    //  Test_device_2.main

if __name__ == '__main__':
    main()
