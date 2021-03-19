# Shift Scheduler

## How it Works
Uses pypy (python3.7) as interpreter to run a flask server and start a webview<br/>
(`webapp-container http://localhost:port/`).<br/>
> The flask server port is set to 0

  * Tested Devices:
    * Volla Phone
  * Arch: aarch64

  > prepared pypy package: [pypy-aarch64.tar.gz](dist/pypy-aarch64.tar.gz)<br/>
  > see: *https://www.pypy.org/*<br/>
  > see: *https://www.pypy.org/download.html*


## Install Info: (pypy interpreter)

1. Install the pypy interpreter (just unpack [pypy.arm64.tar.gz](dist/pypy.arm64.tar.gz) into your home folder.)
  * `wget https://raw.githubusercontent.com/KnacKWursTKinG/python-shiftscheduler/main/ubports/dist/pypy.arm64.tar.gz`
  * `tar --extract --gzip --file pypy.arm64.tar.gz --directory ~/`
2. And `sudo ln -s ~/pypy.arm64/bin/* /usr/local/bin/` (for this step you need to make the image writable)
  > Note: pypy (python3.7) has some preinstalled modules<br/>
  > see `ls ~/pypy.arm64/site-packages`
3. Test with `pypy --version` & `pypy -m pip --version`


### missing libssl.so.1.1:

@ToDo ...


## TODO

* write a workaroud for the missing **libssl.so.1.1** on ubports phone


## Screenshots
<img src="doc/screenshots/landscape.png" width="700"></img><br/>
<img src="doc/screenshots/portrait-note.png" width="350"></img>
<img src="doc/screenshots/portrait.png" width="350"></img>


## License

Copyright (C) 2021  Udo Bauer

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License version 3, as published
by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranties of MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
