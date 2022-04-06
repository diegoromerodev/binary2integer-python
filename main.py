from tkinter import *
from converter import convert

root = Tk()


def click_handle():
    binary_text = binary_field.get()
    conversion_result = convert(binary_text)
    label_guide.config(text=conversion_result)


def delete_placeholder(*args):
    binary_field.delete(0, 'end')
    binary_field.unbind('<Button-1>')


label_intro = Label(root, text="B2INTEGER")
label_guide = Label(root, text="Enter a sequence of binary digits")
binary_field = Entry(root, width=80, borderwidth=2)
binary_field.insert(0, "Enter binary numbers here")
binary_delete_id = binary_field.bind('<Button-1>', delete_placeholder)
convert_button = Button(root, text="Convert to integers",
                        padx=50, pady=5, fg="white", bg="blue", command=click_handle)


label_intro.grid(column=0, row=0)
label_guide.grid(column=0, row=1)
binary_field.grid(column=0, row=2)
convert_button.grid(column=0, row=3)

root.mainloop()
