"""
Customer & Address Storage
Handles all customer and address-related database operations
Module 1: Questions 1.1 to 1.10
"""
from unicodedata import category

from django.db.models import Q, Model
from ..models import Customer, Address


class CustomerStorage:
    """Storage class for Customer and Address operations"""

    @staticmethod
    def register_customer(customer_data):
        """
        1.1 Register a New Customer

        Args:
            customer_data (dict): Customer information

        Returns:
            Customer: Created customer object
        """
        customer = Customer.objects.create(
            full_name=customer_data['full_name'],
            date_of_birth=customer_data['date_of_birth'],
            gender=customer_data['gender'],
            email=customer_data['email'],
            phone_number=customer_data['phone_number']
        )
        return customer

    @staticmethod
    def add_addresses(customer_id, addresses_data):
        """
        1.2 Add Multiple Addresses for a Customer
        """
        customer = Customer.objects.get(id = customer_id)
        addresse_id = []
        for address_data in addresses_data:
            a = Address.objects.create(
                customer=customer,
                house_number = address_data['house_number'],
                street_address = address_data['street_address'],
                city = address_data['city'],
                district = address_data['district'],
                state = address_data['state'],
                pincode = address_data['pincode'],
                landmark = address_data['landmark'],
                category = address_data['category']
            )
            addresse_id.append(a.id)
        return addresse_id





    @staticmethod
    def get_customer_profile(customer_id):
        """
        1.3 Fetch Customer Profile with All Addresses
        """
        customer = Customer.objects.get(id = customer_id)
        a = {
            'full_name': customer.full_name,
            'date_of_birth': customer.date_of_birth,
            'gender': customer.gender,
            'email': customer.email,
            'phone_number': customer.phone_number,
        }
        obj = Address.objects.filter(customer = customer).first()
        if obj:
            b = {
                'house_number': obj.house_number,
                'street_address': obj.street_address,
                'city': obj.city,
                'district' : obj.district,
                'state': obj.state,
                'pincode': obj.pincode,
                'landmark': obj.landmark,
                'category': obj.category
            }
            return a | {'Address' : b }
        else:
            return a | {'Adresses' : 'empty'}  # Or any other fallback value

    @staticmethod
    def set_primary_address(customer_id, address_id):
        """
        1.4 Set Primary Address
        """
        customer = Customer.objects.get(id = customer_id)
        Address.objects.filter(customer = customer).filter(is_primary = True).update(is_primary = False)
        Address.objects.filter(id = address_id).update(is_primary = True)

    @staticmethod
    def get_primary_address(customer_id):
        """
        1.5 Fetch Primary Address for Checkout
        """
        customer = Customer.objects.get(id = customer_id)
        address = Address.objects.get(customer = customer, is_primary = True)
        return {
            'house_number': address.house_number,
            'street_address': address.street_address,
            'city': address.city,
            'district': address.district,
            'state': address.state,
            'pincode': address.pincode,
            'landmark': address.landmark
        }

    @staticmethod
    def update_customer(customer_id, updates):
        """
        1.6 Update Customer Details
        """
        customer = Customer.objects.get(id = customer_id)
        customer.full_name = updates['full_name']
        customer.date_of_birth = updates['date_of_birth']
        customer.email = updates['email']
        customer.gender = updates['gender']
        customer.phone_number = updates['phone_number']
        customer.save()

    @staticmethod
    def find_customers_by_city(city):
        """
        1.7 Find Customers by City
        """
        return Customer.objects.filter(Adress__city = city).values('full_name' , 'Adress__city')

        pass

    @staticmethod
    def find_customers_by_pincode(pincode):
        """
        1.8 Find Customers by Pincode
        """
        return Customer.objects.filter(pincode = pincode).values('full_name' , 'pincode')

    @staticmethod
    def update_address(address_id, updates):
        """
        1.9 Update Address Details
        """
        address = Address.objects.get(id = address_id)
        address.house_number = updates['house_number']
        address.street_address = updates['street_address']
        address.city = updates['city']
        address.district = updates['district']
        address.state = updates['state']
        address.pincode = updates['pincode']
        address.landmark = updates['landmark']
        address.is_primary = updates['is_primary']
        address.save()

    @staticmethod
    def delete_address(address_id, customer_id):
        """
        1.10 Delete an Address
        """
        address = Address.objects.filter(id = address_id).delete()


