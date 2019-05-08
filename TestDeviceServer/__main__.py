#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test Tango device server for use with scaling tests."""
import sys

from tango.server import run


from TestDevice1 import TestDevice1
from TestDevice2 import TestDevice2


def main(args=None, **kwargs):
    # TODO(BMo) Register devices (if needed)
    devices = [TestDevice1, TestDevice2]
    run(devices, verbose=True, msg_stream=sys.stdout, args=args, **kwargs)


if __name__ == '__main__':
    main()
