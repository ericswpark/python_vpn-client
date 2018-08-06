# User made changes from now on

# DEFINE REGION!
#     HK --> Hong Kong
#     LA --> Los Angeles 3
# CHANGE IF AUTO ENABLE/DISABLE WAS CHANGED
export REGION=HK
      
# Set as current region. Default to HK because that's what we use
# on boot.
# DO NOT MODIFY THIS PARAMETER.
export CURRENT_REGION=HK

# (new and improved) VPN script
vpn() { 
   case "$1" in
   "-l" | "--logs" | "--log")
      watch -n 1 "journalctl -u openvpn@$CURRENT_REGION | tail -n 10"
      ;;
   "-r" | "--restart")
      sudo systemctl restart openvpn@$CURRENT_REGION
      ;;
   "-c" | "--change")
      if [ -z "$2" ]
        then
          echo "Warning! No region supplied.\n
This parameter REQUIRES A REGION FIELD. ABORTING..."
      else
          sudo systemctl stop openvpn@$CURRENT_REGION
          export CURRENT_REGION=$2
          sudo systemctl start openvpn@$CURRENT_REGION
      fi
      ;;
   "-q" | "--quit")
      sudo systemctl stop openvpn@$CURRENT_REGION
      unset CURRENT_REGION
      ;;  
   "-s" | "--start")
      if [ -z "$2" ]
        then
          echo "Warning! No region supplied. Using default region."
          sudo systemctl start openvpn@$REGION
          export CURRENT_REGION=$REGION
      else
          sudo systemctl start openvpn@$2
          export CURRENT_REGION=$2
      fi
      ;;
   "-d" | "--disable")
      if [ -z "$2" ]
        then
          echo "Warning! No region supplied. Using default region."
          sudo systemctl disable openvpn@$REGION
      else
          sudo systemctl disable openvpn@$2
      fi  
      ;;
   "-e" | "--enable")
      if [ -z "$2" ]
        then
          echo "Warning! No region supplied. Using default region."
          sudo systemctl enable openvpn@$REGION
      else
          sudo systemctl enable openvpn@$2
      fi
      ;;  
   "-?" | "-h" | "--help")
      echo -e "A script to help facilitate the VPN connection.\n\n
   -l or --logs or --log to display the log\n
   -s or --start to start the VPN\n
   -q or --quit to stop the VPN\n
   -c or --change to change VPN servers online (hotswap)\n
       Supply parameter <region> to set region to use.\n
   -r or --restart to restart the VPN\n\n
   -e or --enable to start auto execution on reboot.\n
       Supply parameter <region> to set region to use.\n
       Default is set to script defaults (check .bashrc.)\n
   -d or --disable to stop auto execution on reboot.\n
       Supply parameter <region> to set region to use.\n
       Default is set to script defaults (check .bashrc.)\n"
      ;;  
   *) 
      echo -e "Warning, $1 is not a valid operand."
   esac
}

