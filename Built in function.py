def parse_csv(file_path):
    """
    Parses a CSV file and returns a list of dictionaries.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    list: A list of dictionaries representing the rows in the CSV file.
    """
    movies = []
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the header line
        headers = file.readline().strip().split(',')
        
        for line in file:
            # Initialize an empty dictionary for the movie
            movie = {}
            # Split the line by comma, taking care of quoted fields
            fields = []
            field = ''
            in_quotes = False
            for char in line:
                if char == '"' and not in_quotes:
                    in_quotes = True
                elif char == '"' and in_quotes:
                    in_quotes = False
                elif char == ',' and not in_quotes:
                    fields.append(field.strip())
                    field = ''
                else:
                    field += char
            fields.append(field.strip())  # Add the last field
            
            # Create a dictionary for the movie
            for i, header in enumerate(headers):
                if i < len(fields):
                    movie[header] = fields[i].strip('"')
                else:
                    movie[header] = ''
            movies.append(movie)
    return movies

def sort_movies_by_director(file_path):
    """
    Sorts movies based on the director's name from a CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file containing the movie dataset.
    
    Returns:
    list: A sorted list of movies based on the director's name.
    """
    movies = parse_csv(file_path)
    return sorted(movies, key=lambda x: x['director'])

if __name__ == "__main__":
    # Replace this with your actual file path on your machine
    file_path =  r"C:/Users/sharo/OneDrive/Documents/Intro to informatics/imdb-movies-dataset.csv"
    sorted_movies = sort_movies_by_director(file_path)
    
    if sorted_movies:
        # Output the sorted movie list
        for movie in sorted_movies[:10]:  # Printing only the first 10 movies for brevity
            print(f"Title: {movie['title']}, Director: {movie['director']}")
    else:
        print("No movies found or error processing the data.")