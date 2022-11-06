import math
import random
# Vivian Procacci
# Program that asks the user various questions
print("Hello!" * 10)
# I print Hello! ten times to indicate that I'm excited to meet the user!
print(" I'm going to create a program that will pair YOU, to a disney "
      "character,based on your personality")
print('\nMy name is Vivian, and before we start, I would love to hear what '
      'your favorite disney character is!')
favorite_character = input("Enter your favorite disney character! :  ")
print("OMG you like",
      favorite_character,
      "that's a great choice!!")
birthday_month = int(input("\nBy the way, whens your birthday? Enter your "
                           "month in "
                           "the form mm : "))
birthday_day = int(input(" Enter your day in the form dd : "))
birthday_year = int(input(" Enter your day in the form yyyy : "))
# I asked the user to insert the month, day, and year, in order to print the
# birthday in the mm/dd/yyyy to show use of sep= argument
if birthday_year >= 2008:
    print("Your birthday is  ",
          birthday_month,
          birthday_day,
          birthday_year,
          " .... You're like 10 kid",
          sep='/')
elif 2008 > birthday_year >= 2012:
    print("Your birthday is  ",
          birthday_month,
          birthday_day,
          birthday_year,
          " .... You're still a youngin'",
          sep='/')
elif 2012 > birthday_year >= 1997:
    print("Your birthday is  ",
          birthday_month,
          birthday_day,
          birthday_year,
          " .... Oh so you're a Gen Z kid... Me too!!'",
          sep='/')
elif 1996 > birthday_year >= 1981:
    print("Your birthday is  ",
          birthday_month,
          birthday_day,
          birthday_year,
          " .... You're a millenial... How's the 'adulting' "
          "going",
          sep='/')
elif 1980 > birthday_year >= 1964:
    print("Your birthday is  ",
          birthday_month,
          birthday_day,
          birthday_year,
          " .... Hey you're around my Dad's age! ",
          sep='/')
elif 1963 > birthday_year >= 1946:
    print("Your birthday is  ",
          birthday_month,
          birthday_day,
          birthday_year,
          ".... You're not a boomer, you're a baby boomer!",
          sep='/')
else:
    print("Your birthday is  ",
          birthday_month,
          birthday_day,
          birthday_year,
          " .... BOOOOOOOOMER",
          sep='/')
# Let's plan a movie night!
# I used a while loop, and set the stop loop from running to False, until it
# hits the sentinel value: 00
sum_of_movies = 0
stop_loop_from_running = False

while not stop_loop_from_running:

    try:
        movie_menu_selection = int(input("Enter the number choice for what "
                                         "you "
                                         "would "
                                         "like "
                                         "to "
                                         "see\n1. Beauty and the Beast ("
                                         "1991)\n2. The Little Mermaid ("
                                         "1989) \n3. Mulan ( "
                                         "1998)\n4. Pocahontas (1995)\n5. "
                                         "Cinderella ( "
                                         "1950)\n To Exit,type 00 or 10\n"))
        if movie_menu_selection <= 5 and movie_menu_selection >= 1:
            print("You have called function number",
                  movie_menu_selection)
            # if 5 is greater than or equal to movie selection and greater
            # than or equal to 1 then print the movie selection
            sum_of_movies += 1
        elif movie_menu_selection == 00 or movie_menu_selection == 10:
            stop_loop_from_running = True
        elif movie_menu_selection > 5 and movie_menu_selection > 1:
            print("Invalid selection. Try again.")
    # Value error to excuse a bad input, and helps the loop to keep running
    except ValueError:
        print("Invalid selection. Try again.")
print("Wow,you want to watch",
      sum_of_movies,
      "movies from the list!")
# using the += operator I was able to add up the amount of movies the user
# chooses to watch.
print("\nNow let's plan a movie night ",
      end=' ')

minutes = input("Enter movie minutes!:  ")
number_of_minutes = int(minutes)
# input(minutes) is a string function so lets make sure
# that we convert to integers
hours = number_of_minutes // 60
# I used the floor division operator to round down numbers
remainder = number_of_minutes % 60
# I then used the modulus operator divided by 60 to get remaining am.
# minutes
print("Your movie is",
      hours,
      "hour",
      remainder,
      " minutes long!!")
