from pytube import YouTube
from math import floor
from os import rename, chdir, system as os_system


chdir("/storage/emulated/0/Download")

def progress(stream, chunk, byts):
	dloaded =  ( int(file_to_download.filesize)- int(byts) )  // 1000000
	print("Downloaded: ","{:.2f}".format(dloaded) ,"MB", end="\t\t")


def downloader():
	global file_to_download
	link = input("Enter video link : > ")
	typ = ""
	print("Getting Info....")
	yt  = YouTube(link)

	ttle = yt.title
	print(ttle)
	stream = yt.streams

	print("Generating available streams to  download video...")
	s = {}
	for i in range(len(stream)):
		s[i] =  stream[i]


	print("Available formats to download are : ")
	for keys in s.keys():
		print(keys, f"{s[keys].type, s[keys].subtype}",s[keys].resolution, "Size approx: ",floor(int(s[keys].filesize)//1000000),"MB")
		print(".")

	stm = input("Enter stream number to download (e.g.  0,1,2...  better to avoid webm files..) :> ")

	file_to_download = s[int(stm)]
	print(f"You selected to download >> {file_to_download.type} Resolution {file_to_download.resolution} Size: {floor(int(file_to_download.filesize) // 1000000)}","MB")

	typ = file_to_download.type
	print("downloading....", typ)


	yt.register_on_progress_callback(progress)
	file_to_download.download()

	print("\n\n\n File Downloaded! and saved in the same Downloads folder")
	input()


info = """
 ====================================
| Elvishaa YouTube Video Downloader  | 
 ====================================

Join Telegram channel :  Tkinter Python GUI
YouTube								:  Not A Pro Bro!

"""

options = """
	Enter : \n \t1 to Download Video \n \t2 To exit \n 3 to update pytube library

"""

def update_lib():os_system("pip install --upgrade pytube")


while True:
	print(info)
	print(options)
	i = input("Choice :> ")
	if i == "1":
		downloader()
	elif i =="2":
		break
	elif i == "3":
		update_lib()
		continue

	else:
		pass

	print("\n"*100)
l --upgrade pytube")


while True:
	print(info)
	print(options)
	i = input("Choice :> ")
	if i == "1":
		downloader()
	elif i =="2":
		break
	elif i == "3":
		update_lib()
		continue

	else:
		pass

	print("\n"*100)
