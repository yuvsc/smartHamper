#!/bin/bash
for ((i=1; i<=5; i++))
	do
		fswebcam -r 640x480 --no-banner image$i.jpg
	done
