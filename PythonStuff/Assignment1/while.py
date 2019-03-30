play_again="y"
while play_again == "y" :

    user= int(input("Enter a number "))
    for i in range(user+1) :
        print(i)

    play_again = input ("would you like to play again ") 
