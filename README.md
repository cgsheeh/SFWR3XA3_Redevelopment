 _____                 ______
|  _  |                | ___ \
| | | |_ __   ___ _ __ | |_/ / __ _ ______ _  __ _ _ __ 
| | | | '_ \ / _ \ '_ \| ___ \/ _` |_  / _` |/ _` | '__|
\ \_/ / |_) |  __/ | | | |_/ / (_| |/ / (_| | (_| | |   
 \___/| .__/ \___|_| |_\____/ \__,_/___\__,_|\__,_|_|   
      | |  A Redevelopment project for SFWR 3XA3 
      |_|  Daniel Mandel, Shandelle Murray, Connor Sheehan

This project has been tested to work on Ubuntu 14.

To setup the project run
```
$ sudo ./setup.sh
```

Once all dependencies have been installed, run

```
$ python OpenBazaar2.py
```
to start the program. 

Please note that on first startup, a set of GPG keys
will be created. On some operating systems this may take several
minutes, and may require some generated entropy.

To run the program with data from the demo, after startup run

```
$ python OpenBazaar2.py --load-demo
```

To re-initialize the identity module, run

```
$ python OpenBazaar2.py --restart
```
