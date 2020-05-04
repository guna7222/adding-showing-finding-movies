MENU_PROMPT = "\n enter 'a' to add a movie, 'l' to list the movies, 'f' to find movies, 'q' to quit:"
movies = []

def add_movies():
    title = input("enter movie name")
    rating = int(input("enter rating"))
    ticket_pricing =int(input("enter ticket_pricing"))

    movies.append({
         "title":title,
         "rating":rating,
        "ticket_pricing":ticket_pricing
        }
          )
    
def list_movies_avaliable():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
      print(f"Title:{movie['title']}")
      print(f"Rating:{movie['rating']}")
        
def find_movie():
    search_title = input("enter movie name what you are searching for")
    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)


selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == 'a':
        add_movies()
    elif selection == 'l':
        list_movies_avaliable()

    elif selection == 'f':
        find_movie()
    else:
        print("unknow command, please try again")

    selection = input(MENU_PROMPT)
        
