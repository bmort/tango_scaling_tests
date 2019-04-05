# -*- coding: utf-8 -*-
"""Test Tango device server for use with scaling tests."""
import sys

import tango
from tango import server

import test_device


def register_devices():
    """."""
    tango_db = tango.Database()
    device_info = tango.DbDevInfo()
    device_info._class = "TestDevice"
    device_info.server = "test_device_ds/1"

    num_devices = 1
    for index in range(num_devices):
        device_info.name = 'low_sdp/elt/test_device_{:03d}'.format(index)
        tango_db.add_device(device_info)

    tango_db.put_class_property(device_info._class, dict(version='1.0.0'))


def main(args=None, **kwargs):
    """Start the test device server."""
    return server.run([test_device.TestDevice1],
                      verbose=True, msg_stream=sys.stdout,
                      args=args, **kwargs)


if __name__ == '__main__':
    register_devices()
    main()
