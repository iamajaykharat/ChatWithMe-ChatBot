
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

# Creating an object of ChatBot class
myBot = ChatBot("My Bot")

# converstion to get reference to our bot for chatting
conv = [
    'Hi Buddy',
    'Hello,My friend',
    'How are you?',
    'I am great! and You?',
    'Ok,Great!',
    'What is your name?',
    'My name is Aksh and I am created By Mr.Ajay',
    'Where do you live?',
    'I live in your PC.It is an amezing place',
    'Who is your favorite actor?',
    'My favorite actor is Shah Rukh Khan.what about you?',
    'Awesome!',
    'Bye Bye!',
    'Bye Bye Friend!,Nice to talk with you,You are Awesome!',

    # Add more converstion here to train your bot perfectly

]

# Trainging our bot
trainer = ListTrainer(myBot)
trainer.train(conv)


def ask_me():
    query = textF.get()
    response = myBot.get_response(query)
    msg.insert(END, 'You: ' + query + "\n\n")
    msg.insert(END, 'Bot: ' + str(response) + "\n\n")
    textF.delete(0, END)
    
# Creating GUI for Our Application

main = Tk()
main.geometry("450x650")
main.title("ChatWithMe                                 By Ajay")
icon = PhotoImage(file="icon.png")
main.iconphoto(False, icon)

img = PhotoImage(file="appimg.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)

frame = Frame(main)
sc = Scrollbar(frame)
msg = Listbox(frame, width=80, height=20)
sc.pack(side=RIGHT, fill=Y)
msg.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack(padx=10)

textF = Entry(main, font=("Arial Bold", 15))
textF.pack(fill=X, pady=8, padx=10)

btn = Button(main, text="Ask Me", font=("Times New Roman", 15), bg='yellow', command=ask_me)
btn.pack(pady=5)

main.mainloop()
