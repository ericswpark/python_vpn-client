# vpn-client

A Python script to help the use of a VPN client on a server!

For more information, visit this link: https://blog.ericswpark.com/2018/04/30/set-up-a-network-wide-vpn-using-ubuntu-server.html


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
                            Hot-swaps the VPN region. The region is NOT optional.
      --logs, -l            Shows VPN logs.

## Tips and tricks

**Q: The script asks for my password every time I try to stop or start the VPN.**

This is expected behavior. The script makes use of `systemctl`, and OpenVPN can only be run with the system-level systemd service. To modify system services, you need root permission.

If you are OK with less security because the box is on a secure network, or if you're really confident with your security skills, you could modify the `sudoers` file with `sudo visudo` and tell `sudo` not to prompt you when you are running `systemctl` calls. Type the following line at the end of the file:

    username ALL=NOPASSWD: /bin/systemctl

Replace `username` with your username, save, and exit.

If it complains about syntax errors, your `systemctl` binary might be in a different location. Try `whereis systemctl` and substitute the correct directory name. For more information, I suggest [this AskUbuntu article.](https://askubuntu.com/questions/72267/how-to-allow-execution-without-prompting-for-password-using-sudo)
