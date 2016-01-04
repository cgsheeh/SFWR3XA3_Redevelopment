# OpenBazaar Redevelopment Project

This repo contains the OpenBazaar Redevelopment project for SFWR 3XA3 at McMaster University

The course mission was to integrate the body of knowledge obtained up to this point in the program in an open ended way. This was done by allowing students to select an open source project and 'redevelop' it, with teacher guidance. The focus of the course was on documentation and following good practices, rather than creating a large implementation. Due to time constraints, only the front-end components of the application were developed, with a "Node" module to implement the networking component at a later time (after the course completion). Below this point is the project in its final submission.

Some important skills learned through this course:
+ Proper use of Git and revisions
+ Automatic code generation
+ Importance of deadlines and project scheduling
___

```
_____                 ______
|  _  |                | ___ \
| | | |_ __   ___ _ __ | |_/ / __ _ ______ _  __ _ _ __
| | | | '_ \ / _ \ '_ \| ___ \/ _` |_  / _` |/ _` | '__|
\ \_/ / |_) |  __/ | | | |_/ / (_| |/ / (_| | (_| | |   
 \___/| .__/ \___|_| |_\____/ \__,_/___\__,_|\__,_|_|   
      | |  A Redevelopment project for SFWR 3XA3 
      |_|  Daniel Mandel, Shandelle Murray, Connor Sheehan
```

This project has been tested to work on Ubuntu 14.

To setup the project, in src/ run
```
$ sudo ./setup.sh
```

Once all dependencies have been installed, run

```
$ python OpenBazaar2.py
```
in src/ to start the program. 

Please note that on first startup, a set of GPG keys
will be created. On some operating systems this may take several
minutes, and may require some generated entropy.

To run the program with data from the demo, after startup run in src/

```
$ python OpenBazaar2.py --load-demo
```

To re-initialize the identity module, run in src/

```
$ python OpenBazaar2.py --restart
```
