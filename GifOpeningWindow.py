from tkinter import *
import random


# function for GIF opening window
def OpeningWindow(root):
    # For Central positioning of gif opening image
    positionRight = int(root.winfo_screenwidth() / 2 - 350)
    positionDown = int(root.winfo_screenheight() / 2 - 350)

    # using geometry to place in center
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # lists of frame count and images

    frame_count_list = [57, 49, 57]
    gif_image_list = \
        [
            'Resources\\GIFS\\coutinho.gif',
            'Resources\\GIFS\\Gundogan.gif',
            'Resources\\GIFS\\ozil.gif'
        ]

    # our function for gif image animation

    def Gif_loop(gif_image_location, total_frames, timer):
        # stores frames array of gif image
        gif_image_frames = [PhotoImage(file=gif_image_location, format='gif -index %i' % i) for i in
                            range(total_frames)]

        def update(ind):
            frame = gif_image_frames[ind]
            ind += 1
            if ind == total_frames:
                gif_image_label.pack_forget()
                return
            gif_image_label.configure(image=frame)
            root.after(timer, update, ind)

        gif_image_label = Label(root)
        gif_image_label.pack(anchor=CENTER)
        root.after(0, update, 0)
        return

        # randomizing opening images

    random_integer = random.randint(0, 2)

    Gif_loop(gif_image_list[random_integer], frame_count_list[random_integer], 30)


# for intro page EFF2.1
def intropage(root, label):
    root.state('zoomed')
    # using geometry to place in center
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.configure(bg='black')

    label.place(x=0, y=0)
    root.after(3600, label.place_forget)
