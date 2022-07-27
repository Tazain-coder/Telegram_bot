from urllib.request import urlopen
import re

def Song(search):
    search_query = search.split()

    final_query = "".join(search_query)
        
    search ='https://www.youtube.com/results?search_query={}'.format(final_query)

    html = urlopen(search)
    video_ids = re.findall("watch\?v=(\S{11})", html.read().decode())
    return "https://www.youtube.com/watch?v=" + video_ids[0]
    
