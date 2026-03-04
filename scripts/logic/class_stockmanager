from scripts.logic.sql_utilities import access_database, point_cursor, close_everything_properly
from scripts.logic.class_product import Product
from scripts.logic.class_category import Category


class StockManager:
    """
    Provides high-level operations to retrieve and manage products and categories.
    """

    def __init__(self):
        pass


    def get_all_products(self):
        """
        Retrieve all products from the database and return them as Product objects.

        :return: List of Product instances.
        :rtype: list[Product]
        """
        database = access_database("store")
        cursor = point_cursor(database)

        query = (
            "SELECT id, name, description, price, quantity, id_category "
            "FROM product"
        )
        cursor.execute(query)
        rows = cursor.fetchall()

        close_everything_properly(cursor, database)

        products = []
        for row in rows:
            product_id, name, description, price, quantity, id_category = row
            products.append(
                Product(
                    name=name,
                    description=description,
                    price=price,
                    quantity=quantity,
                    id_category=id_category,
                    id=product_id
                )
            )

        return products

    def get_all_categories(self):
        """
        Retrieve all categories from the database and return them as Category objects.

        :return: List of Category instances.
        :rtype: list[Category]
        """
        database = access_database("store")
        cursor = point_cursor(database)

        query = "SELECT id, name FROM category"
        cursor.execute(query)
        rows = cursor.fetchall()

        close_everything_properly(cursor, database)

        categories = []
        for row in rows:
            category_id, name = row
            categories.append(Category(name=name, id=category_id))

        return categories

    def get_product_by_id(self, product_id):
        """
        Retrieve a single product by its ID.

        :param product_id: ID of the product.
        :return: Product instance or None.
        """
        database = access_database("store")
        cursor = point_cursor(database)

        query = (
            "SELECT id, name, description, price, quantity, id_category "
            "FROM product WHERE id = %s"
        )
        cursor.execute(query, (product_id,))
        row = cursor.fetchone()

        close_everything_properly(cursor, database)

        if row is None:
            return None

        product_id, name, description, price, quantity, id_category = row
        return Product(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            id_category=id_category,
            id=product_id
        )

    def get_category_by_id(self, category_id):
        """
        Retrieve a single category by its ID.

        :param category_id: ID of the category.
        :return: Category instance or None.
        """
        database = access_database("store")
        cursor = point_cursor(database)

        query = "SELECT id, name FROM category WHERE id = %s"
        cursor.execute(query, (category_id,))
        row = cursor.fetchone()

        close_everything_properly(cursor, database)

        if row is None:
            return None

        category_id, name = row
        return Category(name=name, id=category_id)

    def get_products_by_category(self, id_category):
        """
        Retrieve all products belonging to a specific category.

        :param id_category: Category ID.
        :return: List of Product instances.
        """
        database = access_database("store")
        cursor = point_cursor(database)

        query = (
            "SELECT id, name, description, price, quantity, id_category "
            "FROM product WHERE id_category = %s"
        )
        cursor.execute(query, (id_category,))
        rows = cursor.fetchall()

        close_everything_properly(cursor, database)

        products = []
        for row in rows:
            product_id, name, description, price, quantity, id_category = row
            products.append(
                Product(
                    name=name,
                    description=description,
                    price=price,
                    quantity=quantity,
                    id_category=id_category,
                    id=product_id
                )
            )

        return products

    def search_products(self, keyword):
        """
        Search products by keyword in name or description.

        :param keyword: Search keyword.
        :return: List of Product instances.
        """
        database = access_database("store")
        cursor = point_cursor(database)

        like_pattern = f"%{keyword}%"

        query = (
            "SELECT id, name, description, price, quantity, id_category "
            "FROM product "
            "WHERE name LIKE %s OR description LIKE %s"
        )
        cursor.execute(query, (like_pattern, like_pattern))
        rows = cursor.fetchall()

        close_everything_properly(cursor, database)

        products = []
        for row in rows:
            product_id, name, description, price, quantity, id_category = row
            products.append(
                Product(
                    name=name,
                    description=description,
                    price=price,
                    quantity=quantity,
                    id_category=id_category,
                    id=product_id
                )
            )

        return products
