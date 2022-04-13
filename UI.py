from tkinter import Tk, Canvas, Entry, Button, StringVar, filedialog, END, Spinbox
from search import search_func

def read_data():

    global  topic, location_input, pages, screen_height, screen_width

    tp_search      = topic.get()
    file_location  = location_input.get()
    p_number       = pages.get()

    search_func(tp_search, p_number, file_location, screen_width, screen_height)

def browse_button():
    
    global folder_path, location_input, canvas1
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    location_input.delete(0,END)
    location_input.insert(0, filename)


if __name__ == "__main__":
   
    window = Tk()

    screen_width    = window.winfo_screenwidth()
    screen_height   = window.winfo_screenheight() 

    window.title("Google scholar - Articles downloader V.1")
    window.configure(width=600, height=400)
    window.configure(bg='lightgray')
    window.eval('tk::PlaceWindow . center')
    window.resizable(False, False)

    canvas1 = Canvas(window, width=635, height=300, bg='#7874F6')
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_text(100, 45, text="Your topic:", fill="white", font=('Helvetica 13 bold'))
    topic = Entry(canvas1, width=40, font=("Helvetica", 12))
    topic.place(x=170,y=33)

    canvas1.create_text(90, 120, text="Location:", fill="white", font=('Helvetica 13 bold'))
    location_input = Entry(canvas1, width=33, font=("Helvetica", 12))
    location_input.place(x=175,y=110)

    folder_path = StringVar()
    browse = Button(canvas1, text="Browse", width=7, font=("Helvetica", 8), command=browse_button)
    browse.place(x=482,y=110)

    canvas1.create_text(120, 190, text="Number of pages:", fill="white", font=('Helvetica 13 bold'))
    pages = Spinbox(canvas1, from_=0, to=30, width=7, textvariable=0, wrap=True)
    pages.place(x=210,y=182)

    down = Button(canvas1, text="Search", width=15, font=("Helvetica", 11), bg="Green", fg="White", command=read_data)
    down.place(x=265,y=260)
    
    window.mainloop()