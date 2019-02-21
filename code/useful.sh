#!/usr/bin/env bash
#takes first arguement (URL of video) and downloads 
#best quality available using youtube-dl

VIDEO=$1
#checks if youtube-dl is installted, if not then installs it using apt
if apt-cache policy youtube-dl | grep none ; then

	sudo apt-get install youtube-dl
	echo "youtube-dl installed"
else
	echo "youtube-dl already installed"
fi
echo "Downloading requested video at max quality"
youtube-dl ${VIDEO} -f bestvideo+bestaudio --merge-output-format mkv
