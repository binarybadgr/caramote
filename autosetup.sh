# automate setup script
#!/bin/sh

# fetch update to latest
sudo apt update && sudo apt upgrade -y
sudo apt install git libopencv
