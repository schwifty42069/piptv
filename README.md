PIPTV - A simple Python IPTV client with 82 channels including NFL Network, ESPN, FS1 & FS2

This is an incredibly simple module.

**Setup** 

*This is assuming you have python 3.x and pip installed, if you don't and you're using 
windows, go to python.org and install the latest version of python (which will have pip bundled with it)
Make sure you choose to install for all users and to add to your path (you will see the check boxes in
the install dialog) For ubuntu and other Debian based Linux distros, open a terminal and type the following*:

```
apt install python3
```

Once you have finished installing python and pip, the process is as simple as navigating to the directory 
that you downloaded/cloned piptv into, and typing the following in your terminal:

**For Ubuntu/Debian**

```
python3 -m pip install -r requirements.txt
```

**For Windows**

```
pip install -r requirements.txt
```

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


Enjoy!