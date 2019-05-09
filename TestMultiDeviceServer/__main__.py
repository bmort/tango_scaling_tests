#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test Tango device server for use with scaling tests."""
import sys
import time

import tango
from tango.server import run


from TestDevice1 import TestDevice1
from TestDevice2 import TestDevice2


def init_callback():
    """Callback called post server initialisation"""
    global START_TIME
    db = tango.Database()
    elapsed = time.time() - START_TIME
    exported_devices = list(db.get_device_exported('test/*'))
    num_devices = len(exported_devices)
    file = open('results.txt', 'a')
    file.write(',{},{}\n'.format(elapsed,elapsed/num_devices))
    print('>> Time taken to start devices: {:.4f} s ({:.4f} s/dev)'
          .format(elapsed, elapsed / num_devices))


def main(args=None, **kwargs):
    """."""
    devices = [TestDevice1, TestDevice2]
    run(devices, verbose=True, post_init_callback=init_callback,
        msg_stream=sys.stdout, args=args, **kwargs)


if __name__ == '__main__':
    START_TIME = time.time()
    print('* Starting server ...')
    sys.argv = ['TestMultiDeviceServer', '1', '-v4']
    main()
