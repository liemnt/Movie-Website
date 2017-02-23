import fresh_tomatoes
import media
sing = media.Movie("Sing","About Animal Singer","http://www.impawards.com/2016/posters/sing_ver9_xxlg.jpg","https://www.youtube.com/watch?v=Y7uGHY-t80I")
avatar = media.Movie("Avatar","A marine on an alien planet","http://pre03.deviantart.net/3cb2/th/pre/i/2011/058/8/8/avatar_jake_and_neytiri_poster_by_remus09-d3aiukt.jpg", "https://www.youtube.com/watch?v=d1_JBMrrYw8")
school_of_rock = media.Movie("School Of Rock","Using rock music to learn","https://fanart.tv/api/download.php?type=download&image=79534&section=3","https://www.youtube.com/watch?v=XCwy6lW5Ixc")
ratatouille = media.Movie("Ratatouille","A rat is a chief in Paris","http://www.pixartalk.com/wp-content/uploads/2009/06/ratus1.jpg","https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight In Paris","Going back in time to meet authors","http://www.impawards.com/2011/posters/midnight_in_paris_xlg.jpg","https://www.youtube.com/watch?v=FAfR8omt-CY")
hunger_games = media.Movie("Hunger Game","A really real reality show","http://cdn.collider.com/wp-content/uploads/the-hunger-games-mockingjay-part-1-final-poster.jpg","https://www.youtube.com/watch?v=4S9a5V9ODuY")
movies = [sing,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]
fresh_tomatoes.open_movies_page(movies)

