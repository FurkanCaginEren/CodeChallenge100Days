from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
new_card = {}
words_to_learn = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")

except:
    original_data = pandas.read_csv("data/french_words.csv")
    words_to_learn  =original_data.to_dict(orient="records")
else:
    words_to_learn  =data.to_dict(orient="records")



## PANDAS DATA COLLECTING ##



def next_card():
    global new_card,flip_timer
    window.after_cancel(flip_timer)
    new_card = random.choice(words_to_learn)
    #Canvas function canvas.itemconfig("item that we want to change,attribute of the item ")
    card.itemconfig(card_image,image=back_image)
    card.itemconfig(card_language,text="French",fill="white")
    card.itemconfig(card_word,text =new_card["French"],fill="white")
    flip_timer = window.after(3000,func=flip_card)
## Flipping Utility ##

def flip_card():
    #Canvas function canvas.itemconfig("item that we want to change,attribute of the item ")
    card.itemconfig(card_language,text="English",fill="black")
    card.itemconfig(card_word,text =new_card["English"],fill="black")
    card.itemconfig(card_image,image=front_image)


def remove_card():
    words_to_learn.remove(new_card)
    ## dict to DATA frame and I save that data frame as words_to_learn
    data = pandas.DataFrame(words_to_learn)
    # data frame to csv
    data.to_csv("data/words_to_learn.csv",index=False)

    next_card()
    




## UI ##
window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flesh-Card")

flip_timer = window.after(3000,func=flip_card)

card = Canvas(width=800,height =526,bg=BACKGROUND_COLOR,highlightthickness=0)
back_image=PhotoImage(file="images/card_back.png")
front_image=PhotoImage(file="images/card_front.png")
card_image=card.create_image(400,263,image=back_image)
card_language = card.create_text(400,150,font=("Arial",40,"italic"),text="French")
card_word = card.create_text(400,263,font=("Arial",40,"italic"),text="Word")
card.grid(row=0,column=0,columnspan=2)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0,command=remove_card)
correct_button.grid(row=1,column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)




next_card()




window.mainloop()