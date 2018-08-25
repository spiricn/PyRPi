# DS18B20


Temperature sensor, using 1-Wire protocol to read values from a DS18B20 probe


## Quick start

* Enable 1-Wire interface, by adding the following line to ```/boot/config.txt``` 

    ```
    dtoverlay=w1-gpio,gpiopin=<PIN_NUMBER>
    ```
    Rreplace ```<PIN_NUMBER>``` with an actual PIN number of your choosing.


* Reboot the device
    ```
    sudo reboot
    ```

* Find the device ID by listing the following directory:

    ```
    ls /sys/bus/w1/devies
    ```

    You will need to save the device ID from that directory (e.g. ```28-00000482b243```) and use it in configuring the library

* Run the example
    ```
    PYTHONPATH=`pwd` python3 rpi/DS18B20/Example.py 28-00000482b243
    ```
