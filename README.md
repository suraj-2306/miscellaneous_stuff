# miscellaneous_stuff
Small scripts or conifgs to make life easier

## 1. Paper_extractor
  - This is based off [scihub.py](https://github.com/zaytoun/scihub.py). I'd suggest you to go through it for thorough understanding of how the pdf are scraped.
  - This works for Ieee and springer papers.
  - I've added another script to help you with autorenaming the downloaded pdfs.
### Usage
  - Install all the dependencies by `pip3 install -r dependencies.txt`
  - Call scihub `python3 /path/to/scihub.py -d "The url of the pdf" -o "output directory"`
  - Then call the name.py to scrape the title from the pdf and rename the file with it.  - `python3 /path/to/name.py -o "ouput directory"`
### Known Issues
  - Dont have other pdf's in the present folder when you call name.py. This may rename it unnecessarily.
  - Not all websites work.


## 2. Xilinx_ISIM_terminal
  - This is to access xilninx toolchain and build a simulation, all from the terminal
  - The file structure will be something like [this](https://pasteboard.co/JKI1HDe.png)
  - All the sources, i.e all user defined files such as all verilog files and cmd file for ISIM simulation go to the sources directory.
  - A custom makefile calls the recipe and creates a folder called isim.
### General Guidelines
  - Always keep the prj folder updated of all the files created. Follow a bottom up approach while ordering the verilog files in the prj file.
  - Create a normal project from ise and try matching the files in case of errors. Update the makefile if required.
  - The top is usually test_bench for all the modules that follow. Make sure that this has the same name as the prj file.
### Configuration (Important)
  - Change the path, in top.prj as to fetch the `glbl.v` correctly in the xilinx installation folders.
  - Source the xilinx configitation (the settings64.sh or settings32.sh), else you might encounter errors.
### Usage
  - Navigate to the top of the directory of the project.
  - Call the makefile. For example `make -f xilinx.makefile CUSTOM_TOP=top`.
  - As already mentioned, the "top" file which is the project filename as well as the top testbench file name. So if you would wanna change the name of top file, remember to change the prj file and the `CUSTOM_TOP=some_cutom_name`, while calling the makefile.
  - Call `make -f xilinx.makefile CUSTOM_TOP=top -s simulate` for simulating the modules. Check out the makefile for more options.

## 3. Kite + youcompleteme + vim 
  - This is for using kite only for python and using ycm for other extension files, Add this into your vimrc
  - `if(expand('%:t')!='py') let g:ycm_auto_trigger=1 endif`

## 4. MPI course Scraper
  - This can be used to scrape all the files in [this page](https://sanjayvidhyadharan.in/Downloads/Microprocessors/)
  - Navigate to a directory and put this in the terminal. `wget --recursive --html-extension --page-requisites --convert-link -np --reject html,robots.txt -c -N -X _autoindex -X robots.txt https://sanjayvidhyadharan.in/Downloads/Microprocessors/`
  - This updates the existing files. So you need to run this whenever there's a new file uploaded. 
  - Add this to the bash_alias file, and map it to an alias.

## 5. Tool for monitoring internet Usage in linux
  - Add `alias ius="sudo vnstat --oneline | cut -d ';' -f 11"` to the bash_aliases. 
  - Refer [this](https://www.tecmint.com/install-vnstat-and-vnstati-to-monitor-linux-network-traffic/) for installation of vnstat
  - This will poll for the usage of internet through Wifi and Ethernet, and give you the usage for the current month in interval of 5 minutes.
## 6. Offline conversion of files
  - Libre office has a cli tool to convert files.
  - `libreoffice --headless --invisible --convert-to convert_to_format file_name.extension`. add it to your ~/.bash_aliases
## 7. Drive_video_downloader
  - It uses 2 cookies and the video id as parameters.
### Usage 
  - `python3 video_downloader --file_id XXX --drive_id YYY --drive_stream ZZZ`
  -  `XXX` is the field in `https://drive.google.com/file/d/XXX/view`
  -  `YYY` is the ` __Secure-3PSID` cookie
  -  `ZZZ` is the ` DRIVE_STREAM` cookie
## 8.Cowin_data_logger
  - A bot to send you a mail if there is a vaccine available in your district for 18+ group.
  - Add it as a daily cron job in your pc.
### Usage
  - The script to be run is scraper.py in cowin_data_logger folder
  - Steps to find a app password from your gmail account.
    - go to manage my [google account](https://myaccount.google.com/security)
    - Under "Signing in to Google" confirm that "2-Step Verification" is "On" for the account.
    - Also under "Signing in to Google" Select "App passwords".
    - Select the app as "Mail" and the device as "Other (Custom name)" and name it.
    - Copy the app password, it will be in a yellow box and looks like: "XXXX XXXX XXXX XXXX"
  - Remember to find the district_id of your city and update it in the file
## 9.youtube_playlist_script
  - It can be used to make a copy of your favourite playlist (configuration copy and not download the videos) from youtube. You can open that on your favourite media player without ads or distraction :)  
  - Desc: A script to make a offline playlist of youtube playlists. 
  - It creates a .xspf as a playlist file, it is compatible with most media players.
### Prereq
  - xspf parser library : `pip3 install xspf-lib`
  - command line javascript utitly : `sudo apt-get install js`
  - youtube-dl : `pip3 install youtube-dl` or `sudo apt-get install youtube-dl`
### Usage
  - Use the config.yaml file to fill the details of your playlist.
    - For example a playlist ID of the link "https://www.youtube.com/playlist?list=PL8BC75818022EC4CA" is PL8BC75818022EC4CA
    - Similarly playlist ID of the link "https://www.youtube.com/watch?v=8ZYXks8pySE&list=PL8BC75818022EC4CA&index=1" is also PL8BC75818022EC4CA
  - Other parameters are self explanatory
    - If the track_title is not specified, it defaults to playlist_title
  - Run the playlist.py 
 
