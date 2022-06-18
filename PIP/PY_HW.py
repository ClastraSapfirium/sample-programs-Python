from pytube import YouTube

link = 'https://youtube.com/shorts/0nvR5qOG8nw?feature=share'

yt_obj = YouTube(link)

# for stream in yt_obj.streams:
#     print(stream)

filters = yt_obj.streams.filter(progressive=True, file_extension='mp_4')

for mp4_filter in filters:
    print (mp4_filter)