import media
import fresh_tomatoes


kluay = media.Movie("Khan Kluay", 
	"https://upload.wikimedia.org/wikipedia/en/7/77/Khankluay.jpg", 
	"https://www.youtube.com/watch?v=DsmWluXpLQw")

kluay2 = media.Movie("Khan Kluay 2", 
	"http://2.bp.blogspot.com/-bR_dJ4QJgOM/VDE_RLm56UI/AAAAAAAABNU/w0mbiGsr56w/s1600/khan%2Bkluay%2B2%2Bposter.jpg", 
	"https://www.youtube.com/watch?v=crZ8xm0msH4")

toy_story = media.Movie("Toy Story", 
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", 
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=d1_JBMrrYw8")

despicable = media.Movie("Despicable Me", 
	"https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
	"https://www.youtube.com/watch?v=TZkAcKCFIVo")

ice_age = media.Movie("Ice Age", 
	"https://upload.wikimedia.org/wikipedia/en/3/3c/Ice_Age_%282002_film%29_poster.jpg", 
	"https://www.youtube.com/watch?v=wjdqn9r4thg")


if __name__ == '__main__':

	# Create a list of the movies
	movies = [kluay, kluay2, toy_story, avatar, despicable, ice_age]

	# Open the fresh tomatoes movie webpage
	fresh_tomatoes.open_movies_page(movies)