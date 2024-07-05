import tkinter as tk

class HarpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Harp App")
        self.root.geometry("900x500")

        self.main_frame = tk.Frame(self.root)#self.main_frame 是一个实例属性，用于存储创建的 Frame 小部件。
        # tk.Frame 是 tkinter 的一个小部件类，用于容纳和组织其他小部件。它通常用于分组和布局界面元素。
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        #pack 是 tkinter 中的一种布局管理器，用于在父容器中排列小部件
        #fill 选项指定了小部件在父容器中填充的方向
        #tk.BOTH 表示小部件将填充其父容器的水平和垂直方向
        #expand=True 表示 self.main_frame 将会扩展以占据主窗口中所有可用的空间（不仅仅是在初始大小之外的空间），这通常会导致小部件在父容器调整大小时自动调整自身的大小。
        self.canvas = tk.Canvas(self.main_frame, width=900, height=500)
        self.canvas.pack()

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.select_option)
        self.root.bind("<Escape>", self.go_back)

        self.page_history = []
        self.current_page = "home"
        self.home_options = ["Harp", "LED Lighting"]
        self.harp_options = ["Free Play Mode","Harp Hero","Setting"]
        self.LED_options = ["Turn on","Turn off","Change Color"]
        self.instrument_options = ["Harp","Guitar","Piano"]
        self.setting_options = ["Volume","Delay"]
        self.current_selection = 0  # 这里后面循环选择要用

        self.create_home_page()
    # 创建首页
    def create_home_page(self):
        self.page_history.clear()  # Clear history when returning to home
        self.canvas.delete("all")
        self.current_page = "home"
        self.current_selection = 0

        self.harp_button = tk.Label(self.canvas, text="Harp", font=("Arial", 24), bg="white", width=15, height=5)
        self.harp_button_window = self.canvas.create_window(250, 200, window=self.harp_button)
        self.harp_button_border = self.canvas.create_rectangle(150, 100, 350, 300, outline="white", width=2)

        self.led_button = tk.Label(self.canvas, text="LED Lighting", font=("Arial", 24), bg="white", width=15, height=5)
        self.led_button_window = self.canvas.create_window(550, 200, window=self.led_button)
        self.led_button_border = self.canvas.create_rectangle(450, 100, 650, 300, outline="white", width=2)

        self.update_selection()
    #创建首页选中harp后的页面
    def create_harp_page(self):#Creat new page for harp
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
    # 创建选中harp中的free play mode后的页面
    def create_FPM_page(self):#Creat new page for Free Play Mode
        self.canvas.delete("all")
        self.current_page = "instrument"
        self.parent_page = "harp"
        self.current_selection = 0

        self.Laserharp_button = tk.Label(self.canvas, text="Laser Harp", font=("Arial", 24), bg="white", width=15, height=5)
        self.Laserharp_button_window = self.canvas.create_window(150, 200, window=self.Laserharp_button)
        self.Laserharp_button_border = self.canvas.create_rectangle(50, 100, 250, 300, outline="white", width=2)

        self.guitar_button = tk.Label(self.canvas, text="Guitar", font=("Arial", 24), bg="white", width=15, height=5)
        self.guitar_button_window = self.canvas.create_window(450, 200, window=self.guitar_button)
        self.guitar_button_border = self.canvas.create_rectangle(350, 100, 550, 300, outline="white", width=2)

        self.piano_button = tk.Label(self.canvas, text="Piano", font=("Arial", 24), bg="white", width=15,height=5)
        self.piano_button_window = self.canvas.create_window(750, 200, window=self.piano_button)
        self.piano_button_border = self.canvas.create_rectangle(650, 100, 850, 300, outline="white", width=2)

        self.create_back_text()
        self.update_selection()
    # 创建选中harp后的setting的页面
    def create_setting_page(self):
        self.canvas.delete("all")
        self.current_page = "setting"
        self.parent_page = "harp"
        self.current_selection = 0

        self.volume_button = tk.Label(self.canvas, text="Volume", font=("Arial", 24), bg="white", width=15, height=5)
        self.volume_button_window = self.canvas.create_window(250, 200, window=self.volume_button)
        self.volume_button_border = self.canvas.create_rectangle(150, 100, 350, 300, outline="white", width=2)

        self.delay_button = tk.Label(self.canvas, text="Delay", font=("Arial", 24), bg="white", width=15, height=5)
        self.delay_button_window = self.canvas.create_window(550, 200, window=self.delay_button)
        self.delay_button_border = self.canvas.create_rectangle(450, 100, 650, 300, outline="white", width=2)

        self.create_back_text()
        self.update_selection()
    # 创建在首页选中LEDlighting后的页面
    def create_LED_page(self):#Creat new page for Free Play Mode
        self.canvas.delete("all")
        self.current_page = "LED lighting"
        self.parent_page = "home"
        self.current_selection = 0

        self.turnon_button = tk.Label(self.canvas, text="Turn On", font=("Arial", 24), bg="white", width=15, height=5)
        self.turnon_button_window = self.canvas.create_window(150, 200, window=self.turnon_button)
        self.turnon_button_border = self.canvas.create_rectangle(50, 100, 250, 300, outline="white", width=2)

        self.turnoff_button = tk.Label(self.canvas, text="Turn Off", font=("Arial", 24), bg="white", width=15, height=5)
        self.turnoff_button_window = self.canvas.create_window(450, 200, window=self.turnoff_button)
        self.turnoff_button_border = self.canvas.create_rectangle(350, 100, 550, 300, outline="white", width=2)

        self.changecolor_button = tk.Label(self.canvas, text="Change Color", font=("Arial", 24), bg="white", width=15,height=5)
        self.changecolor_button_window = self.canvas.create_window(750, 200, window=self.changecolor_button)
        self.changecolor_button_border = self.canvas.create_rectangle(650, 100, 850, 300, outline="white", width=2)

        self.create_back_text()
        self.update_selection()

    def create_back_text(self):
        back_text = tk.Label(self.canvas, text="Back to last page", font=("Arial", 12), fg="gray")
        self.canvas.create_window(700, 450, window=back_text)
    # 左键功能
    def move_left(self, event):
        if self.current_page == "home":
            self.current_selection = (self.current_selection - 1) % len(self.home_options)
        elif self.current_page == "harp":
            self.current_selection = (self.current_selection - 1) % len(self.harp_options)
        elif self.current_page == "instrument":
            self.current_selection = (self.current_selection - 1) % len(self.instrument_options)
        elif self.current_page == "setting":
            self.current_selection = (self.current_selection - 1) % len(self.setting_options)
        elif self.current_page == "LED lighting":
            self.current_selection = (self.current_selection - 1) % len(self.LED_options)
        self.update_selection()
    # 右键功能
    def move_right(self, event):
        if self.current_page == "home":
            self.current_selection = (self.current_selection + 1) % len(self.home_options)
        elif self.current_page == "harp":
            self.current_selection = (self.current_selection + 1) % len(self.harp_options)
        elif self.current_page == "instrument":
            self.current_selection = (self.current_selection + 1) % len(self.instrument_options)
        elif self.current_page == "setting":
            self.current_selection = (self.current_selection + 1) % len(self.setting_options)
        elif self.current_page == "LED lighting":
            self.current_selection = (self.current_selection + 1) % len(self.LED_options)
        self.update_selection()
    # 空格键的选择功能
    def select_option(self, event):
        if self.current_page == "home":
            if self.current_selection == 0:
                self.create_harp_page()
            elif self.current_selection == 1:
                self.create_LED_page()
        elif self.current_page == "harp":
            if self.current_selection == 0:
                self.create_FPM_page()
            elif self.current_selection == 1:
                # self.create_hh_page()
                print("Harp hero")
            elif self.current_selection == 2:
                self.create_setting_page()
        elif self.current_page == "instrument":
            if self.current_selection == 0:
                # self.create_laserharp_page()
                print("laserharp")
            elif self.current_selection == 1:
                # self.create_guitar_page()
                print("guitar")
            elif self.current_selection == 2:
                # self.create_piano_page()
                print("piano")
        elif self.current_page == "setting":
            if self.current_selection == 0:
                # self.create_volume_page()
                print("volume")
            elif self.current_selection == 1:
                # self.create_delay_page()
                print("delay")
        elif self.current_page == "LED lighting":
            if self.current_selection == 0:
                print("Turn on")
            elif self.current_selection == 1:
                print("Turn off")
            elif self.current_selection == 2:
                # self.create_colorchange_page()
                print("Change Color")

    def update_selection(self):
        if self.current_page == "home":
            buttons = [self.harp_button, self.led_button]
            borders = [self.harp_button_border, self.led_button_border]
        elif self.current_page == "harp":
            buttons = [self.fpm_button, self.hh_button, self.harp_setting_button]
            borders = [self.fpm_button_border, self.hh_button_border, self.harp_setting_button_border]
        elif self.current_page == "instrument":
            buttons = [self.Laserharp_button, self.guitar_button, self.piano_button]
            borders = [self.Laserharp_button_border, self.guitar_button_border, self.piano_button_border]
        elif self.current_page == "setting":
            buttons = [self.volume_button, self.delay_button]
            borders = [self.volume_button_border, self.delay_button_border]
        elif self.current_page == "LED lighting":
            buttons = [self.turnon_button, self.turnoff_button, self.changecolor_button]
            borders = [self.turnon_button_border, self.turnoff_button_border, self.changecolor_button_border]


        # 选中按钮的变色功能实现
        for i, button in enumerate(buttons):
            button.config(bg="lightgreen" if i == self.current_selection else "white")
            self.canvas.itemconfig(borders[i], outline="green" if i == self.current_selection else "white",
                                   width=4 if i == self.current_selection else 2)


    def go_back(self, event=None):
        if self.parent_page == "home":
            self.create_home_page()
        elif self.parent_page == "harp":
            self.create_harp_page()
        # elif self.parent_page == "":
        #     self.create_led_lighting_page()


if __name__ == "__main__":
    root = tk.Tk()
    app = HarpApp(root)
    root.mainloop()
