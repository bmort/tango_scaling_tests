#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test Tango device server for use with scaling tests."""
import sys
import time
import logging

import tango
from tango import server

# import test_device


def register_devices():
    """."""

    tango_db = tango.Database()
    logging.info("Registering devices!")


    device_info = tango.DbDevInfo()

    test_name = 'test1'
    device_info.server = "TestDevice/{}".format(test_name)
    device_info._class = "TestDevice"

    # Generate names and add devices to the database.
    start_time = time.time()
    num_devices = 1000
    for index in range(num_devices):
        device_info.name = 'tango/{}/{:03d}'.format(test_name, index)
        tango_db.add_device(device_info)

    tango_db.put_class_property(device_info._class, dict(version='1.0.0'))
    print('elapsed = {}'.format(time.time() - start_time))


if __name__ == '__main__':
    logging.basicConfig()
    register_devices()
