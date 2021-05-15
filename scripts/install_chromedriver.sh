CHROMEDRIVER_VERSION=90.0.4430.24
CHROMEDRIVER_DIR=/chromedriver

# Set up the Chrome PPA and add google-chrome-stable source
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

apt-get update
apt-get install libnss3 google-chrome-stable -y

# Download and install Chromedriver
mkdir $CHROMEDRIVER_DIR
wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR