import webbrowser

class Movie(object):
	""" This class contains information about the movie 
	and can also show a trailer.

	Attributes:
		movie_title: A string with the movie title
		movie_poster: A link to an image of the movie poster
		trailer_youtube: A link to the youtube trailer of the movie
	"""

	def __init__(self, movie_title, movie_poster, trailer_youtube):
		""" Initialisation of a new movie instance """
		self.title = movie_title
		self.poster_image_url = movie_poster
		self.trailer_youtube_url= trailer_youtube


	def show_trailer(self):
		""" Plays the trailer of the movie instance """
		webbrowser.open(self.trailer_youtube_url)


