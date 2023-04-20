from pytube import YouTube, Playlist

downloads_directory = r"C:\Users\Unnamed\Downloads"

def log_download(link):
    with open('downloaded.txt', 'a') as f:
        f.write(f"{link}\n")


def download_video(video_url):
    def on_progress(stream, chunk, bytes_remaining):
        percent = round(((1 - bytes_remaining / video.filesize) * 100), 1)
        print(f"\r[{percent}%]: {video.title}", end="")
        if percent % 10 == 0:
            print(f"\r[✔]: {video.title}     \n", end="")

    youtube_object = YouTube(video_url, on_progress_callback=on_progress)
    video = youtube_object.streams.get_highest_resolution()
    video.download(downloads_directory)


def get_video_links():
    video_links = []
    with open('links.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("https://www.youtube.com/watch?v="):
                video_links.append(line.strip())
            elif line.startswith("https://www.youtube.com/playlist?list="):
                playlist = Playlist(line.strip())
                video_links.extend(playlist.video_urls)

    video_links = list(set(video_links))
    downloaded_links = [link.strip() for link in open('downloaded.txt', 'r').readlines()]
    video_links = [link for link in video_links if link not in downloaded_links]
    print(f"Let's download all {len(video_links)} video(s)...")
    for link in video_links:
        try:
            download_video(link)
            log_download(link)
        except :
            print(f"[x]: {link}")

get_video_links()
