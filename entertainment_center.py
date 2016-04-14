import fresh_tomatoes
import media

pizza = media.Movie("Pizza",
                    "Michael Karthikeyan (Vijay Sethupathi) is a pizza delivery boy who lives with his girlfriend Anu (Remya Nambeesan).",
                    "http://keralapals.com/wp-content/uploads/2012/12/pizza-tamil-to-hindi.jpg",
                    "https://www.youtube.com/watch?v=1ORbkrHs5JU"
                    )

breakin = media.Movie("Breakin'",
                      "Kelly is a struggling young jazz dancer and, through her friend Adam, she is introduced to two Street dancers, Ozone and Turbo.",
                      "https://upload.wikimedia.org/wikipedia/en/a/ae/Breakin'_movie_poster.jpg",
                      "https://www.youtube.com/watch?v=NUPNFLIhMag")

opera_jawa = media.Movie("Opera Jawa",
                         "Trouble follows when a wealthy butcher (Eko Supriyanto) falls in love with the wife (Artika Sari Devi) of a poor potter (Martinus Miroto)",
                         "https://www.cinematerial.com/media/posters/md/k8/k8pi4ktw.jpg?v=1456826276",
                         "https://www.youtube.com/watch?v=3D39grpg7Rs")

akira = media.Movie("Akira",
                    "In 1988, a psychic explosion destroys Tokyo and initiates World War III",
                    "http://static.zerochan.net/AKIRA.(Ootomo.Katsuhiro).full.471268.jpg",
                    "https://www.youtube.com/watch?v=FtPhrCTjMtQ")

sholay = media.Movie("Sholay",
                    "In the small village of Ramgarh, the retired policeman Thakur Baldev Singh (Sanjeev Kumar) summons a pair of small-time thieves that he had once arrested. ",
                    "http://static.koimoi.com/wp-content/new-galleries/2013/11/Sanjeev-Kumar-in-a-Sholay-3D-movie-poster.jpg",
                    "https://www.youtube.com/watch?v=hLhzpe3_V_g")

battle_wizard = media.Movie("The Battle Wizard",
                            "1977 Hong Kong film adapted from Louis Cha's novel Demi-Gods and Semi-Devils.",
                            "http://ecx.images-amazon.com/images/I/517MFoko8PL._SY445_.jpg",
                            "https://www.youtube.com/watch?v=asdLkfFnLQ0")
movies = [pizza, breakin, opera_jawa, akira, sholay, battle_wizard]
fresh_tomatoes.open_movies_page(movies)
