from pytube import Youtube

def videosearch(vlink,format,filepath,quality):
    try:
        yt_obj=Youtube(vlink)

        if(format==mp4):
            dvideo(format,filepath,quality)
        else:
            daudio(format,filepath)
    except Exception as e:
        print(e)



def dvideo(format,filepath,quality):
    filters = yt_obj.streams.filter(progressive=True,filetype=format)
    if quality=='high':
        filters.get_highest_resolution().download(filepath)
    else:
        filters.get_lowest_resolution().download(filepath)

def daudio(format,filepath):
    yt_obj.streams.get_audio_only().download(output_path=filepath, filename='audio')
