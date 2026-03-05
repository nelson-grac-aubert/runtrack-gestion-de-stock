from scripts.logic.sql_utilities import access_database, close_everything_properly, point_cursor

class Product:
    """
    Represents a product stored in the database.
    """

    def __init__(self, name, description, price, quantity, id_category):
        """
        Initialize a Product instance.

        :param name: Product name.
        :type name: str
        :param description: Product description.
        :type description: str
        :param price: Product price.
        :type price: int
        :param quantity: Available stock quantity.
        :type quantity: int
        :param id_category: ID of the category the product belongs to.
        :type id_category: int

        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.id_category = id_category
        
        self.insert_into_database()

    def insert_into_database(self):
        """
        Insert the product into the database and store the generated ID.
        """
        database = access_database("store")
        cursor = point_cursor(database)  # must be a normal cursor, not dictionary=True

        query = """
            INSERT INTO product (name, description, price, quantity, id_category)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            self.name,
            self.description,
            self.price,
            self.quantity,
            self.id_category
        )

        cursor.execute(query, values)
        database.commit()

        # Retrieve auto-incremented ID
        self.id = cursor.lastrowid

        if self.id is None:
            raise RuntimeError("Failed to retrieve auto-incremented ID. Check cursor type and DB schema.")

        close_everything_properly(cursor, database)


    def delete_from_database(self):
        """
        Delete the product from the database using its ID.

        :return: None
        """
        if not hasattr(self, "id") or self.id is None:
            raise ValueError("Cannot delete a product without a valid ID.")

        database = access_database("store")
        cursor = point_cursor(database)

        query = "DELETE FROM product WHERE id = %s"
        values = (self.id,)

        cursor.execute(query, values)
        database.commit()

        close_everything_properly(cursor, database)

    # Modify the product in the database

    def _update_field(self, field_name, value):
        """
        Internal helper to update a single field in the database.

        :param field_name: Name of the column to update.
        :type field_name: str
        :param value: New value to store in the column.
        :type value: Any
        :return: None
        """
        if not hasattr(self, "id") or self.id is None:
            raise ValueError("Cannot update a product without a valid ID.")

        database = access_database("store")
        cursor = point_cursor(database)

        query = f"UPDATE product SET {field_name} = %s WHERE id = %s"
        values = (value, self.id)

        cursor.execute(query, values)
        database.commit()

        close_everything_properly(cursor, database)

    def update_name_in_database(self):
        """
        Update the product name.
        """
        self._update_field("name", self.name)


    def update_description_in_database(self):
        """
        Update the product description.
        """
        self._update_field("description", self.description)


    def update_price_in_database(self):
        """
        Update the product price.
        """
        self._update_field("price", self.price)


    def update_quantity_in_database(self):
        """
        Update the product quantity.
        """
        self._update_field("quantity", self.quantity)


    def update_category_in_database(self):
        """
        Update the product category ID.
        """
        self._update_field("id_category", self.id_category)