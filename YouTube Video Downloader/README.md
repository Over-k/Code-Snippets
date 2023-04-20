# YouTube Video Downloader
A simple Python script to download YouTube videos and playlists using the pytube library.

## Installation
Install the required libraries using pip:
``
pip install pytube
``

## Usage
Add the video or playlist links to the links.txt file, with one link per line.

Run the youtube-downloader.py script:
``
python youtube-downloader.py
``
The script will download all videos that are not already in the downloaded.txt file, which is used to keep track of downloaded videos.

## Customization
You can customize the download location by changing the path in the
``
downloads_directory = r"C:\Users\Unnamed\Downloads"
``

You can also customize the progress bar by modifying the on_progress() function.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue if you have any suggestions or bug reports.

# License
This project is licensed under the MIT License.
