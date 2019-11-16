#!/usr/bin/python3
import textwrap
import subprocess
import os
import platform
import httpimport
import getopt
import textwrap
import argparse

#Downloading Modules
print("Downloading Addons")
os.system("wget https://download1324.mediafire.com/djtqtv9yuhyg/kqtyfyrzwlxd996/speedvideo.py")
os.system("wget https://download853.mediafire.com/52ynclmz60yg/ernhf1d7hsvc0h6/streamsite.py")
#Importing SpeedVideo Catcher
import sys
sys.path.append('')

from speedvideo import speedVideo

#Colors = print(bcolors.example + "urmom" + bcolors.ENDC)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#Main
def main():
	print(bcolors.OKBLUE + "Mr. Robot Downloader\n" + bcolors.ENDC)
	print(bcolors.OKGREEN + "	By Denis Sossich\n" + bcolors.ENDC)
main()

site = speedVideo()

print(bcolors.OKBLUE + "This script was made thanks to the CatchTheStream Python Module for SpeedVideo Streaming (work as a grabber) imported remotely by httpimport Python Module from a webhost called anonfile.com with the zipped file uploaded containing the module taken from CatchTheStream GitHub Repository (https://github.com/davidezanella/CatchTheStream/blob/master/speedvideo.py)\n" +bcolors.ENDC)


### Help ###
#parser = argparse.ArgumentParser()
#parser.add_argument("--help", help="show help",
#                    action="store_true")
#args = parser.parse_args()
#if args.help:
#	print(bcolors.OKBLUE + "Arguments: " + bcolors.ENDC)
#print(bcolors.WARNING + "--help\n [Show this output]\n" + bcolors.ENDC)
#print(bcolors.WARNING + "--seasonone\n [Download Season One in ITA]." + bcolors.ENDC)
#print(bcolors.WARNING + "--seasontwo\n [DOwnload Season Two in ITA].\n" + bcolors.ENDC)
#print(bcolors.WARNING + "--seasonthree\n [Download Season Three in ITA].\n" + bcolors.ENDC)
#print(bcolors.WARNING + "--seasonfour\n [Download Four Four in ITA].\n" + bcolors.ENDC)
#print(bcolors.WARNING + "--info\n [Information about this script and his costruction.]" + bcolors.ENDC)

## Season One
print("Cercando lo stream degli episodi...")

#Stagione 1
stream = site.getStreamUrl("https://speedvideo.net/embed-psah8bc90040.html")
stream2 = site.getStreamUrl("https://speedvideo.net/embed-hvi6qv052j1l.html")
stream3 = site.getStreamUrl("http://speedvideo.net/embed-nn7f303f6aqk.html")
stream4 = site.getStreamUrl("http://speedvideo.net/embed-8365y7e458jr.html")
stream5 = site.getStreamUrl("http://speedvideo.net/embed-wqdsrqafd018.html")
stream6 = site.getStreamUrl("http://speedvideo.net/embed-38oasshz5mi9.html")
stream7 = site.getStreamUrl("http://speedvideo.net/embed-9pym6e282s47.html")
stream8 = site.getStreamUrl("http://speedvideo.net/embed-6s2jkv7864ou.html")
stream9 = site.getStreamUrl("http://speedvideo.net/embed-88v972gs340b.html")
stream10 = site.getStreamUrl("http://speedvideo.net/embed-f6677fixfap6.html")
#
print("Trovato!\n")
print("Download in corso della Prima Stagione...\n")

#Download degli episodi
os.system('%s %s' % ('wget -O S01E01.mp4', stream))
os.system('%s %s' % ('wget -O S01E02.mp4', stream2))
os.system('%s %s' % ('wget -O S01E03.mp4', stream3))
os.system('%s %s' % ('wget -O S01E04.mp4', stream4))
os.system('%s %s' % ('wget -O S01E05.mp4', stream5))
os.system('%s %s' % ('wget -O S01E06.mp4', stream6))
os.system('%s %s' % ('wget -O S01E07.mp4', stream7))
os.system('%s %s' % ('wget -O S01E08.mp4', stream8))
os.system('%s %s' % ('wget -O S01E09.mp4', stream9))
os.system('%s %s' % ('wget -O S01E010.mp4', stream10))

## Season Two

