import os
import tkinter
import tkinter.filedialog


# TODO Create better UI
# TODO Handel Multiple subtitles
# TODO Handel more errors

def get_address():
    """Get the absolut path of the srt or ass file"""
    file_address = tkinter.filedialog.askopenfilename(title="Open a file",
                                                      filetypes=[('subtitle_srt', '*.srt'),
                                                                 ("subtitle_ass", "*.ass")])
    if file_address:
        result_text.set(file_address)


def change_encoding():
    """Change the .srt or .ass file encoding """

    # Absolut path of the program to save the new .srt/.ass file.
    save_address = os.path.join(os.getcwd(), "convert_srt")
    # Absolut path of the .srt or .ass file for convert.
    subtitle_address = result_text.get()
    # If we have the file address then do the encoding.
    if subtitle_address:
        # Get the name and the type of the file. ex: seven_samurai.srt
        address_tail = os.path.split(subtitle_address)[1]
        # Decoding
        with open(subtitle_address, 'rb') as subtitle_file:
            decoded_file = subtitle_file.read().decode('cp1256')

        # Encode with utf-8 and save it.
        with open(os.path.join(save_address, address_tail), "w", encoding="utf-8") as subtitle_encoded_file:
            subtitle_encoded_file.write(decoded_file)

        result_text.set("Convert is done. You can find your file in the program folder!")

    else:
        result_text.set("Please Chose A File First!")


# Create and config main window
mainWindow = tkinter.Tk()
mainWindow.title("Convert SRT")
mainWindow.geometry("480x240")
mainWindow["padx"] = 8
mainWindow["pady"] = 8

# Configure main window columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=2)

# Configure main window rows
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)

# Main label
main_title = tkinter.Label(mainWindow, text="SRT Encoder")
main_title.grid(row=0, column=1, sticky='n')

# Buttons Frame
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=1, column=0, sticky='nw')

# Buttons in the button frame
button_brows = tkinter.Button(button_frame, text="Brows", command=get_address)
button_change_encode = tkinter.Button(button_frame, text="Change Encoding", command=change_encoding)
button_exit = tkinter.Button(button_frame, text="Exit", command=mainWindow.destroy)

button_brows.grid(row=0, column=0, sticky='n')
button_change_encode.grid(row=1, column=0, sticky='n')
button_exit.grid(row=2, column=0, sticky='n')

# Result Frame
result_frame = tkinter.Frame(mainWindow)
result_frame.grid(row=1, column=2, sticky='ew')
# Result Message
result_text = tkinter.StringVar()
result_label = tkinter.Message(result_frame, textvariable=result_text)
result_label.grid(row=0, column=0)

mainWindow.mainloop()
