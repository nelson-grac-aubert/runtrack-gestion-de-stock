import ttkbootstrap as ttk
from scripts.graphic.class_app import ProductApp

def main():
    app = ttk.Window(themename="cosmo")  # ou "litera", "morph", "superhero", etc.
    ProductApp(app)
    app.mainloop()

if __name__ == "__main__":
    main()