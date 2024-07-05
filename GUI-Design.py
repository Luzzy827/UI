import tkinter as tk

class HarpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Harp App")
        self.root.geometry("800x480")

        self.selected_option = 0  # 0: Harp, 1: LED Lighting

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.main_frame, width=800, height=480)
        self.canvas.pack()

        self.root.bind("<Left>", self.switch_left)
        self.root.bind("<Right>", self.switch_right)
        self.root.bind("<space>", self.confirm_selection)

        self.create_home_page()

    def create_home_page(self):

        self.canvas.delete("all")

        # 绘制 Harp 按钮
        self.harp_button = tk.Label(self.canvas, text="Harp", font=("Arial", 24), bg="lightgreen", width=15, height=5)
        self.harp_button_window = self.canvas.create_window(250, 200, window=self.harp_button)
        self.harp_button_border = self.canvas.create_rectangle(150, 100, 350, 300, outline="green", width=2)

        # 绘制 LED Lighting 按钮
        self.led_button = tk.Label(self.canvas, text="LED Lighting", font=("Arial", 24), bg="white", width=15, height=5)
        self.led_button_window = self.canvas.create_window(550, 200, window=self.led_button)
        self.led_button_border = self.canvas.create_rectangle(450, 100, 650, 300, outline="green", width=2)

        self.update_selection()

    def update_selection(self):
        if self.selected_option == 0:
            self.harp_button.config(bg="lightgreen")
            self.led_button.config(bg="white")
            self.canvas.itemconfig(self.harp_button_border, width=4)
            self.canvas.itemconfig(self.led_button_border, width=2)
        else:
            self.harp_button.config(bg="white")
            self.led_button.config(bg="lightgreen")
            self.canvas.itemconfig(self.harp_button_border, width=2)
            self.canvas.itemconfig(self.led_button_border, width=4)

    def switch_left(self, event):
        self.selected_option = 0
        self.update_selection()

    def switch_right(self, event):
        self.selected_option = 1
        self.update_selection()

    def confirm_selection(self, event):
        if self.selected_option == 0:
            self.create_harp_hero_page()
        else:
            self.create_led_lighting_page()

    def create_harp_hero_page(self):
        self.clear_frame()

        harp_label = tk.Label(self.main_frame, text="Harp", font=("Arial", 24))
        harp_label.pack(pady=20)

        select_instrument_button = tk.Button(self.main_frame, text="Select Instrument", font=("Arial", 18), command=self.create_select_instrument_page)
        select_instrument_button.pack(pady=10)

        select_song_button = tk.Button(self.main_frame, text="Select Song", font=("Arial", 18), command=self.create_select_song_page)
        select_song_button.pack(pady=10)

        play_mode_button = tk.Button(self.main_frame, text="Free Play Mode", font=("Arial", 18), command=self.create_play_mode_page)
        play_mode_button.pack(pady=10)

        back_button = tk.Button(self.main_frame, text="Back", font=("Arial", 18), command=self.create_home_page)
        back_button.pack(pady=10)

    def create_led_lighting_page(self):
        self.clear_frame()

        led_label = tk.Label(self.main_frame, text="LED Lighting", font=("Arial", 24))
        led_label.pack(pady=20)

        led_settings_button = tk.Button(self.main_frame, text="LED Settings", font=("Arial", 18))
        led_settings_button.pack(pady=10)

        back_button = tk.Button(self.main_frame, text="Back", font=("Arial", 18), command=self.create_home_page)
        back_button.pack(pady=10)

    def create_select_instrument_page(self):
        self.clear_frame()

        instrument_label = tk.Label(self.main_frame, text="Select Instrument", font=("Arial", 24))
        instrument_label.pack(pady=20)

        instruments = ["Harp", "Piano", "Guitar"]
        for instrument in instruments:
            button = tk.Button(self.main_frame, text=instrument, font=("Arial", 18))
            button.pack(pady=5)

        back_button = tk.Button(self.main_frame, text="Back", font=("Arial", 18), command=self.create_harp_hero_page)
        back_button.pack(pady=10)

    def create_select_song_page(self):
        self.clear_frame()

        song_label = tk.Label(self.main_frame, text="Select Song", font=("Arial", 24))
        song_label.pack(pady=20)

        songs = ["Song 1", "Song 2", "Song 3"]
        for song in songs:
            button = tk.Button(self.main_frame, text=song, font=("Arial", 18))
            button.pack(pady=5)

        back_button = tk.Button(self.main_frame, text="Back", font=("Arial", 18), command=self.create_harp_hero_page)
        back_button.pack(pady=10)


    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HarpApp(root)
    root.mainloop()

