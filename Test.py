import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Selection UI")
        self.options = ["Harp", "LED Lighting", "Setting"]
        self.current_selection = 0

        self.frames = [tk.Frame(self.root, width=300, height=500, bg="white", highlightbackground="green", highlightthickness=2) for _ in self.options]
        self.labels = [tk.Label(frame, text=option, font=("Helvetica", 24)) for frame, option in zip(self.frames, self.options)]

        for i, frame in enumerate(self.frames):
            frame.grid(row=0, column=i, padx=20, pady=20)
            frame.grid_propagate(False)
            self.labels[i].pack(expand=True)

        self.update_selection()

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.select_option)

    def move_left(self, event):
        self.current_selection = (self.current_selection - 1) % len(self.options)
        self.update_selection()

    def move_right(self, event):
        self.current_selection = (self.current_selection + 1) % len(self.options)
        self.update_selection()

    def select_option(self, event):
        for frame in self.frames:
            frame.config(bg="white")
        self.frames[self.current_selection].config(bg="lightgreen")

    def update_selection(self):
        for i, frame in enumerate(self.frames):
            frame.config(highlightbackground="green" if i == self.current_selection else "white")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

