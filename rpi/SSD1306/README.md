# SSD1306


Wrapper for the Adafruit SSD1306 Raspberry PI OLEG display

### Install dependencies:

```
sudo apt-get update
sudo apt-get install build-essential python-dev python-pip
sudo pip install RPi.GPIO
sudo apt-get install python-imaging python-smbus
```


### Install library

```
sudo apt-get install git
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python setup.py install
```

### Run sample
```
PYTHONPATH=`pwd` python3 rpi/ssd1306/Example.py
```