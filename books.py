books = {'zake ahmed': ['Book1', 'Book2','Book3'], 'ryan wright': ['Book4','Book5']}


autor = input('Please input the autor you want to search ')


print(", ".join(books[autor.lower()]))