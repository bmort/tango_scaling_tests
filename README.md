# Tango Performance tests

Tango Controls performance tests.

## TODO

- ~~Create XMI file for test device with pogo?~~
  - ✅ Can Skip this and create device manually
  - ✅ Can Skip adding all attributes and commands (for now)
- ~~Add instructions to readme for using the development container~~
- Add instructions for monitoring memory / cpu
- Write test script for a few tests to shakedown results
- Move repository to SDP GitHub? (and link to JIRA?)

## 1  References

- [Notes: Google Docs](https://docs.google.com/document/d/1XxoDWZd827XyeOOD8qlFXDuOWoWfx0tw3OsX9iRbSU4)
- <https://jira.ska-sdp.org/browse/UKSW-3>

## 2  Quick-start

```bash
docker stack deploy -c docker-compose.yml tango_test
```

where `tango_test` is the name of the stack.

This starts ....

## Developing using the `tango-python-dev` (name?) container

TODO

## 3  Approach

- Running on Mac book pro using Docker CE X.Y.Z
- ***TODO(BMo): Run on P3***

### 3.1 Test device: `/test_device_1`

This is a Tango device with XX attributes (one of each type) and XX commands.

It is registered and started using xxx

Started using both a Tango Facility and without the Tango db.

## 4  Test results

### 4.1  Device registration and start up

```bash
./tests/device_registration.py N
```

where `N` is the number of test devices.


#### 4.1.1  With Tango database

Using:

```bash
python3 TestDeviceServer N
```

to capture time taken to register and start `N` devices.

**--THESE RESULTS NEED REPEATING AFTER TIMER FIX--**

| Number of devices | Registration (s, s/dev) | Start-up (s, s/dev) | No. samples |
|:-:                |---                      |---                  |--- |
| 1                 |  0.0029 (0.0029)        |   0.0744 (0.0744)   |++  |
| 10                |  0.0290 (0.0029)        |   0.1039 (0.0104)   |1  |
| 100               |  0.3463 (0.0035)        |   0.8781 (0.0088)   |1  |
| 1000              |  4.7922 (0.0048)        |  14.1615 (0.0142)   |1  |
| 2000              | 10.8678 (0.0054)        |  71.2775 (0.0356)   |1  |
| 5000              | 34.3370 (0.0069)        | 264.8581 (0.0530)   |1  |
| 10,000            | 89.7591 (0.0090)        | 899.2384 (0.0899)   |1  |

- Device registration is about 300-100 devices per second.
- Start-up time is about 20 devices per second.

#### 4.1.2  Without Tango database

Use`test_device_1` capture time taken to start

| Number of devices | Start time (s) |
|:-:                |---             |
| 1                 | ???            |
| 10                | ???            |
| 100               | ???            |
| 1000              | ???            |
| 10,000            | ???            |

### 4.2  Device server resource usage (steady state)

> - As reported by `docker stats` and/or monitoring stack
> - Might need to start container non interactively?
>    - (first arg of container == number of devices, 2nd arg = service instance id)
>      - `200 1` --> creates 200 devices using TestDeviceServer/1
>      - `100 2` --> creates 100 devices using TestDeviceServer/2

| Number of devices | (Peak?) Memory (MiB, MiB/device)   | Average CPU (%) |
|:-:                |---                                 | ---             |
| 1                 | 23.57                              |                 |
| 10                | 24.01                              |                 |
| 100               | 30.3                               |                 |
| 1000              | 93.32 (~0.06975 + 23.57)           |                 |
| 2000              | 162.9                              |                 |
| 5000              | 372.3                              |                 |
| 10,000            | 721.4                              | 0.0             |

- For this (TestDevice) device the memory per device seems to be ~0.06975 MiB
- Average CPU for the device, database and sql server is ~0 if the device
  is not in use. The SQL server is the highest with ~0.2% CPU average.
- Average CPU for the SQL db gets maxed out during registration and start-up
of the time which implies that a faster db will improve tango performance.

### 4.3  Device attribute query performance

Number of concurrent queries
Query rate

### 4.4  Device command performance

Number of concurrent commands
Command issue rate

### 4.5  Device pipe performance

***Stretch goal***

----

## Appendix A: PyCharm Pro development setup

Project interpreter set to Docker using `bmort/tango_python_dev:0.1.0`.

## Appendix B: Starting and running the Tango test Device

Start an interactive prompt into a container with Tango installed using

```bash
make prompt
```

### B.1  Without a Tango db & SQL server

```bash
python3 TestDeviceServer 1 -ORBendPoint giop:tcp::20001 \
    -nodb -dlist test/test/0
```

Additional devices can be listed using `dlist` and comma separators.

***Note: This does not seem to work well with multiple classes per server.***

One can then connect to these devices with:

```python
d = DeviceProxy('localhost:20001/test/test/0#dbase=no')
d.identifier
```

### B.2  With Tango Db

First register the device(s) in the database

```bash
python3 scripts/register_test_devices.py
```

To start the device server

```bash
python3 TestDeviceServer N
```

where `N` is the number of devices to start.

To list test devices

```bash
python3 scripts/list_test_devices.py
```

To delete test devices

```bash
python3 scripts/delete_test_devices.py
```


## Appendix C: Useful iTango commands

<https://manpages.debian.org/unstable/python-itango/itango.1.en.html>

- `refreshdb`
- `db`
- `lsdev`
- `lsserv`
- `lsdevclass`
