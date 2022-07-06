```
Updated: June 26, 2022
For use ONLY with a new Ubuntu 22.04 install
Some commands apply to VirtualBox but will not harm VMWare and others
These will assist with the creation of your custom machine and will be updated as things change
Full usage details are available in the book: https://inteltechniques.com/book1.html
Slight variations may be present for Windows/Mac users (such as 'Next' vs. 'Continue')
Please send any issues to errors@inteltechniques.com
Copyright 2022 Michael Bazzell
These instructions are provided 'as is' without warranty of any kind
In no event shall the copyright holder be liable for any claim, damages or other liability
Full license information and restrictions at https://inteltechniques.com/osintbook9/license.txt
```

# VM CREATION

- Install, configure, and launch VirtualBox
- Download Ubuntu 22.04 Desktop from https://releases.ubuntu.com/22.04/
- Within VirtualBox, click on the button labeled 'New' or "Machine" > "New"
- Provide a name of 'OSINT Original'
- Choose your desired location to save the machine on your host
- Select 'Linux' as the type, and 'Ubuntu 64-bit' as the version
- Click Continue
- In the Memory size window, move the slider to select 50% of your system memory
- Click Continue
- Click Create
- Leave the hard disk file type as VDI and click Continue
- Select the default option of 'Dynamically allocated' and click Continue
- Choose the desired size of your virtual hard drive (40GB+)
- Click Create
- Click the Settings icon
- Click the Storage icon
- Click the CD icon which displays 'Empty' in the left menu
- Click the small blue circle to the far right in the 'Optical Drive' option
- Select 'Choose a Disk File'
- Select the Ubuntu 22.04 ISO downloaded previously
- Click 'Open' or Choose' if prompted
- Click 'OK'
- If prompted, confirm the Ubuntu iso
- Click 'Start' in the main menu
- Click 'Start' again if prompted
- Select 'Try or Install Ubuntu'
- Select 'Install Ubuntu'
- Select your desired language and location, then click 'Continue'
- Select 'Normal Installation', 'Download Updates', and 'Install third party'
- Click 'Continue'
- Select 'Erase disk and install Ubuntu', then 'Install Now'. Confirm with 'Continue'
- Choose your desired time zone and click 'Continue'
- Choose a name, user name, computer name, and password of 'osint' for each
- Select 'Log in automatically' then 'Continue'
- Allow Ubuntu to complete the installation, and reboot
- Strike "Enter" when prompted to reboot


# VM CONFIGURATION

- Click 'Skip'
- Select 'No' and then 'Next' when asked to help improve Ubuntu
- Click 'Next' then 'Done' to remove the welcome screen
- If prompted to install updates, click 'Remind me later'
- In the VirtualBox Menu, select Devices > 'Insert Guest Additions CD Image'
- Double click the CD icon in the dock
- Right-click on the file autosun.sh and select 'run as program'
- Provide your password when prompted
- Once the process is complete, press enter, and power off the VM (Upper right menu)
- In VirtualBox, select your VM and click 'Settings'
- In the 'General' icon, click on the 'Advanced' tab
- Change 'Shared clipboard' and Drag n Drop' to 'Bidirectional'
- In the 'Display' icon, change the Video Memory to the maximum
- In the 'Shared Folders' icon, click the green '+'
- Click the dropdown menu under 'Folder Path'
- Select 'Other'
- Choose a desired folder on your host to share data and click 'Open'
- Select the 'Auto-mount' option and then 'OK'
- Click 'OK' to close the settings window
- Start the VM, Open Terminal, and execute the following
- sudo adduser osint vboxsf
- sudo apt purge -y apport
- Restart your Ubuntu VM
- Resize the window if desired
- Resize the VM if desired (View > Virtual Screen > Scale)
- In the left dock, right-click and eject the CD
- Click the Applications Menu (9 dots) in the lower left and launch Settings
- Click 'Notifications' and disable both options
- Click the 'Privacy' option, then click 'Screen Lock' and disable all options
- Click 'File History & Trash', then disable the option
- Click 'Diagnostics', then change to 'Never'
- Click the back arrow and click Power, changing 'Blank Screen' to 'Never'
- Click 'Automatic Suspend' and disable the feature
- Close all Settings windows
- Click the Applications Menu and launch Software Updater
- Click 'Install Now' to apply all updates
- If prompted, restart the VM


# VIRTUALBOX MAINTENANCE

- Some readers have reported the inability to resize VM windows within VirtualBox with the "Auto-resize Guest Display" greyed out. The following commands within Terminal of the Linux VM should repair. There is no harm running these if you are unsure.

```bash
sudo apt update
sudo apt install -y build-essential dkms gcc make perl
sudo rcvboxadd setup
reboot
```


# INSTALL OSINT TOOLS-BASIC

