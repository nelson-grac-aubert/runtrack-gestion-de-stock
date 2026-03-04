import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class MainMenu:
    """
    Main menu window for Supermarket Manager 3000.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket Manager 3000")

        self.create_widgets()

    def create_widgets(self):
        """
        Create the main menu UI.
        """
        frame = ttk.Frame(self.root, padding=40)
        frame.pack(fill=BOTH, expand=True)

        title = ttk.Label(
            frame,
            text="Supermarket Manager 3000",
            font=("Segoe UI", 22, "bold")
        )
        title.pack(pady=20)

        ttk.Button(
            frame,
            text="View Products",
            bootstyle=PRIMARY,
            command=lambda: self.open_blank_window("View Products")
        ).pack(fill=X, pady=10)

        ttk.Button(
            frame,
            text="Edit Products",
            bootstyle=PRIMARY,
            command=lambda: self.open_blank_window("Edit Products")
        ).pack(fill=X, pady=10)

        ttk.Button(
            frame,
            text="Edit Categories",
            bootstyle=PRIMARY,
            command=lambda: self.open_blank_window("Edit Categories")
        ).pack(fill=X, pady=10)

        ttk.Button(
            frame,
            text="Quit",
            bootstyle=DANGER,
            command=self.root.quit
        ).pack(fill=X, pady=10)


    def open_blank_window(self, title):
        new_window = ttk.Toplevel(self.root)
        new_window.title(title)

        ttk.Label(
            new_window,
            text=f"{title} Window",
            font=("Segoe UI", 16)
        ).pack(pady=20)
