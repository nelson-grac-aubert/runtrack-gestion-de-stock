import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar

class ProductApp:
    """
    Main application window for managing products.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Product Manager")

        self.create_widgets()

    def create_widgets(self):
        """
        Create all UI components.
        """

        # Frame for the Treeview
        self.table_frame = ttk.Frame(self.root, padding=10)
        self.table_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # Frame for the form
        self.form_frame = ttk.Frame(self.root, padding=10)
        self.form_frame.pack(side=RIGHT, fill=Y)

        # Treeview
        self.tree = ttk.Treeview(
            self.table_frame,
            columns=("name", "description", "price", "quantity", "category"),
            show="headings",
            bootstyle=INFO
        )
        self.tree.pack(fill=BOTH, expand=True)

        # Form fields
        ttk.Label(self.form_frame, text="Name").pack(anchor=W)
        self.entry_name = ttk.Entry(self.form_frame)
        self.entry_name.pack(fill=X)

        ttk.Label(self.form_frame, text="Description").pack(anchor=W)
        self.entry_description = ttk.Entry(self.form_frame)
        self.entry_description.pack(fill=X)

        ttk.Label(self.form_frame, text="Price").pack(anchor=W)
        self.entry_price = ttk.Entry(self.form_frame)
        self.entry_price.pack(fill=X)

        ttk.Label(self.form_frame, text="Quantity").pack(anchor=W)
        self.entry_quantity = ttk.Entry(self.form_frame)
        self.entry_quantity.pack(fill=X)

        ttk.Label(self.form_frame, text="Category ID").pack(anchor=W)
        self.entry_category = ttk.Entry(self.form_frame)
        self.entry_category.pack(fill=X)

        # Buttons
        ttk.Button(self.form_frame, text="Add Product", bootstyle=SUCCESS).pack(fill=X, pady=5)
        ttk.Button(self.form_frame, text="Update Product", bootstyle=WARNING).pack(fill=X, pady=5)
        ttk.Button(self.form_frame, text="Delete Product", bootstyle=DANGER).pack(fill=X, pady=5)
        ttk.Button(self.form_frame, text="Refresh", bootstyle=INFO).pack(fill=X, pady=5)