```bash
sudo snap install vlc
sudo apt update
sudo apt upgrade
sudo apt install -y ffmpeg
sudo apt install -y python3-pip
sudo -H pip install youtube-dl
sudo -H pip install yt-dlp
sudo -H pip install youtube-tool
cd ~/Desktop
sudo apt install -y curl
curl -u osint9:book143wt -O https://inteltechniques.com/osintbook9/vm-files.zip
unzip vm-files.zip -d ~/Desktop/
mkdir ~/Documents/scripts
mkdir ~/Documents/icons
cd ~/Desktop/vm-files/scripts
cp * ~/Documents/scripts
cd ~/Desktop/vm-files/icons
cp * ~/Documents/icons
cd ~/Desktop/vm-files/shortcuts
sudo cp * /usr/share/applications/
cd ~/Desktop
rm vm-files.zip
rm -rf vm-files
sudo -H pip install streamlink
sudo -H pip install Instalooter
sudo -H pip install Instaloader
sudo -H pip install toutatis
mkdir ~/Downloads/Programs
cd ~/Downloads/Programs
sudo apt install -y git
git clone https://github.com/Datalux/Osintgram.git
cd Osintgram
sudo apt-get install libncurses5-dev libffi-dev -y
sudo -H pip install -r requirements.txt -I
make setup (This asks for IG username/pass, skip if desired)
sudo snap install gallery-dl
sudo snap connect gallery-dl:removable-media
cd ~/Downloads
sudo apt install default-jre -y
wget https://github.com/ripmeapp/ripme/releases/latest/download/ripme.jar
chmod +x ripme.jar
cd ~/Downloads/Programs
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
sudo -H pip install -r requirements.txt -I
sudo -H pip install socialscan -I
sudo -H pip install holehe -I
cd ~/Downloads/Programs
git clone https://github.com/WebBreacher/WhatsMyName.git
cd WhatsMyName
sudo -H pip install -r requirements.txt -I
cd ~/Downloads/Programs
git clone https://github.com/martinvigo/email2phonenumber.git
cd email2phonenumber
sudo -H pip install -r requirements.txt -I
cd ~/Downloads/Programs
git clone https://github.com/ChrisTruncer/EyeWitness.git
cd EyeWitness/Python/setup
sudo -H ./setup.sh
sudo snap install amass
cd ~/Downloads/Programs
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r
sudo -H pip install -r requirements.txt -I
cd ~/Downloads/Programs
git clone https://github.com/s0md3v/Photon.git
cd Photon
sudo -H pip install -r requirements.txt -I
cd ~/Downloads/Programs
git clone https://github.com/laramies/theHarvester.git
cd theHarvester
sudo -H pip install -r requirements.txt -I
sudo -H pip install testresources -I
sudo -H pip install pipenv -I
sudo -H pip install webscreenshot -I
cd ~/Downloads/Programs
git clone https://github.com/Lazza/Carbon14
cd Carbon14
sudo -H pip install -r requirements.txt -I
sudo apt install tor torbrowser-launcher -y
cd ~/Downloads/Programs
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb
sudo rm google-chrome-stable_current_amd64.deb
sudo apt install -y mediainfo-gui
sudo apt install -y libimage-exiftool-perl
sudo apt install -y mat2
sudo -H pip install xeuledoc -I
cd ~/Downloads/Programs
sudo apt install subversion -y
git clone https://github.com/GuidoBartoli/sherloq.git
cd sherloq/gui
sudo -H pip install -r requirements.txt -I
sudo -H pip install matplotlib
sudo apt install -y webhttrack
sudo apt install -y libcanberra-gtk-module
cd ~/Downloads/Programs
git clone https://github.com/opsdisk/metagoofil.git
cd metagoofil
sudo -H pip install -r requirements.txt -I
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.9 -y
sudo -H python3.9 -m pip install bdfr -I
sudo -H pip install redditsfinder -I
cd ~/Downloads/Programs
git clone https://github.com/MalloyDelacroix/DownloaderForReddit.git
cd DownloaderForReddit
sudo -H pip install -r requirements.txt -I
wget http://dl.google.com/dl/earth/client/current/google-earth-stable_current_amd64.deb
sudo apt install -y ./google-earth-stable_current_amd64.deb
sudo rm google-earth-stable_current_amd64.deb
sudo apt install -y kazam
sudo snap install keepassxc
sudo apt update --fix-missing
sudo apt -y upgrade
sudo apt --fix-broken install
sudo -H pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 sudo -H pip install -U
reboot
```

# INSTALL FIREFOX PROFILE

- Launch and then close Firefox
- Click the Applications Menu, launch Terminal, and execute the following commands

```bash
cd ~/Desktop
curl -u osint9:book143wt -O https://inteltechniques.com/osintbook9/ff-template.zip
unzip ff-template.zip -d ~/snap/firefox/
cd ~/snap/firefox/ff-template/
cp -R * ~/snap/firefox/common/.mozilla/firefox/*.default
cd ~/Desktop
rm ff-template.zip
```
- Open Firefox and update all add-ons


