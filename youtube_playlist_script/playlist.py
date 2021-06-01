#! /usr/bin/python3

import os
import xspf_lib as xspf
import yaml


with open("config.yaml", "r") as config:
    data = yaml.safe_load(config)
    data = data["playlist_config"]
    creator_name=data["creator_name"]
    playlist_id = data["playlist_id"]
    playlist_title = data["playlist_title"]
    track_title = data["track_title"]

    if not track_title:
        track_title = playlist_title


def download_video_links(playlist_id):
    playlist_link = 'https://www.youtube.com/playlist?list=%s' % playlist_id
    command = "youtube-dl -j --flat-playlist '%s' | jq -r '.id' | sed 's_^_https://www.youtube.com/watch?v=_' > result.log" % playlist_link
    os.system(command)


def make_xspf(track_title,creator_name,playlist_title):
    result_file = open('result.log', 'r')
    Lines = result_file.readlines()
    count = 0
    playlist_name = []

    for line in Lines:
        command = "youtube-dl --get-title  '%s'" % line
        title = os.popen(command).read()
        title = title.strip('\n')
        print(count)

        fileconfig = xspf.Track()
        fileconfig.location = ["%s" % line.strip('\n')]
        print(fileconfig.location)
        fileconfig.title = str(title)
        playlist_name.append(fileconfig)
        count = count + 1

    playlist = xspf.Playlist(
        title=track_title, creator=creator_name,  trackList=playlist_name)
    playlist_title = "%s.xspf" %playlist_title
    playlist.write(playlist_title)


def main():
    download_video_links(playlist_id)
    make_xspf(track_title,creator_name,playlist_title)


if __name__ == "__main__":
    main()
