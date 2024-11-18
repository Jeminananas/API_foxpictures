import requests
from tkinter import *

#Picture time
class Picture_window_:
    def __init__(self, image_):
        self.Q = INITIAL_
        self.__main_window = Tk()

        self.__main_window.mainloop()

    def quit(self):
        self.__main_window.destroy()

#Menu, loops infinitely
def menu():
    Ongoing_ = True
    l = ""
    while Ongoing_:
        print(f"Would you like a{l} picture of a fox? (y/n)")
        answer = input("> ")
        print("")

        if(answer.lower() == "y"):
            response = requests.get("https://randomfox.ca/floof")
            print(response.json())
            l = " new"
            print("")
        else:
            print("Suit yourself!\n")

            Ongoing_ = False
            return

def main():
    #Lets gooo!
    menu()


if __name__ == "__main__":
    main()

