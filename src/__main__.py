import customtkinter  # type: ignore

from PowerManager import get_system_platform
from Window import Window


class App(customtkinter.CTk):
    def __init__(self) -> None:
        self.mode = customtkinter.set_appearance_mode("dark")
        self.color_theme = customtkinter.set_default_color_theme("dark-blue")
        super().__init__()
        self.title("PowerRangers")
        self.geometry("300x300")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.window = Window(master=self, command=self.go_button)

    def go_button(self):
        system = get_system_platform()
        select = self.window.get()
        if select == "Power Off":
            system.power_off()
        elif select == "Power Reboot":
            system.restart()
        else:
            system.log_out()


if __name__ == "__main__":
    app = App()
    app.mainloop()
