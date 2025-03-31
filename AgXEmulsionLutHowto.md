# Spectral film simulations in ART with *agx-emulsion*

*(contributed by Leopoldo Saggin and Sébastien Guyader)*

Recently [*arctic*](https://discuss.pixls.us/u/arctic/summary) released [***agx-emulsion***](https://github.com/andreavolpato/agx-emulsion), a physics-based simulation of color film photography processing.

[Alberto Griggio](https://discuss.pixls.us/u/agriggio) decided to extend [**ART**](https://art.pixls.us/) and make possible to integrate *agx-emulsion* as an additional type of **3dLUT**, similarly in concept to what is already possible with *CTL scripts*.

Here, we describe the *installation of agx-emulsion* and its *integration in ART* using **Microsoft Windows** and **Linux** so you can play with it, in case you are interested.

## Installing *uv* {#uv-install}

Since *agx-emulsion* relies on Python, the use of *uv* as a package manager is a nice solution, as it is both easy, fast and cross-platform.

On Windows, *uv* can be installed by typing the following command in a terminal:

``` bash
# ! you only need to execute this command the first time to install uv !
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Installation methods are provided at *uv*'s website for [Linux and MacOS](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1). In addition, you may check your Linux distribution's package manager and see if a binary package already exists.

This way *uv/uvx* binaries are installed in a new subdirectory of the active user by default, which is: `C:\users\%username%\.local\bin` on Windows, or `~/.local/bin` on Linux and MacOS. Notice that if you used a package manager on Linux, the *uv/uvx* binaries may be installed in `/usr/bin`.

***N.B.***: Please check that command for the **uv/uvx** installation have added the directory: `C:\users\%username%\.local\bin` to the ***%username%*** *environment path*.

## Installing *Python 3.11* {#python-install}

Installing Python 3.11 with *uv* is as simple as typing the following command in the terminal:

``` bash
uv python install 3.11
```

This will install CPython 3.11 in `C:\users\%username%\.local\share\uv\python\cpython-3.11{...}\` (Windows) or ``` ~/.local/share/uv/python/``cpython-3.11{...}\ ``` (Linux and MacOS)

## Installing and preparing *agx-emulsion* and required Python packages

### ***agx-emulsion*** **installation** {#agx-emulsion-installation}

If you haven't installed *agx-emulsion* already, the simplest way of doing so is through *uvx*:

``` bash
uvx --from git+https://github.com/andreavolpato/agx-emulsion.git agx-emulsion
```

If you previously downloaded an older zip/tarball snapshot of *agx-emulsion* from its [github repository](https://github.com/andreavolpato/agx-emulsion/), we suggest you delete it and refer to the installation method above to ensure you get an up-to-date version.

Alternatively, if you cloned the *agx-emulsion* repository using *git*, you should first refresh the local repo (`git pull`) and then type:

``` bash
uvx path/to/local/agx-emulsion
```

If everything went well, a napari GUI window should pop up which will let you experiment with *agx-emulsion*. For instance, you can load one of the provided test images (or any image of your choice), and play with the film and print emulsions to ensure the module works.

![*agx-emulsion* native GUI](resources/agx-napari-GUI.png)

### *agx-emulsion* integration in ART {#agx-emusion-art-integration}

Integration of *agx-emulsion* in ART has started since [commit 22fe47d](https://github.com/artpixls/ART/commit/22fe47d2a4b5f72c7895ddd0cf7cfddaaabf3cfe) and is available since [release 1.25.3](https://github.com/artpixls/ART/releases/tag/1.25.3).

In order to use the module in ART, you need to download 2 support files (***agx_emulsion_mklut.py*** and ***ART_agx_film.json)*** from <https://github.com/artpixls/ART/tree/master/tools/extlut> and to save them *both in the same directory* of your choice. **It is crucial that both files reside in the same directory**.

***Note:*** the most convenient place to save both files is the 3D LUT directory declared in ART's **Preferences \> Image Processing \> Directories \> CLUT directory**.

***ART_agx_film.json*** is a configuration file which sets the command to run the Python script ***agx_emulsion_mklut.py*** which by default is:

``` json
    "command" : "python3 agx_emulsion_mklut.py --server",
```

Since this command will likely vary according to your operating system and Python install, you need to open it with a text editor and edit **line 12** to point to the *Python interpreter* you used to install *agx-emulsion*.

If you followed the instructions above to install *uv* and Python 3.11, you will need to update this command with:

(for Windows:)

``` json
    "command" : "C:\\users\\<username>\\.local\\bin\\uv.exe run --python 3.11 --with-editable C:\\path\\to\\local\\agx-emulsion agx_emulsion_mklut.py --server",
```

(for Linux and MacOS:)

``` json
    "command" : "uv run --python 3.11 --with-editable /path/to/local/agx-emulsion agx_emulsion_mklut.py --server",
```

and save the file. Please also note the presence of a "**comma**" at the end of the line!

Now when you start ART you should be able to load ***ART_agx_film.json*** as a **LUT** from the "*Color/Tone Correction*" tool in the "Local editing" tab, or from the "Film Simulation" tool in the "Special Effects" tab.

At this point you can test if everything works:

1.  Open an image in ART
2.  Activate the "*Color/Tone Correction*" tool and, from its "*Mode"* dropdown menu select **LUT** (note that default mode is generally *Standard* or *Perceptual*)
3.  The program will ask for a *LUT file*
4.  Select ***ART_agx_film.json***
5.  At this point a large set of parameters appears, as reported in the image below, and you can play and choose the film simulation you wish to simulate etc...

![*agx-emulsion* module in ART](resources/agx-emulsion-lut.png)

### Updating *agx-emulsion* {#agx-emulsion-updating}

In order to keep both the ***agx-emulsion*** Python code base and its support in ART up to date:

1.  update your local agx-emulsion repo (though *git* or by extracting a zip/tarball) and refer to the second command in the [agx-emulsion section](#agx-emulsion-installation) above
2.  download the ***agx_emulsion_mklut.py*** and ***ART_agx_film.json*** files from <https://github.com/artpixls/ART/tree/master/tools/extlut> again, and replace the existing files in ART's **CLUT directory** with the new ones.

**Disclaimer**

All the information provided on this document is provided on an "*as-is*" basis and you agree that you use such information entirely at *your own risk*. We give *no warranty* and accept *no responsibility or liability for the accuracy or the completeness of the information contained in this document*. Under no circumstances will we be held responsible or liable in any way for any claims, damages, losses, expenses, costs or liabilities whatsoever (including, without limitation, any direct or indirect damages for loss of profits, business interruption or loss of information) resulting or arising directly or indirectly from your use of or inability to use this document.

Leopoldo Saggin aka **Topoldo** [leopoldo.saggin\@yahoo.com](mailto:leopoldo.saggin@yahoo.com)

[Sébastien Guyader](https://discuss.pixls.us/u/sguyader)

Version 0.2 **2025/03/31**