# INSTALL SEARCH TOOLS

```bash
cd ~/Desktop
curl -u osint9:book143wt -O https://inteltechniques.com/osintbook9/tools.zip
unzip tools.zip -d ~/Desktop/
rm tools.zip
```

# INSTALL OSINT TOOLS-ADVANCED

```bash
cd ~/Downloads/Programs
git clone https://github.com/lanmaster53/recon-ng.git
cd recon-ng
sudo -H pip install -r REQUIREMENTS -I
cd ~/Downloads/Programs
git clone https://github.com/smicallef/spiderfoot.git
cd spiderfoot
sudo -H pip install -r requirements.txt -I
cd ~/Downloads/Programs
git clone https://github.com/AmIJesse/Elasticsearch-Crawler.git
sudo -H pip install nested-lookup -I
sudo -H pip install internetarchive -I
sudo apt install -y ripgrep
sudo -H pip install waybackpy -I
sudo -H pip install search-that-hash -I
sudo -H pip install h8mail -I
cd ~/Downloads
h8mail -g
sed -i 's/\;leak\-lookup\_pub/leak\-lookup\_pub/g' h8mail_config.ini
cd ~/Downloads/Programs
git clone https://github.com/mxrch/ghunt
cd ghunt
sudo -H pip install -r requirements.txt -I
```

# USER INTERFACE CONFIGURATION

```bash
gsettings set org.gnome.desktop.background picture-uri ''
gsettings set org.gnome.desktop.background primary-color 'rgb(66, 81, 100)'
gsettings set org.gnome.shell favorite-apps []
gsettings set org.gnome.shell.extensions.dash-to-dock dock-position BOTTOM
gsettings set org.gnome.shell favorite-apps "['firefox_firefox.desktop', 'google-chrome.desktop', 'torbrowser.desktop', 'org.gnome.Nautilus.desktop', 'org.gnome.Terminal.desktop', 'updates.desktop', 'tools.desktop', 'youtube_dl.desktop', 'ffmpeg.desktop', 'streamlink.desktop', 'instagram.desktop', 'gallery.desktop', 'usertool.desktop', 'eyewitness.desktop', 'domains.desktop', 'metadata.desktop', 'httrack.desktop', 'metagoofil.desktop', 'elasticsearch.desktop', 'reddit.desktop', 'internetarchive.desktop', 'spiderfoot.desktop', 'recon-ng.desktop', 'mediainfo-gui.desktop', 'google-earth-pro.desktop', 'kazam.desktop', 'keepassxc_keepassxc.desktop', 'gnome-control-center.desktop']"
gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 32
```

# SOFTWARE UPDATES

```bash
sudo apt update
sudo apt -y upgrade
sudo snap refresh
sudo apt update --fix-missing
sudo apt --fix-broken install
sudo -H pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 sudo -H pip install -U
cd ~/Downloads/Programs/sherlock
git pull https://github.com/sherlock-project/sherlock.git
cd ~/Downloads/Programs/WhatsMyName
git pull https://github.com/WebBreacher/WhatsMyName.git
cd ~/Downloads
wget -N https://github.com/ripmeapp/ripme/releases/latest/download/ripme.jar
cd ~/Downloads/Programs/EyeWitness
git pull https://github.com/ChrisTruncer/EyeWitness.git
cd ~/Downloads/Programs/Sublist3r
git pull https://github.com/aboul3la/Sublist3r.git
cd ~/Downloads/Programs/Photon
git pull https://github.com/s0md3v/Photon.git
cd ~/Downloads/Programs/theHarvester
git pull https://github.com/laramies/theHarvester.git
cd ~/Downloads/Programs/Carbon14
git pull https://github.com/Lazza/Carbon14
cd ~/Downloads/Programs/metagoofil
git pull https://github.com/opsdisk/metagoofil.git
cd ~/Downloads/Programs/sherloq
git pull https://github.com/GuidoBartoli/sherloq.git
cd ~/Downloads/Programs/recon-ng
git pull https://github.com/lanmaster53/recon-ng.git
cd ~/Downloads/Programs/spiderfoot
git pull https://github.com/smicallef/spiderfoot.git
cd ~/Downloads/Programs/Elasticsearch-Crawler
git pull https://github.com/AmIJesse/Elasticsearch-Crawler.git
cd ~/Downloads/Programs/ghunt
git pull https://github.com/mxrch/ghunt.git
sudo apt autoremove -y
```

# OPTIONAL CALLER ID SCRIPT

```bash
cd ~/Documents/scripts
curl -u osint9:book143wt -O  https://inteltechniques.com/osintbook9/cid.sh
chmod +x cid.sh
curl -u osint9:book143wt -O  https://inteltechniques.com/osintbook9/cid.desktop
chmod +x cid.desktop
sudo cp cid.desktop /usr/share/applications/
rm cid.desktop
```