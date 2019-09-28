
PIPTV - A simple Python IPTV client with 82 channels including NFL Network, ESPN, FS1 & FS2

*This is an incredibly simple module. With that being said, I provide this code and all support free of charge, so any donations are welcome and can be sent to this bitcoin address: **bc1qahz93vyljhjj0fsadu2m8zdhaqdaf60gnc7y2y** Thank you and enjoy!*

**Setup** 

*These setup instructions assume you have vlc installed before setup. If you don't have it installed, you can find a download link
[here](https://www.videolan.org/vlc). **Please make sure that the architecture of vlc (64bit/32bit) matches the architecture
of your python installation!** These instructions also assume you have python 3.x and pip installed. If you don't and you're using 
windows, go to python.org and install the latest version of python (which will have pip bundled with it)
Make sure you choose to install for all users and to add python to your path (you will see the check boxes in
the install dialog) For ubuntu and other Debian based Linux distros, open a terminal and type the following*:

```
apt install python3
```

Once you have finished installing vlc, python and pip, the process is as simple as navigating to the directory 
that you downloaded/cloned piptv into, and typing the following in your terminal:

**For Ubuntu/Debian**

```
python3 -m pip install -r requirements.txt
```

**For Windows**

```
pip install -r requirements.txt
```

If you need a more detailed explanation for windows 10, see [doc/windows.md](https://github.com/schwifty42069/piptv/blob/master/doc/windows.md) in this repository

**Use:**

To run the script, navigate to the directory where you downloaded it and type the following:

**For Ubuntu/Debian**

```
python3 piptv.py
```

**For Windows**

```
python piptv.py
```

Upon running the script, you can type **list** to see the channel list, you can type **the name as it appears
in the channel list** to tune to that channel, or you can type **quit** to quit. To stop an actively 
streaming channel, hit **CTRL + C** to stop the stream and return to the prompt.

**Debugging**

The option to pass a debug flag has been added, so if you're experiencing issues you can 
add --debug to the end of the channel name when attempting to tune, and you will see a very verbose
debug output in the terminal. For example, when prompted to enter a command after running the script,
instead of typing.. 

```
espn
```

to tune to espn, type

```
espn --debug
```

and you will see the additional debug output in the terminal!

Enjoy!
