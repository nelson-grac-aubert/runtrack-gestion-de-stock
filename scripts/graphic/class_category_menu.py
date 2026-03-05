import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from scripts.logic.class_stockmanager import StockManager


class CategoryMenu:
    """
    Window for viewing, adding, editing and deleting categories.
    """

    def __init__(self, root):
        """
        Initialize the category menu window.
        """
        self.root = root
        self.root.title("Category Manager")

        self.manager = StockManager()
        self.selected_category_id = None

        self.create_widgets()
        self.load_categories()

    def create_widgets(self):
        """
        Create UI components.
        """
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=BOTH, expand=True)

        # Title
        ttk.Label(
            main_frame,
            text="Category Manager",
            font=("Segoe UI", 20, "bold")
        ).pack(pady=10)

        # List container
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=BOTH, expand=True, pady=10)

        # Category list
        self.category_list = ttk.Treeview(
            list_frame,
            columns=("id", "name"),
            show="headings",
            height=10,
            bootstyle=INFO
        )
        self.category_list.heading("id", text="ID")
        self.category_list.heading("name", text="Name")
        self.category_list.column("id", width=60)
        self.category_list.column("name", width=200)
        self.category_list.pack(side=LEFT, fill=BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            list_frame,
            orient="vertical",
            command=self.category_list.yview
        )
        scrollbar.pack(side=RIGHT, fill=Y)
        self.category_list.configure(yscrollcommand=scrollbar.set)

        # Selection event
        self.category_list.bind("<<TreeviewSelect>>", self.on_select)

        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=X, pady=10)

        ttk.Button(
            btn_frame,
            text="Add Category",
            bootstyle=PRIMARY,
            command=self.open_add_window
        ).pack(fill=X, pady=5)

        ttk.Button(
            btn_frame,
            text="Edit Category",
            bootstyle=PRIMARY,
            command=self.open_edit_window
        ).pack(fill=X, pady=5)

        ttk.Button(
            btn_frame,
            text="Delete Category",
            bootstyle=DANGER,
            command=self.delete_category
        ).pack(fill=X, pady=5)

    def load_categories(self):
        """
        Load all categories into the list.
        """
        for row in self.category_list.get_children():
            self.category_list.delete(row)

        categories = self.manager.get_all_categories()

        for cat in categories:
            self.category_list.insert("", END, values=(cat.id, cat.name))

    def on_select(self, event):
        """
        Handle category selection.
        """
        selected = self.category_list.selection()
        if selected:
            values = self.category_list.item(selected[0], "values")
            self.selected_category_id = int(values[0])

    def open_add_window(self):
        """
        Open a window to add a new category.
        """
        win = ttk.Toplevel(self.root)
        win.title("Add Category")

        ttk.Label(win, text="Category name:", font=("Segoe UI", 12)).pack(pady=10)
        entry = ttk.Entry(win)
        entry.pack(pady=5)

        def add():
            name = entry.get().strip()
            if not name:
                messagebox.showerror("Error", "Name cannot be empty.")
                return

            from scripts.logic.class_category import Category
            new_cat = Category(name=name)
            new_cat.insert_into_database()

            win.destroy()
            self.load_categories()

        ttk.Button(win, text="Add", bootstyle=SUCCESS, command=add).pack(pady=10)

    def open_edit_window(self):
        """
        Open a window to edit the selected category.
        """
        if not self.selected_category_id:
            messagebox.showerror("Error", "Select a category first.")
            return

        win = ttk.Toplevel(self.root)
        win.title("Edit Category")

        ttk.Label(win, text="New name:", font=("Segoe UI", 12)).pack(pady=10)
        entry = ttk.Entry(win)
        entry.pack(pady=5)

        def edit():
            new_name = entry.get().strip()
            if not new_name:
                messagebox.showerror("Error", "Name cannot be empty.")
                return

            cat = self.manager.get_category_by_id(self.selected_category_id)
            cat.name = new_name
            cat.update_name_in_database()

            win.destroy()
            self.load_categories()

        ttk.Button(win, text="Save", bootstyle=SUCCESS, command=edit).pack(pady=10)

    def delete_category(self):
        """
        Delete the selected category after confirmation.
        """
        if not self.selected_category_id:
            messagebox.showerror("Error", "Select a category first.")
            return

        confirm = messagebox.askyesno(
            "Confirm deletion",
            "Are you sure you want to delete this category?"
        )

        if not confirm:
            return

        cat = self.manager.get_category_by_id(self.selected_category_id)
        cat.delete_from_database()

        self.load_categories()