import sys
__author__="Vivian Procacci"
# import sys for sys.exit so that after the program the user isnt stuck in an
#infinite loop

personality_type = ""
#This is the final string that accumalates
def announce(personality_type):
    """

    :param personality_type:
    """
    print("Your personality type is",
          (personality_type) + "!\nThank you for participating!")
    # function that declares personality after the test
def run():
    # function that quite literally runs our program, and stores our test
    # questions in a list
    list_questions=0
    print("\nType T for True and F for False!")
    list_questions= [
        """
Question 1:
Being around people energizes me.
*  T
*  F
""",
        """
Question 2: 
I work better in groups, rather than alone.
*  T
*  F
""",
        """
Question 3:
At a party, it energizes me when I mingle and interact with people.
*  T
*  F
""",
        """
Question 4:
When thinking of a solution to any complex problem I like to be practical 
rather than creative.
*  T
*  F
""",
        """        
Question 5:
In my head I love living in the past and present rather than in the future.
*  T
*  F
""",
        """
Question 6:
I am a traditional person.
*  T
*  F
""",
        """
Question 7:
I think the world would be a better place if people were more compassionate 
and less blunt.
*  T
*  F
""",
        """
Question 8:
I find it easy to empathize with a person whose experiences are very 
different from mine.
*  T
*  F
""",
        """
Question 9:
Seeing other people cry can easily make me want to cry.
*  T
*  F
""",
        """
Question 10:
I am stimulated by an approaching deadline.
*  T
*  F
""",
        """
Question 11:
I prefer improvation rather than meticulous planning.
*  T
*  F
""",
        """
Question 12:
I work in bursts of energy.
*  T
*  F
"""
    ]
    # 12 questions, 3 per section
    # 1-3 Extroverted is True, Introverted is False
    # 4-6 Sensing is True, Intuitive is False
    # 7-9 Feeling is True, Thinking is False
    # 10-12 Perceiving is True, Judging is False
    count_of_t: int = 0
    count_of_f: int = 0
    personality_type: str = ''
    count = 0
    for question in list_questions:
        answer = ''
        while not (answer == 'T' or answer == 'F'):
            count_of_t = 0
            count_of_f = 0
            try:
                answer = input(question).upper()
            #takes input and makes it uppercase
                if not (answer == 'T' or answer == 'F'):
                    raise ValueError()
            #let's computer know that anything other then T or F is invalid
            except ValueError:
                    print("Hey, that wasn't a part of our agreement!\nTry "
                          "again...")
#https://docs.python.org/3/tutorial/errors.html
            else:
                if answer == 'T':
                    count_of_t = count_of_t + 1
                if answer == 'F':
                    count_of_f = count_of_f + 1
                count = count + 1
        #our for loop counters ^
        #compute dominant dichotomy with if statements v
        if count == 3:
            if count_of_t > count_of_f:
                personality_type = personality_type + 'E'
            else:
                personality_type = personality_type + 'I'
        # determining which choice was dominant, it adds to our personality
            count_of_t: int = 0
            count_of_f: int = 0
        #resets count of t and f so if user chooses 9 T and 3 F it will
        # account for F
        else:
            if count == 6:
                if count_of_t > count_of_f:
                    personality_type = personality_type + 'S'
                else:
                    personality_type = personality_type + 'N'
                count_of_t: int = 0
                count_of_f: int = 0
            else:
                if count == 9:
                    if count_of_t > count_of_f:
                        personality_type = personality_type + 'F'
                    else:
                        personality_type = personality_type + 'T'
                    count_of_t: int = 0
                    count_of_f: int = 0
                else:
                    if count == 12:
                        if count_of_t > count_of_f:
                            personality_type = personality_type + 'P'
                        else:
                            personality_type = personality_type + 'J'
                        count_of_t: int = 0
                        count_of_f: int = 0

    announce(personality_type)
    stop2_loop_from_running = False
    while stop2_loop_from_running == False:
        try:
            con_input = int(input("""
                Press 1  to continue my program
                Press 2 to exit program 
                    ／ʕ •ᴥ•ʔ-->  """))
            if con_input == 1:
                continue_program()
            elif con_input == 2:
                print("Thanks! Have a nice day")
                stop2_loop_from_running = True
                sys.exit(0)
        except ValueError:
            print("That was not a valid option.  Try again..."
                  )
def continue_program():
    print("Before I go.....")
    # Let's plan a movie night!
    # I used a while loop, and set the stop loop from running to False, until
    # it hits the sentinel value: 00
    sum_of_movies = 0
    stop_loop_from_running = False

    while not stop_loop_from_running:

        try:
            movie_menu_selection = int(input("Let's plan a "
                                             "movie night."
                                             "\nEnter the "
                                             "number choice for what "
                                             "you "
                                             "would "
                                             "like "
                                             "to "
                                             "see\n1. Beauty and the Beast ("
                                             "1991)\n2. The Little Mermaid ("
                                             "1989) \n3. Mulan ( "
                                             "1998)\n4. Pocahontas (1995)\n5. "
                                             "Cinderella ( "
                                             "1950)\n To Exit,type 00 or "
                                             "10\n"))
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
    print("You want to watch",
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
    print("If you watched your movie 5 times, it would appromiately take "
          "you..",
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
          "minutes...")
    print("\nLets say youre having a movie night, and you want to watch the "
          "movie you inserted above and a \nnew movie....",
          end='')
    print("Let's figure out how long the duration of the movie night is in "
          "hours "
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
    print("Thats all folks! Have an amazing day!")
    sys.exit()
def main():
    fetching_sentence = open('open_me.txt')
    for line in fetching_sentence.readlines():
        print(line.strip())
    fetching_sentence.close()
    stop_loop_from_running= False
    while stop_loop_from_running==False:
        try:
            user_input = int(input("""
            Press 1  to take test
            Press 2 to exit test
            Press 3 to see the rest of the project 
                ૮ ˶ᵔ ᵕ ᵔ˶ ა-->  """))
            if user_input== 1:
                run()
            elif user_input== 2:
                print("Thanks! Have a nice day")
                stop_loop_from_running=True
            elif user_input == 3:
                continue_program()
                stop_loop_from_running = True
        except ValueError:
            print("That was not a valid option.  Try again..."
                  )
    #while loop is running is false, ask user for input, if user chooses 1,
    # run the program and if user chooses 2 set stop loop from running true,
    # and all other responses are an error

#exit program
#Call to main! ,first step in flow of execution
