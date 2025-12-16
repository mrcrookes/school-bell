# Simple school bell
### Simple python script to play sounds over the school day on a Raspberry Pi
Credit to https://gist.github.com/BillSimpson/d7a1a531995c8b63492bb47ef8872618 for the orginal idea, code and instructions

### And Two simple python scripts to play Christmas playlist over breaks on a Raspberry Pi
Credit to https://gist.github.com/gitblight1/602f0a73672822c1ef6b056ff35ea293 for the orginal idea, code and instructions

## Setup soundcard
May need to do following step to set correct default system soundcard. You can find your desired card with:
> #### cat /proc/asound/cards <br />
and then create /etc/asound.conf with following to set defaults. Replace "1" with the number of your card determined above. <br />
> #### defaults.pcm.card 1 <br />
> #### defaults.ctl.card 1 <br />

## Setup crontab
Open crontab <br />
> #### crontab -e  <br />
Add this line at the bottom (make sure there is a space between the * symbols) to run the program every minute  <br />
> #### * * * * * /home/pi/schoolbell.py  <br />

## Setup crontab for Christmas tunes
This will start script from 08:20-08:48, 10:31-10:43, 13:16-13:40
20 08 * * * /home/pi/random_playlist.py -t 28 /home/pi/winter/pl.xspf  <br />
31 10 * * * /home/pi/random_playlist.py -t 12 /home/pi/winter/pl.xspf  <br />
16 13 * * * /home/pi/random_playlist.py -t 24 /home/pi/winter/pl.xspf  <br />

## Credit for sound clips:
nextperiod.wav - https://freesound.org/people/Jackalgirl/sounds/683750/ <br />
warn.wav - https://freesound.org/people/Benboncan/sounds/93646/ <br />
quickchime.wav - https://freesound.org/people/kwahmah_02/sounds/245956/ <br />
longchime.wav - https://freesound.org/people/mpaol2023/sounds/370182/ <br />

sqbell - Squarepusher - Tommib <br />
s1bell - Prince Jazzbo - School <br />




