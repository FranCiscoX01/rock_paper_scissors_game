from tkinter import ttk
from tkinter import *
from random import randint

import os
import sys

from PIL import Image, ImageTk
# python3 -m pip install --upgrade Pillow

class RockPaperScissors:

    #create a list of play options
    options = ["rock", "paper", "scissors"]

    def __init__(self, window):
        self.wind = window
        self.wind.title('Rock Paper Scissors')

        # Buttons
        # Open Image and resize on button
        img_rock_path = Image.open('img/user_rock.png')
        img_rock_path = img_rock_path.resize((150, 150))
        img_rock = ImageTk.PhotoImage(img_rock_path)
        self.btn_rock = Button(self.wind, text="Rock", image=img_rock, background="#fcec04", command=lambda: self.result(self.options[0]))
        self.btn_rock.image = img_rock
        self.btn_rock.grid(row=1, column=1)

        # Open Image and resize on button
        img_paper_path = Image.open('img/user_paper.png')
        img_paper_path = img_paper_path.resize((150, 150))
        img_paper = ImageTk.PhotoImage(img_paper_path)
        self.btn_paper = Button(self.wind, text="Paper", image=img_paper, background="#fcec04", command=lambda: self.result(self.options[1]))
        self.btn_paper.image = img_paper
        self.btn_paper.grid(row=1, column=2)

        # Open Image and resize on button
        img_scissors_path = Image.open('img/user_scissors.png')
        img_scissors_path = img_scissors_path.resize((150, 150))
        img_scissors = ImageTk.PhotoImage(img_scissors_path)
        self.btn_scissors = Button(self.wind, text="Scissors", image=img_scissors, background="#fcec04", command=lambda: self.result(self.options[2]))
        self.btn_scissors.image = img_scissors
        self.btn_scissors.grid(row=1, column=3, sticky='E')

        # Label
        # results
        self.lb_result_title = Label(self.wind, fg='white', bg='#fcec04', font=("Helvetica", 64))
        self.lb_result_title.grid(row=3,columnspan=4, sticky='WE')

        self.lb_result_description = Label(self.wind, fg='white', bg='#fcec04', font=("Helvetica", 18))
        self.lb_result_description.grid(row=4, columnspan=4,sticky='WE')


    # Configrure result
    def result(self, user_selection):
        player = user_selection
        computer = self.options[randint(0,2)]

        title = ''
        description = ''

        if player == computer:
            title = "Tie!"
        elif player == "rock":
            if computer == "paper":
                title = "You Lose!"
                description = computer + " " + "covers" + " " + player
            else:
                title = "You Win!"
                description = player + " " + "smashes" + " " + computer
        elif player == "paper":
            if computer == "scissors":
                title = "You Lose!"
                description = computer + " " + "cut" + " " + player
            else:
                title = "You Win!"
                description = player + " " + "covers" + " " + computer
        elif player == "scissors":
            if computer == "rock":
                title = "You Lose!"
                description = computer + " " + "smashes" + " " + player
            else:
                title = "You Win!"
                description = player + " " + "cut" + " " + computer
        else:
            title = "That's not a valid play. Check your spelling!"


        # configure result title and description
        self.lb_result_title.configure(text=title)
        self.lb_result_description.configure(text=description)


        # Open Image and resize on button User selectio
        img_res_user_path = Image.open('img/user_' + player + '.png')
        img_res_user_path = img_res_user_path.resize((80, 80))
        img_res_user = ImageTk.PhotoImage(img_res_user_path)
        self.lb_result_user = Label(self.wind, image=img_res_user, bg='#fcec04')
        self.lb_result_user.grid(row=5, column=1)
        self.lb_result_user.image = img_res_user

        self.vs = Label(self.wind,text="VS", bg='#fcec04')
        self.vs.grid(row=5, column=2)

        # Open Image and resize on button Computer selectio
        img_res_compu_path = Image.open('img/ai_' + computer + '.png')
        img_res_compu_path = img_res_compu_path.resize((80, 80))
        img_res_compu = ImageTk.PhotoImage(img_res_compu_path)
        self.lb_result_computer = Label(self.wind, image=img_res_compu, bg='#fcec04')
        self.lb_result_computer.grid(row=5, column=3)
        self.lb_result_computer.image = img_res_compu




if __name__ == '__main__':
    root = Tk()
    game = RockPaperScissors(root)

    # Background color window
    root.configure(bg='#fcec04')

    root.mainloop()
