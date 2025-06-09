while True:

    score = 0


    #Insert input -------

    name = input("Insert name:")
    print(f"Hello,{name}!")

    answer = input("Ready for quiz? (Y/N)").strip().upper()

    #if /else -------

    if answer == "Y":
        print("Lets go!")

    else:
        print("Goodbye!")
        exit()


    # QUIZ SECTION -------
    print("There are 5 questions. Each correct answer is worth 1 point.")


    # QUESTION 1 -------
    questionone = float(input("2+2"))

    if questionone == 4:
        score+=1
        print("CORRECT!")

    else:
        print("Incorrect")


    # QUESTION 2 -------
    questiontwo = float(input("5+5"))

    if questiontwo == 10:
        score+=1
        print("CORRECT!")


    else:
        print("Incorrect")

    # QUESTION 3 -------
    questionthree = float(input("20+5"))

    if questionthree == 25:
        score+=1
        print("CORRECT!")


    else:
        print("Incorrect")

    # QUESTION 4 -------
    questionfour = float(input("1+5"))

    if questionfour == 6:
        score+=1
        print("CORRECT!")


    else:
        print("Incorrect")

    # QUESTION 5 -------
    questionfive = float(input("4+4"))

    if questionfive == 8:
        score+=1
        print("CORRECT!")


    else:
        print("Incorrect")


    #RESULT

    result = input("Want to the see result? (Y/N)").strip().upper()


    #if /else -------

    if result == "Y":
        print(f"{name} you got a {score} out of 5")

    else:
        print("Goodbye!")


   # Ask to play again
    again = input("Play again? (Y/N): ").strip().upper()
    if again != "Y":
        print("Thanks for playing!")
        break