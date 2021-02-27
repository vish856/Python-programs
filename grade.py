#Lists Challenge 6: Grade Sorter App
print("Welcome to the Grade Sorter App")
#Initialize list and get user input
grades = []
grades.append((input("what's you first grade(9-100) :")))
grades.append((input("what's you second grade(9-100) :")))
grades.append((input("what's you third grade(9-100) :")))
grades.append((input("what's you forth grade(9-100) :")))
print("\nYour grades are: " + str(grades))
#Sort the list from highest to lowest
grades.sort(reverse=True)
print("\nYour grades from highest to lowest are: " + str(grades))
#Removing the lowest two grades.
print("\nThe lowest two grades will now be dropped.")
removed_grade = grades.pop()
print("Removed grade: " + str(removed_grade))
removed_grade = grades.pop()
print("Removed grade: " + str(removed_grade))
#Recap remaining grades
print("\nYour remaining grades are: " + str(grades))
print("Nice work! Your highest grade is " + str(grades[0]) + ".")
