from tkinter import*
from PIL.Image import Image, ImageTk
from random import randint

#window display
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="blue")

#defining image
rock_user = ImageTk.PhotoImage(Image.open("rock.jpeg"))
paper_user = ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_user = ImageTk.PhotoImage(Image.open("scissor.jpeg"))
rock_computer = ImageTk.PhotoImage(Image.open("rock computer.jpeg"))
paper_computer = ImageTk.PhotoImage(Image.open("paper computer.jpg"))
scissor_computer = ImageTk.PhotoImage(Image.open("scissor.jpeg"))

#inserting image
user_label = Label(root,image=rock_user,bg="blue")
computer_label = Label(root,image=rock_computer,bg="blue")
computer_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)



#scores section
player_score = Label(root,text=0,font=100,bg="blue",fg="black")
computer_score = Label(root,text=0,font=100,bg="blue",fg="black")
player_score.grid(row=1,column=3)
computer_score.grid(row=1,column=1)

#identy
user_identy = Label(root,font=50,text="PLAYER",bg="blue")
computer_identy = Label(root,font=50,text="COMPUTER",bg="blue")
user_identy.grid(row=0,column=3)
computer_identy.grid(row=0,column=1)
#message
message = Label(root,font=50,bg="blue",fg="black")
message.grid(row=3,column=2)

# funtion to update the message and the score
def update_message(x):
    message["text"] = x
#update the user score
def update_user_score():
    score = int(player_score["text"])
    score +=1
    player_score["text"] = str(score)
#to update computer score
def update_computer_score():
    score = int(computer_score["text"])
    score +=1
    computer_score["text"] = str(score)

#to check the winner
def check_winner(player, computer):
    if player == computer:
        update_message("EQUAL!")
    elif player == "rock":
        if computer == "paper":
            update_message("LOSE :(")
            update_computer_score()
        else:
            update_message("VICTORY !!")
            update_user_score()
    elif player =="paper":
         if computer =="scissor":
             update_message("LOSE:(")
             update_computer_score()
         else:
             update_message("VICTORY !!")
             update_user_score 
    elif player == "scissor":
         if computer=="rock":
            update_message("LOSE :(")
            update_computer_score()
         else:
             update_message("VICTORY !!")
             update_user_score()
    else:
         pass
check_winner()

#defining the function to update the choice
choices= ["rock", "paper", "scissor"]
def update_choice(x):
    #for computer
    computer_choice= choices[randint(0,2)]
    if computer_choice== "rock":
        computer_label.configure(image=rock_computer)
    elif computer_choice== "paper":
        computer_label.configure(image=paper_computer)
    else:
        computer_label.configure(image=scissor_computer)

    #for user
    if x=="rock":
        user_label.configure(image=rock_user)
    elif x=="paper":
        user_label.configure(image=paper_user)
    else:
        user_label.configure(image=scissor_user)

#button section
rock = Button(root, width=20,height=2,text="ROCK",
              bg="pink",fg="black",command= lambda:update_choice("rock")).grid(row=2,column=1)
paper = Button(root, width=20,height=2,text="PAPER",
               bg="purple",fg="black",command= lambda:update_choice("paper")).grid(row=2,column=2)
scissor = Button(root, width=20,height=2,text="SCISSOR",
                 bg="yellow",fg="black",command= lambda:update_choice("scissor")).grid(row=2,column=3)













root.mainloop()