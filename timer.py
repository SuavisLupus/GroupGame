import tkinter as tk
from game import *

# Description: timer, separate window, using tkinter widget
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# stackoverflow.com
# https://wiki.python.org/moin/TkInter
# Automate the Boring Stuff with Python (https://www.nostarch.com/automatestuff), Practical Programming for Total Beginners, by Al Sweigart, April 2015, 504 pp. ISBN: 978-1-59327-599-0
#
# to-do: remove class, work-out-of-box solution
#
# create a Tk root widget before any other widgets (because there can only be one root widget)
#root = Tk()
# first parameter of the Label call is the name of the parent window. Now our Label widget is a child of the root widget.
#w = Label(root, text="Victory is ours!")
# pack() method tells Tk to fit the size of the window to the given text.
#w.pack()
# Wwindow won't appear until we enter the Tkinter event loop:
#root.mainloop()
#
# Other changes:----
#
#
# change in game.py to
#
# if __name__ == "__main__":
#    p = TimerWidget()
#    while main():
#        p
#
#
#
#
class TimerWidget(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="", width=50)
        self.label.pack()
        self.wm_title("Oxygen Tank")
        self.wm_iconbitmap('new.ico')
        global remaining
        self.remaining = 0
        # 20 minutes
        self.countdown(600)

    def countdown(self, remaining=None):
        global player_alive

        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(fg='red', bg='black', text="Time's up, player is dead!")
            self.remaining = 0
            player_alive = False
            death(player_alive)
            #print('Player is dead')
            # kill player

        else:
            self.label.configure(fg='green', bg='black', text="Oxygen tank: %d seconds left until depletion" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

if __name__ == "__main__":
    app = TimerWidget()
    app.mainloop()
