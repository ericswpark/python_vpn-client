# vpn-client

A Python script to help the use of a VPN client on a server!

For more information, visit this link: https://ideaman924.com/2018/05/01/set-up-a-network-wide-vpn-using-ubuntu-server.html


## Build

Download PyInstaller

    sudo pip install pyinstaller

Then, in the `vpn-client` directory, execute this command:

    pyinstaller --onefile src/main.py

In the `dist` folder, there should be an ELF executable assuming you use Linux.

## Usage

    ./main -h

    usage: main [-h]
                [--start START_REGION | --quit | --restart | --change CHANGE_REGION | --logs]
    
    A simple VPN script for OpenVPN client
    
    optional arguments:
      -h, --help            show this help message and exit
      --start START_REGION, -s START_REGION
                            Start the VPN with the supplied region.
      --quit, -q            Stops the VPN.
      --restart, -r         Restarts the VPN.
      --change CHANGE_REGION, -c CHANGE_REGION
                            Hot-swaps the VPN region.The region is NOT optional.
      --logs, -l            Shows VPN logs.

