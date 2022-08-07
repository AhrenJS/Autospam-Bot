import pyautogui
import time
from tkinter import *

root = Tk()
WIDTH = root.winfo_screenwidth()//3
HEIGHT = root.winfo_screenheight()//2
root.title("Da Spammer Thing")
root.geometry(f"{WIDTH}x{HEIGHT}")

spam_label = Label(root, text="The\nGreat\nSpam", height=5, font=("Impact", "30"), anchor=CENTER)
spam_label.pack(fill=BOTH, expand=TRUE)
frame4_top = Frame(root, width=WIDTH, height=HEIGHT*0.6)
frame4_top.pack(side=TOP)
frame4_bot = Frame(root, width=WIDTH, height=HEIGHT*0.4)
frame4_bot.pack(side=BOTTOM)

class spam_button:
    def __init__(self, spamframe):
        frame5 = Frame(spamframe)
        frame5.pack()
        tip_label = Label(frame4_top, text=("(To Stop Spamming : Move mouse to the top corner of the screen)"))
        tip_label.pack(side=TOP)
        self.spam_but = Button(frame4_top, text="Start Spamming (Normal)", command=self.start_spam)
        self.spam_but.pack()
        self.spam_but_fast = Button(frame4_top, text="Start Spamming (Fast)", command=self.fast_spam)
        self.spam_but_fast.pack()
        self.quit_button = Button(frame4_top, text="Quit", command=frame5.quit)
        self.quit_button.pack()

    def fast_spam(self):
        print("Fast Spam started")
        with open("Beemovie_Script", "r") as f:
            time.sleep(2)
            try:
                for word in f:
                    pyautogui.typewrite(word)
                    pyautogui.press("enter")
                    time.sleep(0.1)
            except:
                self.stop_spam()

    def start_spam(self):
        print("Normal Spam started")
        with open("Beemovie_Script", "r") as f:
            time.sleep(2)
            try:
                for word in f:
                    pyautogui.typewrite(word)
                    pyautogui.press("enter")
                    time.sleep(1)
            except:
                self.stop_spam()

    def remove_text(self):
        self.remove_but.pack_forget()
        self.text_spam.pack_forget()

    def stop_spam(self):
        self.text_spam = Label(frame4_bot, text="Spam has ended", fg="Red", anchor=CENTER, font=("Georgia",10), pady=HEIGHT//15, padx=WIDTH//5)
        self.text_spam.pack()
        self.remove_but = Button(frame4_bot, text="Remove Notifications", command=self.remove_text)
        self.remove_but.pack()

class_spam = spam_button(root)

root.mainloop()