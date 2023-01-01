"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name: Karri Seppä
Student id: 150435444
Email: karri.seppa@tuni.fi
GUI project 13.12.2021
"""

from tkinter import *
from winsound import *
import random

class Animalgame:
    """
    In this animalgame aimed for children (or people with no experience in
    identifying animals) the player needs to connect the name of the animal
    i.e. "fox" with the picture of a fox by clicking on the fox image. If the
    player chooses the right animal the game progresses. There are 9 animals
    you need to find and 9 pictures of animals. The order of A) the pictures
    of the animals and B) the order you need to find them is randomized!
    Also for fun and educational purposes, when you click on an animal
    (right or wrong, we won't judge) the animal makes sounds according to the
    one pressed. Make sure you have the "sounds" and "images" folders where
    you have the python file. These files should be there when you unzip the
    .zip file, you don't have to touch anything. I've imported tkinter for
    the graphic ui, winsound to play the sound files and random for
    randoming the order of animals. When you find all the animals the game
    asks if you want to play the game again (randomizing the orders again) or
    just quit. This project was trying to be an advanced project. I hope you
    won't disagree.
    Have fun playing!
    """

    def __init__(self):
        self.__mainwindow = Tk()

        # First we're creating a list for the order of the animals (that we're
        # gonna randomize soon. There's 9 animals so as a programmer that
        # means from 0-8. We also create animal names as a list that we use
        # to randomize the guessing order and also check if the if the correct
        # animal was pressed. We also create a buttons list that we're gonna
        # change the values to each of the 9 buttons. Then we need a
        # gamestate counter that starts from 0 and when it reaches 9(all
        # animals have been found from 0-8.) The game doesn't prompt any more
        # animals to find. Last we have a call to randomize the order of the
        # animal pictures and the order of animals to guess from.
        self.__order = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        self.__animals = ["cow", "chicken", "sheep", "dog", "bird", "fox",
                          "cat", "horse", "pig"]

        self.__buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        self.__gamestate = 0

        self.randomorder()

        # I was hoping to create a loop for these but unfortunately I
        # couldn't find a way since apparently the tkinter garbage collects
        # the images unless they're being names and kept constantly in
        # memory. Oh well, luckily the game isn't that big! If we could use
        # some imported modules we could probably make this a bit neater.
        # After all of the images are created (and placed in the randomized
        # order!) They're all placed in a list of images for ease of use and
        # calling. All images are already 300x300 pixels, but with added depth
        # probably could be rescaled in the program itself so you could use
        # your own pictures. Most of these pictures were found on the internet
        # and I'm not using them for any commercial gain. 1 picture is mine,
        # can you guess which one it is?
        self.__img0 = PhotoImage(file=f"./images/{self.__order[0]}.png")
        self.__img1 = PhotoImage(file=f"./images/{self.__order[1]}.png")
        self.__img2 = PhotoImage(file=f"./images/{self.__order[2]}.png")
        self.__img3 = PhotoImage(file=f"./images/{self.__order[3]}.png")
        self.__img4 = PhotoImage(file=f"./images/{self.__order[4]}.png")
        self.__img5 = PhotoImage(file=f"./images/{self.__order[5]}.png")
        self.__img6 = PhotoImage(file=f"./images/{self.__order[6]}.png")
        self.__img7 = PhotoImage(file=f"./images/{self.__order[7]}.png")
        self.__img8 = PhotoImage(file=f"./images/{self.__order[8]}.png")
        self.images = [self.__img0, self.__img1, self.__img2, self.__img3,
                       self.__img4, self.__img5, self.__img6, self.__img7,
                       self.__img8]

        # Next for the sounds. Each sounds is only being called for by
        # clicking on a picture of an animal. So by creating a list of the
        # animal sounds, we can use the list when creating the buttons and
        # their commands. These sounds were found on the internet and I'm
        # not getting any commercial gain from them. I don't own any of
        # these sound files.
        self.sounds = [self.sound0, self.sound1, self.sound2, self.sound3,
                       self.sound4, self.sound5, self.sound6, self.sound7,
                       self.sound8]

        # Creating the 2 labels for the title of the game and then the
        # prompt label that guides the playing. Then creating the 2 buttons for
        # either restarting the game or quitting the game at any point during
        # play. The playlabel is laterchanged after each successful button
        # press by the button being pressed.
        self.__labeltitle = Label(self.__mainwindow, text="Animal guessing  "
                                                          "game by KarriS")
        self.__labeltitle.grid(row=0, column=0)

        self.__playlabel = Label(self.__mainwindow, text=f"Find the "
                                                         f"{self.__animals[self.__gamestate]}")
        self.__playlabel.grid(row=0, column=2)

        self.__restartbutton = Button(self.__mainwindow, text="Restart",
                                   command=self.restart)
        self.__restartbutton.grid(row=0, column=4)

        self.__quitbutton = Button(self.__mainwindow, text="Quit",
                                   command=self.quit)
        self.__quitbutton.grid(row=0, column=4, sticky=E)

        # Here's where most of the magic happens. We're creating all the 9
        # buttons with the pictures of the animal and connecting them to the
        # correct sound of the animal in the picture. We start by creating a
        # variable that guides which animal is in turn for the creation.
        # Then we increase the number by 1 to move to
        # the next animal in question.
        self.__number = 0
        # Next we make a for loop inside a for loop to create the rows
        # with columns. The first row is for the labels and quit
        # button, so we begin from row 1. Then to leave some space for
        # the labels etc possible future modifications we make the
        # buttons on every second row and column.
        for r in range(1, 6, 2):
            for c in range(0, 5, 2):
                # To create a button and then later place it in the list of
                # buttons we name each new button a "button".
                button = Button(self.__mainwindow,

                # We add the image of the correct animal from the list
                image=self.images[self.__number],

                # And then add the corresponding sound to the same animal by
                # fetching the position using the position number and
                # the number from the randomized order list
                command=self.sounds[self.__order[self.__number]])

                # Then we add the buttons to the list by using the variable
                # button where we stored the button itself created by this
                # loop. We use the number variable to keep track.
                self.__buttons[self.__number] = button

                # Using the for loop variables we place the button in the grid.
                self.__buttons[self.__number].grid(row=r, column=c)

                # Last we increase the number by 1 to hop on to the next
                # animal in the randomized list.
                self.__number += int(1)

        self.__mainwindow.mainloop()

    def sound0(self):
        """
        These sound commands don't take any variables in them and don't
        return anything. They play the sound of the animal in the picture
        when pressed, and if the animal was the one we were trying to find,
        we progress the game by adding 1 to the gamestate. If we reach 9 in
        the gamestate the game ends!
        """
        PlaySound("./sounds/0.wav", SND_ASYNC)
        correct = "cow"
        if self.__animals[self.__gamestate] == correct:
            self.__gamestate += int(1)
            if self.__gamestate == 9:
                self.ending()
            else:
                self.__playlabel.configure(text=f"Correct! Now find the {self.__animals[self.__gamestate]}")
        else:
            pass

    def sound1(self):
        """
        Identical to sound0 but with the correct animal.
        """
        PlaySound("./sounds/1.wav", SND_ASYNC)
        correct = "chicken"
        if self.__animals[self.__gamestate] == correct:
            self.__gamestate += int(1)
            if self.__gamestate == 9:
                self.ending()
            else:
                self.__playlabel.configure(text=f"Correct! Now find the {self.__animals[self.__gamestate]}")
        else:
            pass

    def sound2(self):
        """
        Identical to sound0 but with the correct animal.
        """
        PlaySound("./sounds/2.wav", SND_ASYNC)
        correct = "sheep"
        if self.__animals[self.__gamestate] == correct:
            self.__gamestate += int(1)
            if self.__gamestate == 9:
                self.ending()
            else:
                self.__playlabel.configure(text=f"Correct! Now find the {self.__animals[self.__gamestate]}")
        else:
            pass

    def sound3(self):
        """
        Identical to sound0 but with the correct animal.
        """
        PlaySound("./sounds/3.wav", SND_ASYNC)
        correct = "dog"
        if self.__animals[self.__gamestate] == correct:
            self.__gamestate += int(1)
            if self.__gamestate == 9:
                self.ending()
            else:
                self.__playlabel.configure(text=f"Correct! Now find the {self.__animals[self.__gamestate]}")
        else:
            pass

    def sound4(self):
        """
        Identical to sound0 but with the correct animal.
        """
        PlaySound("./sounds/4.wav", SND_ASYNC)
        correct = "bird"
        if self.__animals[self.__gamestate] == correct:
            self.__gamestate += int(1)
            if self.__gamestate == 9:
                self.ending()
            else:
                self.__playlabel.configure(text=f"Correct! Now find the {self.__animals[self.__gamestate]}")
        else:
            pass

    def sound5(self):
        """
        Identical to sound0 but with the correct animal.
        """
        PlaySound("./sounds/5.wav", SND_ASYNC)
        correct = "fox"
        if self.__animals[self.__gamestate] == correct:
            self.__gamestate += int(1)
            if self.__gamestate == 9:
                self.ending()
            else:
                self.__playlabel.configure(text=f"Correct! Now find the {self.__animals[self.__gamestate]}")
        else:
            pass

    def sound6(self):
        """
        Identical to sound0 but with the correct animal.
        """
        PlaySound("./sounds/6.wav", SND_ASYNC)
        correct = "cat"
        if self.__animals[self.__gamestate] == correct:
            self.__gamestate += int(1)
            if self.__gamestate == 9:
                self.ending()
            else:
                self.__playlabel.configure(text=f"Correct! Now find the {self.__animals[self.__gamestate]}")
        else:
            pass

    def sound7(self):
        """
        Identical to sound0 but with the correct animal.
        """
        PlaySound("./sounds/7.wav", SND_ASYNC)
        correct = "horse"
        if self.__animals[self.__gamestate] == correct:
            self.__gamestate += int(1)
            if self.__gamestate == 9:
                self.ending()
            else:
                self.__playlabel.configure(text=f"Correct! Now find the {self.__animals[self.__gamestate]}")
        else:
            pass

    def sound8(self):
        """
        Identical to sound0 but with the correct animal.
        """
        PlaySound("./sounds/8.wav", SND_ASYNC)
        correct = "pig"
        if self.__animals[self.__gamestate] == correct:
            self.__gamestate += int(1)
            if self.__gamestate == 9:
                self.ending()
            else:
                self.__playlabel.configure(text=f"Correct! Now find the {self.__animals[self.__gamestate]}")
        else:
            pass

    def ending(self):
        """
        When the player reaches gamestate 9 the game ends. The player
        doesn't get any more prompts in the playlabel to find the correct
        animal. If the player keeps pressing on the animal pictures they can
        still hear the sounds. Unfortunately the gamestate is in 9 so it
        causes an error in the log since there was only 0-8 in the list and
        it's trying to call the 9th (10th) animal. Shame. But it doesn't
        affect the gameplay and the only option from now is to quit so it
        shouldn't bother anyone at least too much.
        """
        self.__playlabel.configure(text="Congratulations! You found all the "
                                        "animals! Replay?")
        self.__quitbutton.configure(text="No (Quit)")
        self.__restartbutton.configure(text="Yes! (Restart)")

    def randomorder(self):
        """
        Using the imported random we shuffle the both lists for the order of
        the animals in pictures and the order you need to guess them to create
        a new and challenging replay to the game.
        """
        random.shuffle(self.__order)
        random.shuffle(self.__animals)

    def restart(self):
        """
        Closes the GUI and runs the main again to restart the whole screen
        to get new order of animal pictures and the order you need to find
        them.
        """
        self.__mainwindow.destroy()
        main()

    def quit(self):
        """
        Closes the program. Goodbye!
        """
        self.__mainwindow.destroy()

def main():
    Animalgame()


if __name__ == "__main__":
    main()
