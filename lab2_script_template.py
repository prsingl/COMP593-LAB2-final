def main():
    about_me = {
        "full_name": "Priyanshu Singla"
        "Student_ID": "10312293"
        "pizza_toppings": ["ONIONS", "TOMATO", "PEPPERS"],
        "movies": [
            {
                "title": "zoolander",
                "genre": "comedy"
            },
            {
                "title": "back to the future"
                "genre": "sci-fi"
            }
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {"title": "anchorman", "genre": "comedy"}


# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    Student_ID = about_me["student_ID"]
    print(
        f"My name is {full_name}, but you can call me Sir {first_name}./nMy student ID is {student_ID}."
    )
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()