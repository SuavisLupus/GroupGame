import tkinter as tk
import game
# Description: (1) Countdown Timer which indicates the oxygen tank and how much time the player has until
# it is over. (2) Display map to player by displaying an image.
#
# Used tkinter for simplicity, it comes as standard Python package.
#
# References:
# - http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# - https://wiki.python.org/moin/TkInter
# - http://stackoverflow.com
# - Automate the Boring Stuff with Python (https://www.nostarch.com/automatestuff), Practical Programming for Total Beginners, by Al Sweigart, April 2015, 504 pp. ISBN: 978-1-59327-599-0
#
# In next version:
# * Make use of coroutines using asyncio (>Python 3.5) - async GUI programming
# * Make tkinter work with asyncio as there is no easy way to combine mainloop of tkinter and asyncio
#
# Cardiff University 2015
class TimerWidget(tk.Tk):
    def __init__(self):
        # init thread
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="", width=50)
        # pack it
        self.label.pack()
        # title of gui window
        self.wm_title("HUD")
        # set logo, use PhotoImage
        global logo
        logo = tk.PhotoImage(file="Map.gif")
        # keep reference of image so garbage collector doesnt eat it
        logo.image = logo
        w1 = tk.Label(self, image=logo).pack(side="right")
        #explanation = """EMPTY SPACE"""
        w2 = tk.Label(self, justify='left').pack(side="left")

        # icon of gui window
        self.wm_iconbitmap('new.ico')
        global remaining
        self.remaining = 0
        # 15 minutes oxygen
        self.countdown(900)

    def countdown(self, remaining=None):
        global player_alive

        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            # Player is not alive if he doesnt have oxygen
            player_alive = False
            # Player is dead
            game.death(player_alive)

        else:
            self.label.configure(fg='green', text="Oxygen tank: %d seconds left until depletion" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

if __name__ == "__main__":
    app = TimerWidget()
    app.mainloop()
