"""
Product & Seller Storage
Handles all product catalog and seller-related operations
Module 2: Questions 2.1 to 2.14
"""
from django.db.models import Q, Avg, Count
from decimal import Decimal

from django.forms.models import model_to_dict

from ..models import Product, Seller, Category, ProductCategory, ProductSeller


class ProductStorage:
    """Storage class for Product and Seller operations"""

    @staticmethod
    def register_seller(seller_data):
        seller = Seller.objects.create(
            name = seller_data["name"],
            contact_mail = seller_data["contact_email"],
            tax_gst_id = seller_data["tax_gst_id"],
            business_type = seller_data["business_type"],
            average_rating = seller_data["average_rating"],
            number_of_ratings = seller_data["number_of_ratings"],
        )
        return seller

    @staticmethod
    def get_seller_profile(seller_id):

        seller = Seller.objects.get(pk = seller_id)
        return model_to_dict(seller)


    @staticmethod
    def update_seller(seller_id, updates):

        seller = Seller.objects.get(pk=seller_id)

        for field_name, value in updates.items():
            setattr(seller, field_name, value)

        seller.save()
        return seller


    @staticmethod
    def create_product(product_data):

        product = Product.objects.create(
            name = product_data["name"],
            description = product_data["description"],
            weight = product_data["weight"],
            dimension = product_data["dimension"],
            avg_rating = product_data["avg_rating"],
            total_no_of_reviews = product_data["total_no_of_reviews"],
        )
        return product

    @staticmethod
    def create_category(category_data):

        parent_category = Category.objects.get(pk = category_data["parent_category"])

        category = Category.objects.create(
            category_name = category_data["category_name"],
            parent_category = parent_category,
            path = category_data["category_hierarchy"],
        )

        return category



    @staticmethod
    def get_product_data(product_id):
        product = Product.objects.get(pk = product_id)

        return model_to_dict(product)

    @staticmethod
    def get_products(category_id):

        category = Category.objects.get(pk = category_id)
        products_category = Product.objects.filter(ProductCategory__category = category)

        return products_category.values('name')

    @staticmethod
    def list_sellers_product(listing_data):
        product = Product.objects.get(pk = listing_data['product_id'])
        seller = Seller.objects.get(pk = listing_data['seller_id'])

        listing = ProductSeller.objects.create(
            product = product,
            seller = seller,
            price = listing_data['price'],
            sku = listing_data['sku'],
            quantity = listing_data['quantity'],
        )

        return listing.values()

    @staticmethod
    def fetch_products_sellers(product_id):
        product = Product.objects.get(pk = product_id)
        sellers = Seller.objects.filter(ProductSeller__product = product)

        return sellers.values('name','contact_email','tax_gst_id','business_type')

    @staticmethod
    def get_products_budget(budget_data):
        category = Category.objects.get(pk = budget_data["category_id"])
        products = Product.objects.filter(ProductCategory__category = category).filter(ProductSeller__price__gte= budget_data["min_price"], ProductSeller__price__lte = budget_data["max_price"])
        return products.values()






