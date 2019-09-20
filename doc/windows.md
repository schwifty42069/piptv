This method was documented by @ZoleeHU for windows 10, but can be adapted for windows 7 & 8

1. First and foremost, download VLC and install it, if you don't already have it. You can find it [here](https://www.videolan.org/vlc/index.html)

2. Next, we will need Python, the easiest way is through powershell with Chocolatey to install Chocolatey copy Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')) into powershell and wait for it to be completed.

3. Next we will need Python itself, copy choco install -y python3 and wait for it to be completed, you may have to sign out & in out of Windows after this.

4. Now write python --version to make sure that it is actually installed (if not and you haven't already logged out and in, do it, it should fix it)

5. Now we will need the requirements, the crude way of getting them is with pip, copy these commands one-by-one and wait for them to be completed:

```
python -m pip install requests
python -m pip install beautifulsoup4
python -m pip install python_vlc
```

**Final Steps**

Now, if you don't already have the piptv.py file then you can do so by right-clicking on [this link](https://github.com/schwifty42069/piptv/raw/master/piptv.py) and choosing "Save link as..." save it to your desired location.

Now cd over to that location with Powershell, once you are in the folder do python piptv.py (or python yourfilename.py ) it should start the program, albeit with funky coloring codes, they should be fixed after tuning to a channel and stopping the playback

Remember that it sets VLC to fullscreen (you can change this in the source code) and to "exit" out of a channel you will need to Alt-Tab and press CTRL+C in the powershell window.