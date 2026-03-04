from scripts.logic.sql_utilities import access_database, point_cursor, close_everything_properly

class Category:
    """
    Represents a product category stored in the database.
    """

    def __init__(self, name, id=None):
        """
        Initialize a Category instance.

        :param name: Category name.
        :type name: str
        :param id: Category ID (auto-incremented by the database).
        :type id: int or None
        """
        self.name = name
        self.id = id


    def insert_into_database(self):
        """
        Insert the category into the database and store the generated ID.

        :return: None
        """
        database = access_database("store")
        cursor = point_cursor(database)

        query = "INSERT INTO category (name) VALUES (%s)"
        values = (self.name,)

        cursor.execute(query, values)
        database.commit()

        self.id = cursor.lastrowid

        close_everything_properly(cursor, database)
    
    def delete_from_database(self):
        """
        Delete the category from the database using its ID.

        :return: None
        """
        if self.id is None:
            raise ValueError("Cannot delete a category without a valid ID.")

        database = access_database("store")
        cursor = point_cursor(database)

        query = "DELETE FROM category WHERE id = %s"
        values = (self.id,)

        cursor.execute(query, values)
        database.commit()

        close_everything_properly(cursor, database)


    def _update_field(self, field_name, value):
        """
        Internal helper to update a single field in the database.

        :param field_name: Name of the column to update.
        :type field_name: str
        :param value: New value to store in the column.
        :type value: Any
        :return: None
        """
        if self.id is None:
            raise ValueError("Cannot update a category without a valid ID.")

        database = access_database("store")
        cursor = point_cursor(database)

        query = f"UPDATE category SET {field_name} = %s WHERE id = %s"
        values = (value, self.id)

        cursor.execute(query, values)
        database.commit()

        close_everything_properly(cursor, database)

    def update_name_in_database(self):
        """
        Update the category name.
        """
        self._update_field("name", self.name)
