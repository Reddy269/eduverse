"""
Output Verification Script
Verifies outputs from all storage modules
Usage: python verify_outputs.py
"""
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from storage.models import Address, Customer, Product , ProductSeller, Seller , Category , ProductCategory

from storage.storages import CustomerStorage

def reset_db():
    """Reset database"""
    print("\n" + "="*60)
    print("📦 MODULE 1: CUSTOMER & ADDRESS MANAGEMENT HAS BEEN RESET")
    print("=" * 60)

    Address.objects.all().delete()
    Customer.objects.all().delete()

    print("✅ Old data cleared\n")


def verify_customer_module():
    """Verify Module 1: Customer & Address Management"""
    print("\n" + "="*60)
    print("📦 MODULE 1: CUSTOMER & ADDRESS MANAGEMENT")
    print("="*60)

    # 1.1 Register Customer
    print("\n📋 Verifying 1.1: Register Customer")
    customer_data = {
        'full_name': 'Rajesh Kumar',
        'date_of_birth': '1990-05-15',
        'gender': 'Male',
        'email': 'rajesh.kumar@example.com',
        'phone_number': '+919876543210'
    }
    customer = CustomerStorage.register_customer(customer_data)
    print(f"✅ Customer created: {customer.full_name} (ID: {customer.id})")

    # 1.2 Add Addresses
    print("\n📋 Verifying 1.2: Add Addresses")
    addresses_data = [
        {
            'house_number': '12A',
            'street_address': 'MG Road',
            'city': 'Hyderabad',
            'district': 'Hyderabad',
            'state': 'Telangana',
            'pincode': 500001,
            'landmark': 'Near Metro Station',
            'category': 'HOME'
        }
    ]
    a = CustomerStorage.add_addresses(customer.id, addresses_data)
    print(f"✅ Created {len(addresses_data)} address(es) " )


    # 1.3 get customer profile
    print("\n📋 Verifying 1.3: Get customer's profile")
    print("\n")
    print(CustomerStorage.get_customer_profile(customer.id))
    print("\n")
    print(f"✅succesfully returned the customer's profile ")

    #1.4 set primary address
    print("\n📋 Verifying 1.4: Set customer's address as primary")
    CustomerStorage.set_primary_address(customer.id,a[0])
    print("\n")
    print(f"✅succesfully set primary address ")

    #1.5 get primary address
    print("\n📋 Verifying 1.5: Get customer's profile")
    print("\n")
    print(CustomerStorage.get_primary_address(customer.id))
    print("\n")
    print(f"✅returned customer's primary address ")




def verify_product_module():
    """Verify Module 2: Products & Sellers"""
    print("\n" + "="*60)
    print("📦 MODULE 2: PRODUCTS & SELLERS")
    print("="*60)

    # Add verifications for product module
    pass


def verify_order_module():
    """Verify Module 3: Orders & Payments"""
    print("\n" + "="*60)
    print("📦 MODULE 3: ORDERS & PAYMENTS")
    print("="*60)

    # Add verifications for order module
    pass


# Add verification functions for other modules...


def main():

    reset_db()

    """Run all module verifications"""
    print("\n" + "🚀 STARTING OUTPUT VERIFICATION")
    print("Organized by Storage Modules\n")

    try:
        # Verify each module
        customer = verify_customer_module()
        # verify_product_module()
        # verify_order_module()
        # ... other modules

        print("\n" + "="*60)
        print("✅ VERIFICATION COMPLETED!")
        print("="*60)

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
