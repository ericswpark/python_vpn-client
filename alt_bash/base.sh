# (new and improved) VPN script
vpn() {
   case "$1" in
   "-l" | "--logs" | "--log")
      journalctl -u openvpn@<VPN name here>
      ;;
   "-r" | "--restart")
      sudo systemctl restart openvpn@<VPN name here>
      ;;
   "-q" | "--quit")
      sudo systemctl stop openvpn@<VPN name here>
      ;; 
   "-s" | "--start")
      sudo systemctl start openvpn@<VPN name here>
      ;;
   "-?" | "-h" | "--help")
      echo -e "A script to help facilitate the VPN connection.\n\n
   -l or --logs or --log to display the log\n
   -s or --start to start the VPN\n
   -q or --quit to stop the VPN\n
   -r or --restart to restart the VPN\n"
      ;;
   *)
      echo -e "Warning, $1 is not a valid operand."
   esac
}
