# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "C:\\Users\\CB Shukla\\Desktop\\Python Youtube" #to_do

# link of the video to be downloaded

'''***  IMPORTANT  ***'''
print("\n"+"*"*40+"GREETINGS MAMA JI"+"*"*40)
print("\nEnter the Youtube video link : ")
link=input()

print("\nHere are the available formats :-\n")

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.streams#.filter(progressive = True)
string = list(i for i in str(mp4files).split(','))
for i in string:
        print(i)

print("\nPlease input the itag of the desired format : ")
itags = int(input())
# get the video with the extension and
# resolution passed in the get() function


'''***  IMPORTANT  ***'''
d_video = mp4files.get_by_itag(itags)


try:
	# downloading the video

	print("\nDOWNLOADING... PLEASE WAIT")
	'''***  IMPORTANT  ***'''
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('\nTask Completed.\nPress any key to exit')
input()
