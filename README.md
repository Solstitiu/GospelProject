This program downloads Bible verses and saves them as images. It is written in Python 3 and uses the requests and os modules.

Getting Started
The following instructions will help you run the program on your local machine.

Prerequisites
The program requires the following modules:

requests
os
json
You can install these modules using pip:
pip install requests 
pip install json

Running the Program
  python gospel.py
change the main function if you want to run it just for one book at a time

How it Works
The program takes input from the user in the form of the name of the book of the Bible, the chapter number, and the verse numbers. It then downloads the specified verses and saves them as images.

The program uses the following API to retrieve the Bible verses:
https://bible-api.com/

The program then uses the following API to generate the images:
https://textoverimage.moesif.com/

Code Structure
The main.py file contains the main function of the program. It takes input from the user, calls the download_image() function to download the specified verses, and saves them as images.

The download_image() function takes the book name, chapter number, and verse numbers as input. It then retrieves the specified verses from the API, processes the text to fit on the image, and saves the image to the file system.

The create_payload() function takes the background image URL and the text as input and generates the API URL to generate the image.

Code Quality
The code is well structured and follows the PEP 8 style guide. The variable names are descriptive and the code is easy to read and understand. The program is well documented and includes instructions for installation and usage.

However, there is an issue with the file path for the book directory. The code currently assumes that the program is running on a Windows machine and uses backslashes (\) in the file path. This will cause the program to fail on other operating systems. To make the code more platform-independent, it is recommended to use forward slashes (/) instead.

Code Output:
get_verses('revelation') => new directory "revelation" => 22 sub directories one for each chapter of the book "revelation1" "revelation2" ... "revelation22" => jpg files numbered from 1 to n where n is the number of jpg files needed to contain the chapter.
![Untitled](https://user-images.githubusercontent.com/41898149/235352160-b5d659ee-f1a1-4d2d-bebc-025af8122a4d.png)