#Seconda Stagione Stream URL's
stream = site.getStreamUrl("http://speedvideo.net/embed-9p5r58y46n17.html")
stream2 = site.getStreamUrl("http://speedvideo.net/embed-568j87snjm97.html")
stream3 = site.getStreamUrl("http://speedvideo.net/embed-k2nl0b4l5626.html")
stream4 = site.getStreamUrl("http://speedvideo.net/embed-c26wiegrwj57.html")
stream5 = site.getStreamUrl("http://speedvideo.net/embed-902917926q42.html")
stream6 = site.getStreamUrl("http://speedvideo.net/embed-33v30l1hcl9l.html")
stream7 = site.getStreamUrl("http://speedvideo.net/embed-vji1pgko942j.html")
stream8 = site.getStreamUrl("http://speedvideo.net/embed-g035u7123hpa.html")
stream9 = site.getStreamUrl("http://speedvideo.net/embed-bw5p93xt191q.html")
stream10 = site.getStreamUrl("http://speedvideo.net/embed-ugyd0w8gl2x7.html")
stream11 = site.getStreamUrl("http://speedvideo.net/embed-kfz9jb45i711.html")
stream12 = site.getStreamUrl("http://speedvideo.net/embed-p0t1r7xv44b0.html")

#Download degli episodi
print("Download della Seconda Stagione\n")
os.system('%s %s' % ('wget -O S02E01.mp4', stream))
os.system('%s %s' % ('wget -O S02E02.mp4', stream2))
os.system('%s %s' % ('wget -O S02E03.mp4', stream3))
os.system('%s %s' % ('wget -O S02E04.mp4', stream4))
os.system('%s %s' % ('wget -O S02E05.mp4', stream5))
os.system('%s %s' % ('wget -O S02E06.mp4', stream6))
os.system('%s %s' % ('wget -O S02E07.mp4', stream7))
os.system('%s %s' % ('wget -O S02E08.mp4', stream8))
os.system('%s %s' % ('wget -O S02E09.mp4', stream9))
os.system('%s %s' % ('wget -O S02E10.mp4', stream10))
os.system('%s %s' % ('wget -O S02E11.mp4', stream11))
os.system('%s %s' % ('wget -O S02E12.mp4', stream12))

## Season Three
#Get stream url
print("Download della Terza Stagione\n")
stream = site.getStreamUrl("http://speedvideo.net/embed-4x3pezz161xz.html")
stream2 = site.BBgetStreamUrl("http://speedvideo.net/embed-726nywtz6b85.html")
stream3 = site.getStreamUrl("http://speedvideo.net/embed-c83sz38zwsop.html")
stream4 = site.getStreamUrl("http://speedvideo.net/embed-6bnspwcsh9a1.html")
stream5 = site.getStreamUrl("http://speedvideo.net/embed-464ys4xag9k8.html")
stream6 = site.getStreamUrl("http://speedvideo.net/embed-la9945bthevj.html")
stream7 = site.getStreamUrl("http://speedvideo.net/embed-ggaz5bv179m5.html")
stream8 = site.getStreamUrl("http://speedvideo.net/embed-p5li6s95r8ei.html")
stream9 = site.getStreamUrl("http://speedvideo.net/embed-5qq0l1e9s859.html")
stream10 = site.getStreamUrl("http://speedvideo.net/embed-w081976l9ka6.html")

#Download all links
os.system('%s %s' % ('wget -O S03E01.mp4', stream))
os.system('%s %s' % ('wget -O S03E02.mp4', stream2))
os.system('%s %s' % ('wget -O S03E03.mp4', stream3))
os.system('%s %s' % ('wget -O S03E04.mp4', stream4))
os.system('%s %s' % ('wget -O S03E05.mp4', stream5))
os.system('%s %s' % ('wget -O S03E06.mp4', stream6))
os.system('%s %s' % ('wget -O S03E07.mp4', stream7))
os.system('%s %s' % ('wget -O S03E08.mp4', stream8))
os.system('%s %s' % ('wget -O S03E09.mp4', stream9))
os.system('%s %s' % ('wget -O S03E10.mp4', stream10))

## Season Four
#Get stream url
stream = site.getStreamUrl("http://speedvideo.net/embed-05caln186rf1.html")
stream2 = site.getStreamUrl("http://speedvideo.net/embed-y9r1428j16zu.html")
stream3 = site.getStreamUrl("http://speedvideo.net/embed-x8q95qp8br46.html")
stream4 = site.getStreamUrl("http://speedvideo.net/embed-6a895106hp2v.html")
stream5 = site.getStreamUrl("http://speedvideo.net/embed-7dpk8j97hm59.html")
stream6 = site.getStreamUrl("http://speedvideo.net/embed-5388ve7w28c4.html")

#Download all links
os.system('%s %s' % ('wget -O S04E01.mp4', stream))
os.system('%s %s' % ('wget -O S04E02.mp4', stream2))
os.system('%s %s' % ('wget -O S04E03.mp4', stream3))
os.system('%s %s' % ('wget -O S04E04.mp4', stream4))
os.system('%s %s' % ('wget -O S04E05.mp4', stream5))
os.system('%s %s' % ('wget -O S04E016.mp4', stream6))
print("")
print(bcolors.OKGREEN + "Download completato, ora hai tutte le stagioni di Mr. Robot in locale" + bcolors.ENCD)
exit()
#Fine dello script
mainmenu()
