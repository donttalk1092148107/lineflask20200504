import tkinter as tk

window = tk.Tk()
top_frame = tk.Frame(window)


top_frame.pack()
bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)


def echo_hello():
    print('hello world :)')


left_button = tk.Button(top_frame, text='Red', fg='red')

left_button.pack(side=tk.LEFT)

middle_button = tk.Button(top_frame, text='Green', fg='green')
middle_button.pack(side=tk.LEFT)

right_button = tk.Button(top_frame, text='Blue', fg='blue')
right_button.pack(side=tk.LEFT)

bottom_button = tk.Button(bottom_frame, text='Black', fg='black', command=echo_hello)

bottom_button.pack(side=tk.BOTTOM)

window.mainloop()