from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text='00:00')
    global reps
    reps = 0
    check_label.config(text='')
    timer_label.config(text='Timer', fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # * test for short time
    # work_sec = 10
    # short_break_sec = 5
    # long_break_sec = 20
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text='Break', fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text='Work', fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        marks = ''
        global reps
        if reps == 8:
            reps = 0
            marks = ''
        for _ in range(reps // 2):
            marks += '✓'
        check_label.config(text=marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, 'bold'))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=204, height=228, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 136, fill='white', font=(FONT_NAME, 28, 'bold'), text='00:00')
canvas.grid(row=1, column=1)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, 'bold'))
check_label.grid(row=3, column=1)

window.mainloop()
