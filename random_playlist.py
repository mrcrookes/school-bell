#!/usr/bin/python3

import argparse
from vlc_player import VLC
from random import shuffle
from xspf_lib import Playlist
from time import sleep

def prune(tracks, time=0):
    "randomly select tracks from a playlist until time limit (in ms) is exceeded"
    new_tracks = []
    shuffle(tracks)
    total_time = 0
    for track in tracks:
        new_tracks.append(track)
        total_time += track.duration
        if 0 < time <= total_time:
            break
    return new_tracks

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            description='play files found in specified playlist in random order, up to a given time limit',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
            'file_path',
            help='path to playlist')
    parser.add_argument(
            '-r',
            '--remote',
            action="store_true",
            help='open a remote http interface')
    parser.add_argument(
            '-p',
            '--password',
            help='set password for remote interface. Default is "vlcremote". Implies -r')
    parser.add_argument(
            '-t',
            '--time',
            type=int,
            default=0,
            help='time limit (in minutes), 0 for no limit')
    args = parser.parse_args()


    playlist = Playlist.parse(args.file_path)
    time_in_s = args.time * 60
    if args.password:
        args.remote = True
    player = VLC(
            tracklist = prune(playlist.trackList, time_in_s*1000),
            remote = args.remote,
            password = args.password
            )
    player.play()
    #wait until playlist ends
    sleep(time_in_s)
    #if we're still going, keep waiting
    while player.is_playing():
        sleep(60)

    player.exit()
