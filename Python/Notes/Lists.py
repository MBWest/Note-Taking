#LISTS - MUTABLE [0,1,2,3,...]------------------------------------------------------------

movies = ["When Harry Met SAlly", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1]) #Returns the second item in the list
print(movies[0]) #Returns the first item in the list
print(movies[1:3]) #Returns the first index number given right until the last number, but not include the last number
print(movies[1:]) #Returns the first index through the rest of the list
print(movies[:1]) #Returns only the items before the first index
print(movies[-1]) #Returns last item in list

print(len(movies)) #Print length of movies list

movies.append("JAWS") #Appends to the end of the list

print(movies[-1])  #Returns last item in list

movies.insert(2,"Hustle") #Insert Hustle into index 2 of the List

movies.pop() #Removes the last item in the movies list
movies.pop(0) #Removes the first item in the movies list
print(movies) #Prints the movie list

amber_movies = ['Just Go With It', '50 First Dates'] 

our_favorite_movies = movies + amber_movies

print(our_favorite_movies)

grades = [['bob', 82], ['Alice', 90], ['Jeff', 90]]

bob_grades = grades[0][1] #Display Bobs grades
print(bob_grades) #Print Bobs grades
grades[0][1] = 83 #Change bobs grade
print(grades) #Print grades