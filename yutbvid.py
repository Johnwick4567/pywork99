# to import Youtube videos from library of python.
import pytube
x = int(input("do you want to download a youtube video, enter 1 if yes, 0 if no: "))
while x == 1:
    # ask for the url of the video
    url = input("Enter the Url of the video.... ")

    # specify the storage path of the video
    path = "D:"

    # main line to download the video
    pytube.YouTube(url).streams.get_highest_resolution().download(path)
    y = int(input("would you like to download another video, enter 1 if yes, 0 if no... "))
    if y == 1:
        continue
    x -= 1
    print("Process finished enjoy watching the video.... :)")
    print("goodbye.")
if x == 0:
    print("process terminated... :(")
