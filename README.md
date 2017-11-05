# ud036_StarterCode -- Movie Trailer

## Synopsis
This Movie Trailer project is the first project of the Full Stack Web Develper course of Udacity.
This project cotaines the source code for a website showing movie trailers.

## Prerequisites
This project was written in Python 2.7.14 and only uses PSL.
### Linux Instructions
Make sure you have installed python 2.7.X
Open a terminal commandline and enter:
`python -V`
else follow your distribution instruction to install python 2.7.X

## How to install
### Linux Instructions
Open a terminal command line and enter:
`git clone https://github.com/tordne/ud036_StarterCode.git`

## How to run the site
### Linux Instructions
Open a terminal command line and go to the projects directory:
`cd /home/XXX/ud036_StarterCode`
then to run the website:
`python entertainment_center.py`
This will open a new tab in your webbrowser which will be the website.

## Project contents
### media.py
This file contains th Movie class, which will need several attributes
* Movie Title
* Movie Poster Link
* Movie Trailer Link

There is also one method which will open the link of the movie trailer in a webbrowser.
`Movie.show_trailer()`

### entertainment_center.py
This file contains all the Movie Instances, please feel free to remove and add your movies by using the movie class with the following syntax:
```
# Khan Kluay movie: movie title, poster image, movie trailer
kluay = media.Movie(
    "Khan Kluay", 
    "https://upload.wikimedia.org/wikipedia/en/7/77/Khankluay.jpg", 
    "https://www.youtube.com/watch?v=DsmWluXpLQw"
    )
```

Within the **__main__** there is one list variable **movies** which will contain all the movies that will be used on the HTML page.
