# Spotify Remote

This is a simple python program that implements the software part of a hardware remote to control Spotify playback on another device. It's the boilerplate of an IT course I teach at [Hacker School](https://www.hacker-school.de/), thus the target audience is programming novices that are between 11 and 18 years old.

## Course Overview

After a general introduction, I usually start with simple electronic circuits:

* power a LED from a Raspberry Pi (3.3V => 220Ω => LED => GND)
* LED with button (3.3V => 220Ω => LED => button => GND)

Then I teach some programming basics (input, output, variables, conditions, loops):

[Python Training](https://github.com/s2b/python-training)

The next step is to combine both skills by introducing `gpiozero`, which is usually pre-installed on Raspberry Pi:

* control LED by user input
* button that toggles one or multiple LEDs
* button that cycles through multiple LEDs
* traffic lights

After that, we import the `spotipy` library (see below) and combine all learnings into something that resembles `spotifyRemote.py`. This is where the students usually get creative and develop their individual remotes:

* play/pause, previous, next
* play a favorite title/album/playlist
* control the volume
* disco light when music is playing
* ...

## Setup

### Dependencies

```
pip install git+https://github.com/plamere/spotipy.git --upgrade
```

### Hardware

You can extract the hardware information from the source code pretty easily:

* `Button(21)` defines a button, connected to `GPIO 21`
* `LED(26)` defines a LED, connected to `GPIO 26`

Make sure that you connect the components to the correct ports and that you use the correct resistors for your LEDs, otherwise it may end badly for your Pi. Also note that we don't use 5V, so some types of LEDs might not work correctly.

### First Run

First, you need to add your API credentials (`client_id` and `client_secret`, see [Spotify Apps](https://developer.spotify.com/dashboard/login)) as well as your username (you can look it up [on your Spotify account page](https://www.spotify.com/de/account/overview/)) to the program code.

```
python spotifyRemote.py
```

On first run, the program requires a few handshakes with the Spotify API server, just follow the instructions.

## Ressources

### Raspberry Pi and Hardware

* [GPIO Labels](https://github.com/splitbrain/rpibplusleaf)
* [GPIO Zero Cheat Sheet](https://static.raspberrypi.org/files/education/posters/GPIO_Zero_Cheatsheet.pdf)
* [GPIO Zero Documentation](https://gpiozero.readthedocs.io/en/stable/recipes.html)
* [LED calculator](http://led.linear1.org/1led.wiz)

### Spotify

* [Manage Spotify Apps](https://developer.spotify.com/dashboard/login)
* [Spotify Account Overview](https://www.spotify.com/de/account/overview/)
* [Spotipy Documentation](http://spotipy.readthedocs.io/en/latest/#)
* [Spotify WebAPI Reference](https://developer.spotify.com/documentation/web-api/reference/)
