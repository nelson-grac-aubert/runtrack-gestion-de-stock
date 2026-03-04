import ttkbootstrap as ttk
from scripts.graphic.class_main_menu import MainMenu

def main():
    app = ttk.Window(themename="cosmo")
    MainMenu(app)
    app.mainloop()

if __name__ == "__main__":
    main()
