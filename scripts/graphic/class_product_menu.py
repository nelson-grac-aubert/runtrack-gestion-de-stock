import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from scripts.logic.class_stockmanager import StockManager
from scripts.logic.class_product import Product


class ProductMenu:
    """
    Window for viewing, adding, editing and deleting products.
    """

    def __init__(self, root):
        """
        Initialize the product menu window.
        """
        self.root = root
        self.root.title("Product Manager")

        self.manager = StockManager()
        self.selected_product_id = None

        self.create_widgets()
        self.load_products()

    def create_widgets(self):
        """
        Create UI components.
        """
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=BOTH, expand=True)

        # Title
        ttk.Label(
            main_frame,
            text="Product Manager",
            font=("Segoe UI", 20, "bold")
        ).pack(pady=10)

        # List container
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=BOTH, expand=True, pady=10)

        # Product list
        self.product_list = ttk.Treeview(
            list_frame,
            columns=("id", "name", "price", "quantity", "category"),
            show="headings",
            height=12,
            bootstyle=INFO
        )
        self.product_list.heading("id", text="ID")
        self.product_list.heading("name", text="Name")
        self.product_list.heading("price", text="Price")
        self.product_list.heading("quantity", text="Qty")
        self.product_list.heading("category", text="Category ID")

        self.product_list.column("id", width=50)
        self.product_list.column("name", width=180)
        self.product_list.column("price", width=80)
        self.product_list.column("quantity", width=80)
        self.product_list.column("category", width=100)

        self.product_list.pack(side=LEFT, fill=BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            list_frame,
            orient="vertical",
            command=self.product_list.yview
        )
        scrollbar.pack(side=RIGHT, fill=Y)
        self.product_list.configure(yscrollcommand=scrollbar.set)

        # Selection event
        self.product_list.bind("<<TreeviewSelect>>", self.on_select)

        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=X, pady=10)

        ttk.Button(
            btn_frame,
            text="Add Product",
            bootstyle=PRIMARY,
            command=self.open_add_window
        ).pack(fill=X, pady=5)

        ttk.Button(
            btn_frame,
            text="Edit Product",
            bootstyle=PRIMARY,
            command=self.open_edit_window
        ).pack(fill=X, pady=5)

        ttk.Button(
            btn_frame,
            text="Delete Product",
            bootstyle=DANGER,
            command=self.delete_product
        ).pack(fill=X, pady=5)

    def load_products(self):
        """
        Load all products into the list.
        """
        for row in self.product_list.get_children():
            self.product_list.delete(row)

        products = self.manager.get_all_products()

        for p in products:
            self.product_list.insert(
                "",
                END,
                values=(p.id, p.name, p.price, p.quantity, p.id_category)
            )

    def on_select(self, event):
        """
        Handle product selection.
        """
        selected = self.product_list.selection()
        if selected:
            values = self.product_list.item(selected[0], "values")
            self.selected_product_id = int(values[0])

    def open_add_window(self):
        """
        Open a window to add a new product.
        """
        win = ttk.Toplevel(self.root)
        win.title("Add Product")

        # Inputs
        ttk.Label(win, text="Name:", font=("Segoe UI", 12)).pack(pady=5)
        entry_name = ttk.Entry(win)
        entry_name.pack(pady=5)

        ttk.Label(win, text="Description:", font=("Segoe UI", 12)).pack(pady=5)
        entry_desc = ttk.Entry(win)
        entry_desc.pack(pady=5)

        ttk.Label(win, text="Price:", font=("Segoe UI", 12)).pack(pady=5)
        entry_price = ttk.Entry(win)
        entry_price.pack(pady=5)

        ttk.Label(win, text="Quantity:", font=("Segoe UI", 12)).pack(pady=5)
        entry_qty = ttk.Entry(win)
        entry_qty.pack(pady=5)

        ttk.Label(win, text="Category:", font=("Segoe UI", 12)).pack(pady=5)
        categories = self.manager.get_all_categories()
        category_names = [f"{c.id} - {c.name}" for c in categories]
        combo_cat = ttk.Combobox(win, values=category_names, state="readonly")
        combo_cat.pack(pady=5)

        def add():
            name = entry_name.get().strip()
            desc = entry_desc.get().strip()
            price = entry_price.get().strip()
            qty = entry_qty.get().strip()
            cat = combo_cat.get()

            if not (name and desc and price and qty and cat):
                messagebox.showerror("Error", "All fields are required.")
                return

            try:
                price = int(price)
                qty = int(qty)
            except ValueError:
                messagebox.showerror("Error", "Price and quantity must be integers.")
                return

            cat_id = int(cat.split(" - ")[0])

            new_product = Product(
                name=name,
                description=desc,
                price=price,
                quantity=qty,
                id_category=cat_id
            )
            new_product.insert_into_database()

            win.destroy()
            self.load_products()

        ttk.Button(win, text="Add", bootstyle=SUCCESS, command=add).pack(pady=10)

    def open_edit_window(self):
        """
        Open a window to edit the selected product.
        """
        if not self.selected_product_id:
            messagebox.showerror("Error", "Select a product first.")
            return

        product = self.manager.get_product_by_id(self.selected_product_id)

        win = ttk.Toplevel(self.root)
        win.title("Edit Product")

        # Inputs
        ttk.Label(win, text="Name:", font=("Segoe UI", 12)).pack(pady=5)
        entry_name = ttk.Entry(win)
        entry_name.insert(0, product.name)
        entry_name.pack(pady=5)

        ttk.Label(win, text="Description:", font=("Segoe UI", 12)).pack(pady=5)
        entry_desc = ttk.Entry(win)
        entry_desc.insert(0, product.description)
        entry_desc.pack(pady=5)

        ttk.Label(win, text="Price:", font=("Segoe UI", 12)).pack(pady=5)
        entry_price = ttk.Entry(win)
        entry_price.insert(0, product.price)
        entry_price.pack(pady=5)

        ttk.Label(win, text="Quantity:", font=("Segoe UI", 12)).pack(pady=5)
        entry_qty = ttk.Entry(win)
        entry_qty.insert(0, product.quantity)
        entry_qty.pack(pady=5)

        ttk.Label(win, text="Category:", font=("Segoe UI", 12)).pack(pady=5)
        categories = self.manager.get_all_categories()
        category_names = [f"{c.id} - {c.name}" for c in categories]
        combo_cat = ttk.Combobox(win, values=category_names, state="readonly")
        combo_cat.set(f"{product.id_category} - {self.manager.get_category_by_id(product.id_category).name}")
        combo_cat.pack(pady=5)

        def save():
            name = entry_name.get().strip()
            desc = entry_desc.get().strip()
            price = entry_price.get().strip()
            qty = entry_qty.get().strip()
            cat = combo_cat.get()

            if not (name and desc and price and qty and cat):
                messagebox.showerror("Error", "All fields are required.")
                return

            try:
                price = int(price)
                qty = int(qty)
            except ValueError:
                messagebox.showerror("Error", "Price and quantity must be integers.")
                return

            cat_id = int(cat.split(" - ")[0])

            product.name = name
            product.description = desc
            product.price = price
            product.quantity = qty
            product.id_category = cat_id

            product.update_name_in_database()
            product.update_description_in_database()
            product.update_price_in_database()
            product.update_quantity_in_database()
            product.update_category_in_database()

            win.destroy()
            self.load_products()

        ttk.Button(win, text="Save", bootstyle=SUCCESS, command=save).pack(pady=10)

    def delete_product(self):
        """
        Delete the selected product after confirmation.
        """
        if not self.selected_product_id:
            messagebox.showerror("Error", "Select a product first.")
            return

        confirm = messagebox.askyesno(
            "Confirm deletion",
            "Are you sure you want to delete this product?"
        )

        if not confirm:
            return

        product = self.manager.get_product_by_id(self.selected_product_id)
        product.delete_from_database()

        self.load_products()