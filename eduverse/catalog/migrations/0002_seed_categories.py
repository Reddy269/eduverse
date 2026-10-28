from django.db import migrations
from catalog.models import Category

CATEGORIES = {
    "Development": [
        "Web Development", "Mobile Development", "Programming Languages",
        "Data Science", "Game Development", "Databases", "Software Testing",
        "Software Engineering", "DevOps & Tools", "No-Code Development",
    ],
    "Business": [
        "Entrepreneurship", "Management", "Sales", "Project Management",
        "Business Strategy", "Business Analytics", "Human Resources", "E-Commerce",
    ],
    "Finance & Accounting": [
        "Accounting & Bookkeeping", "Investing & Trading", "Financial Modeling",
        "Taxes", "Cryptocurrency & Blockchain", "Economics", "Money Management",
        "Finance Exam Prep",
    ],
    "IT & Software": [
        "IT Certifications", "Network & Security", "Cloud Computing",
        "Operating Systems & Servers", "Hardware",
    ],
    "Office Productivity": [
        "Microsoft Excel", "Microsoft Word & PowerPoint", "Google Workspace",
        "Apple Productivity", "SAP", "Oracle",
    ],
    "Personal Development": [
        "Productivity", "Leadership", "Career Development", "Communication Skills",
        "Confidence & Motivation", "Stress Management", "Memory & Study Skills",
        "Creativity",
    ],
    "Design": [
        "Web Design", "Graphic Design", "UI/UX Design", "3D & Animation",
        "Game Design", "Fashion Design", "Interior Design", "Architectural Design",
    ],
    "Marketing": [
        "Digital Marketing", "SEO", "Social Media Marketing", "Branding",
        "Content Marketing", "Paid Advertising", "Marketing Analytics",
        "Public Relations",
    ],
    "Health & Fitness": [
        "Fitness", "Nutrition & Diet", "Yoga", "Meditation", "Mental Health",
        "Sports", "Martial Arts", "First Aid & Safety",
    ],
}


def seed_categories(apps, schema_editor):
    for parent_name, children in CATEGORIES.items():
        parent, _ = Category.objects.get_or_create(name=parent_name, parent=None)
        for child_name in children:
            Category.objects.get_or_create(name=child_name, parent=parent)


def unseed_categories(apps, schema_editor):
    # Children first, because on_delete=PROTECT blocks deleting a parent that has children
    Category.objects.filter(parent__name__in=CATEGORIES, parent__parent=None).delete()
    Category.objects.filter(name__in=CATEGORIES, parent=None).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),  # use your latest migration's name
    ]
    operations = [
        migrations.RunPython(seed_categories, unseed_categories),
    ]