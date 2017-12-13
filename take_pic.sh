#!/bin/bash
for ((i=1; i<=25; i++))
	do
		fswebcam -r 640x480 --no-banner gray/image$i.jpg
	done
