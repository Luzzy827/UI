import tkinter as tk

class HarpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Harp App")
        self.root.geometry("800x480")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.main_frame, width=800, height=480)
        self.canvas.pack()

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.select_option)
        self.root.bind("<Escape>", self.go_back)

        self.current_page = "home"
        self.parent_page = None  # 新增上级页面属性

        self.home_options = ["Harp", "LED Lighting"]
        self.harp_options = ["Free Play Mode", "Harp Hero", "Setting"]
        self.current_selection = 0

        self.create_home_page()

    def create_home_page(self):
        self.canvas.delete("all")
        self.current_page = "home"
        self.parent_page = None
        self.current_selection = 0

        self.harp_button = tk.Label(self.canvas, text="Harp", font=("Arial", 24), bg="white", width=15, height=5)
        self.harp_button_window = self.canvas.create_window(250, 200, window=self.harp_button)
        self.harp_button_border = self.canvas.create_rectangle(150, 100, 350, 300, outline="white", width=2)

        self.led_button = tk.Label(self.canvas, text="LED Lighting", font=("Arial", 24), bg="white", width=15, height=5)
        self.led_button_window = self.canvas.create_window(550, 200, window=self.led_button)
        self.led_button_border = self.canvas.create_rectangle(450, 100, 650, 300, outline="white", width=2)

        self.update_selection()

    def create_harp_page(self):
        self.canvas.delete("all")
        self.current_page = "harp"
        self.parent_page = "home"
        self.current_selection = 0

        self.fpm_button = tk.Label(self.canvas, text="Free Play Mode", font=("Arial", 24), bg="white", width=15, height=5)
        self.fpm_button_window = self.canvas.create_window(150, 200, window=self.fpm_button)
        self.fpm_button_border = self.canvas.create_rectangle(50, 100, 250, 300, outline="white", width=2)

        self.hh_button = tk.Label(self.canvas, text="Harp Hero", font=("Arial", 24), bg="white", width=15, height=5)
        self.hh_button_window = self.canvas.create_window(450, 200, window=self.hh_button)
        self.hh_button_border = self.canvas.create_rectangle(350, 100, 550, 300, outline="white", width=2)

        self.harp_setting_button = tk.Label(self.canvas, text="Setting", font=("Arial", 24), bg="white", width=15,height=5)
        self.harp_setting_button_window = self.canvas.create_window(750, 200, window=self.harp_setting_button)
        self.harp_setting_button_border = self.canvas.create_rectangle(650, 100, 850, 300, outline="white", width=2)

        self.create_back_text()
        self.update_selection()

    def create_free_play_mode_page(self):
        self.canvas.delete("all")
        self.current_page = "free_play_mode"
        self.parent_page = "harp"
        self.current_selection = 0

        label = tk.Label(self.canvas, text="Free Play Mode Page", font=("Arial", 24), bg="white")
        self.canvas.create_window(400, 240, window=label)

        self.create_back_text()

    def create_led_lighting_page(self):
        self.canvas.delete("all")
        self.current_page = "led"
        self.parent_page = "home"
        self.current_selection = 0

        self.mode1_button = tk.Label(self.canvas, text="Mode 1", font=("Arial", 24), bg="white", width=15, height=5)
        self.mode1_button_window = self.canvas.create_window(250, 200, window=self.mode1_button)
        self.mode1_button_border = self.canvas.create_rectangle(150, 100, 350, 300, outline="white", width=2)

        self.mode2_button = tk.Label(self.canvas, text="Mode 2", font=("Arial", 24), bg="white", width=15, height=5)
        self.mode2_button_window = self.canvas.create_window(550, 200, window=self.mode2_button)
        self.mode2_button_border = self.canvas.create_rectangle(450, 100, 650, 300, outline="white", width=2)

        self.create_back_text()
        self.update_selection()

    def create_back_text(self):
        back_text = tk.Label(self.canvas, text="Back to last page", font=("Arial", 12), fg="blue")
        self.canvas.create_window(700, 450, window=back_text)

    def move_left(self, event):
        if self.current_page == "home":
            self.current_selection = (self.current_selection - 1) % len(self.home_options)
        elif self.current_page == "harp":
            self.current_selection = (self.current_selection - 1) % len(self.harp_options)
        self.update_selection()

    def move_right(self, event):
        if self.current_page == "home":
            self.current_selection = (self.current_selection + 1) % len(self.home_options)
        elif self.current_page == "harp":
            self.current_selection = (self.current_selection + 1) % len(self.harp_options)
        self.update_selection()

    def select_option(self, event):
        if self.current_page == "home":
            if self.current_selection == 0:
                self.create_harp_page()
            elif self.current_selection == 1:
                self.create_led_lighting_page()
        elif self.current_page == "harp":
            if self.current_selection == 0:
                self.create_free_play_mode_page()
            else:
                print(f"Selected: {self.harp_options[self.current_selection]}")  # Placeholder for actual selection handling

    def update_selection(self):
        if self.current_page == "home":
            buttons = [self.harp_button, self.led_button]
            borders = [self.harp_button_border, self.led_button_border]
        elif self.current_page == "harp":
            buttons = [self.fpm_button, self.hh_button, self.harp_setting_button]
            borders = [self.fpm_button_border, self.hh_button_border, self.harp_setting_button_border]

        for i, button in enumerate(buttons):
            button.config(bg="lightgreen" if i == self.current_selection else "white")
            self.canvas.itemconfig(borders[i], outline="green" if i == self.current_selection else "white", width=4 if i == self.current_selection else 2)

    def go_back(self, event=None):
        if self.parent_page == "home":
            self.create_home_page()
        elif self.parent_page == "harp":
            self.create_harp_page()
        elif self.parent_page == "led":
            self.create_led_lighting_page()

if __name__ == "__main__":
    root = tk.Tk()
    app = HarpApp(root)
    root.mainloop()
