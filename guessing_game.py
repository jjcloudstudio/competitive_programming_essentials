import builtins  
secret_word = "griaffe"

guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")
    
print("You win!")