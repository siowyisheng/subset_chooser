import tkinter as tk
import tkinter.ttk as ttk
from random import sample

class App(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        ttk.Label(self.master, text=f'Paste items here').pack()
        self.text = tk.Text(self.master, width=50, height=20)
        self.text.config(state=tk.NORMAL)
        self.text.pack()
        self.text.configure(font=("Helvetica", 12))

        ttk.Label(self.master, text=f'How many to choose?').pack()
        self.samplesize_dropdown = ttk.Combobox(self.master,values=([str(i+1) for i in range(15)]))
        self.samplesize_dropdown.pack()

        self.button_frame = ttk.Frame(self.master, padding=(0, 20, 0, 0))
        self.button_frame.pack()
        self.button = ttk.Button(self.button_frame,
                                 text='Shuffle',
                                 command=self.get_sample,
                                 padding='20 10')
        self.button.pack()

    def get_sample(self):
        sample_size = int(self.samplesize_dropdown.get())
        lines = self.text.get('1.0', 'end').splitlines()
        self.text.delete(1.0, tk.END)
        for line in sample(lines, sample_size):
            self.text.insert(
                'end',
                line + '\n',
            )


def main():
    root = tk.Tk()
    root.title('Subset Chooser')
    App(root, padding=20, width=400, height=50).pack()
    root.mainloop()


if __name__ == '__main__':
    main()