# https://greenteapress.com/thinkpython2/html/thinkpython2006.html
# I figured out how to do the movie minutes to hours by an example in think
# python. From there I adjusted to fit the * operator and the ** operator
print("If you watched your movie 5 times, it would appromiately take you...",
      end=' ')
fivex_number_of_minutes = (number_of_minutes * 5)
# I calculated 5 times the amount of minutes by multliplying the amount of
# minutes by 5
fivex_number_of_hours = (fivex_number_of_minutes // 60)
fivex_remainer = (fivex_number_of_minutes % 60)
print(fivex_number_of_hours,
      "hours and",
      fivex_remainer,
      "minutes long!\nWow! thats a long time!!")
print("If you multiplied the amount of minutes of the movie by itself, "
      "it would take you",
      end=' ')
exponent_NOM = (number_of_minutes ** 2)
# Same concepts above, just taking movie minutes and multiplying it against
# itself
exponent_NOH = (exponent_NOM // 60)
exponent_remainder = (exponent_NOM % 60)
print(exponent_NOH,
      "hours and",
      exponent_remainder,
      "minutes... Geez, thats crazy! Who would spend that amount of time?!?!")
print("\nLets say youre having a movie night, and you want to watch the movie "
      "you inserted above and a \nnew movie....",
      end='')
print("Let's figure out how long the duration of the movie night is in hours "
      "and minutes!!")
second_minutes = input("Enter your second movie's minutes!:  ")
second_number_of_minutes = int(second_minutes)
total_minutes_movie_night = (second_number_of_minutes + number_of_minutes)

total_hour_movie_night = (total_minutes_movie_night // 60)
total_remainder_movie_night = (total_minutes_movie_night % 60)
if total_minutes_movie_night <= 200:
    print("Your movie night would be",
          total_hour_movie_night,
          "hours, and",
          total_remainder_movie_night,
          "minutes, that's a short one!")
elif total_minutes_movie_night > 200:
    print("Your movie night would be",
          total_hour_movie_night,
          "hours, and",
          total_remainder_movie_night,
          "minutes, that's a long one! Make sure you snuggle up with some "
          "blankets!")
else:
    print("Are you sure you're even watching a movie!")
print("Time is money, my friend! And money acquires compounded interest "
      "if you do it correctly!!\n If your total amount of minutes from the "
      "movie night, was money and you compounded interest 12 percent annually("
      "average index fund "
      "returns) for however years you choose, how much will you have??,")


# math is imported at the top of file
def compound_interest(principle, rate, time):
    result = principle * (pow((1 + rate / 100),
                              time))
    return result


# compounded interest is calculated by taking time *amount of money *percentage
# of rate
def main():
    # Step 2, the function goes down to compound_interest and goes up to the
    # definition
    rate = 0.12
    principle = total_minutes_movie_night
    time = float(input("Enter how many years you would like for it to sit!: "))
    final = compound_interest(principle,
                              rate,
                              time)
    final_compounded = (format(final,
                               ".2f"))
    print("You will have $",
          final_compounded,
          "in your bank account after",
          time,
          "years!")


main()

# Call to main
# Personality Assessment
# https://www.section.io/engineering-education/personality-test-app/
# Coming soon
print('Let\'s continue to have a little math break! Enter a number and lets '
      'calculate '
      'it\'s square root!')
# I imported math at the top of the program, and now I'm able to access
# "a book from a library" and rip out a page to use the square root function
sqrt_root = int(input("Enter any integer:  "))
print(math.sqrt(sqrt_root))
print("Last but not least, let's demonstrate a for loop!")
# https://bobbyhadz.com/blog/python-attributeerror-int-object-has-no-attribute-
# randint#:~:text=The%20Python%20%22AttributeError%3A%20'
# int,call%20the%20method%20as%20random.

number_of_guesses = int(input("How many rounds would you like?"))
guessing_number = 0
for counter in range(number_of_guesses):
    mystery_number = (random.randint(1,
                                     10))
    if mystery_number != guessing_number:
        guessing_number = int(input("I'm thinking of a number 1-10\n"))
        print("You lost! Try again")
        print(mystery_number)
    else:
        print("Congrats you won!!")
