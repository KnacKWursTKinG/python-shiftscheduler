# Shift Scheduler

## How it Works
Uses pypy (python3.7) as interpreter to run a flask server and start a webview<br/>
(`webapp-container http://localhost:port/`).<br/>
> The flask server port is set to 0

  * Tested Devices:
    * Volla Phone
  * Arch: aarch64
  * Flask Import Duration: 2.4 seconds

  > prepared pypy package: [pypy-aarch64.tar.gz](dist/pypy-aarch64.tar.gz)<br/>
  > see: *https://www.pypy.org/*
  > see: *https://www.pypy.org/download.html*


## Install Info:
1. You need an **pypy** interpreter with the **flask** module, i prepared a package for that.
> `sudo tar --extract --gzip --file dist/pypy-aarch64.tar.gz --directory /opt/`
2. link everything from the pypy bin folder to `/usr/local/bin`
> `sudo ln -s /opt/pypy-aarch64/bin/* /usr/local/bin/`
3. that's it, now install the [shiftscheduler click](dist/shiftscheduler.knackwurstking_1.0.0_arm64.click)
package on the phone
4. or with clickable on pc:
> `clickable --arch arm64`

### Notes:
* Python3.5 is not an option for me, so i use the pypy interpreter on my phone.
* I only prepared an pypy package for *aarch64*, so `--arch` is arm64 for now.
* Will work on PC too (uses `pywebview` and `flask` on PC)
> `python www/main.py`


## TODO
* graphical configuraion
  * for now the *config.ini* file can be used for that
  * location after the first start *`~/.config/shiftscheduler.knackwurstking/config.ini`*
  * and on pc *`~/.config/shiftscheduler/config.ini`*
* add *'opt_steps'* to *'config.ini'* (`opt_steps = U,UP,K`)
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
