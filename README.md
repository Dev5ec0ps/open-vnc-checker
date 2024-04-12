# Open VNC Checker

The Open VNC Checker is a simple Python script designed to check for publicly accessible VNC services without authentication. It connects to specified IP addresses and ports commonly used by VNC servers to determine if they are accessible without requiring authentication.

## Prerequisites

- Python 3.x
- `argparse` library (usually included with Python)

## Installation

There is no formal installation process for this tool. Simply download the `open-vnc-checker.py` script and run it using Python.

## Usage

```cmd
python3 open-vnc-checker.py -ip <ip_address>
```

### Arguments:

- `-ip, --ip_address`: The IP address to check for open VNC ports.

## Example

```cmd
python3 open-vnc-checker.py -ip 127.0.0.1
```

This command checks the specified IP address (`127.0.0.1` in this example) for potentially accessible VNC ports.

## How it works

The script connects to each specified port on the given IP address and sends a simple message to check for a response. If the response contains the string 'RFB', it indicates that a VNC service is running without authentication, making it vulnerable.

## Disclaimer

This tool is intended for security research and educational purposes only. Use it responsibly and only on systems you have permission to test.
