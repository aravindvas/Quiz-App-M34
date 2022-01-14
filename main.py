from tkinter import *
import requests
import html

theme = "#375362"
ip = ""
a = 0
scr = 0

def chgq():
    global ip
    c.config(bg="white")
    t1.config(text=f"Score: {scr}")
    qst()
    c.itemconfig(qt2, text=ip)

def trup():
    global a, scr
    if a < len(ans):
        if ans[a] == "True":
            scr += 1
            print("crct")
            c.config(bg="green")
        else:
            print("wrng")
            c.config(bg="red")
        a += 1
        w.after(1000, chgq)
def falp():
    global a, scr
    if a < len(ans):
        if ans[a] == "False":
            scr += 1
            print("crct")
            c.config(bg="green")
        else:
            print("wrng")
            c.config(bg="red")
        a += 1
        w.after(1000, chgq)

w = Tk()
w.title("Aravindvas's Quiz App")
w.config(padx=20, pady=20, bg=theme)

c = Canvas(width=300, height=250, bg="white")
qt2 = c.create_text(
    150,
    125,
    width=280,
    text="text",
    fill=theme,
    font=("Arial", 20, "italic"))
c.grid(row=1, column=0, columnspan=2, pady=50)
wim = PhotoImage(file="images/false.png")
rim = PhotoImage(file="images/true.png")

t1 = Label(text="Score: 0", bg=theme, fg="white")
t1.grid(row=0, column=1)

b1 = Button(image=rim, highlightthickness=0, command=trup)
b1.grid(row=2, column=0)

b2 = Button(image=wim, highlightthickness=0, command=falp)
b2.grid(row=2, column=1)

parm = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}
rsp = requests.get(url="https://opentdb.com/api.php", params=parm)
rsp.raise_for_status()
aldt = [rsp.json()["results"][i]["question"] for i in range(10)]
ans = [rsp.json()["results"][k]["correct_answer"] for k in range(10)]
print(ans)
cp = 0
def qst():
    global ip, cp
    if cp < len(aldt):
        qtx = html.unescape(aldt[cp])
        ip = f"Q{cp + 1}. {qtx}"
        cp += 1
    else:
        ip = "You have reached the end of the quiz"
        b1.config(state="disabled")
        b2.config(state="disabled")

chgq()




w.mainloop()