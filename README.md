# HandleTracksQuality
If you want to check fastly if your tracks are 320 Bitrate Quality for DJ Mixing

# Prerequisite

pip install mutagen

pydub need libraries to execute some operations in order to analyse your tracks

To download ffmpeg, follow these steps:

Go to the official ffmpeg website at https://ffmpeg.org/ and click on the "Download" link to access the download page. Under the "Windows" section, you will find links to static builds of ffmpeg for Windows. Choose the version that matches your system (32-bit or 64-bit) and click on the link to download the ZIP file.

Extract the ZIP file: After downloading the ffmpeg ZIP file, extract it to a location of your choice on your system.

Add ffmpeg to the PATH environment variable: In order for ffmpeg to be accessible from any location on your system, you need to add the path to the folder containing the ffmpeg files to the "PATH" environment variable. Here are the steps to do it:

Right-click on "This PC" (or "Computer") and select "Properties".
Click on "Advanced system settings" in the left pane.
In the "System Properties" window, click on the "Environment Variables" button.
In the "System variables" section, select the "PATH" variable and click on the "Edit" button.
Add the full path to the ffmpeg folder (e.g., C:\path\to\ffmpeg\bin) to the list of paths. If the "PATH" variable does not exist, you can create it by clicking on the "New" button and entering "PATH" as the variable name and the full path to the ffmpeg folder as the value.
Click "OK" to save the changes.
Verify the installation: Open a new terminal (command prompt) window and type the command ffmpeg. If ffmpeg is properly installed and added to the PATH, you should see the ffmpeg version displayed in the terminal.


