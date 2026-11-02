from catalog.interactors.ports import DraftStorageInterface
from catalog.models import Category, Course, CourseCategory
from catalog.interactors.dtos import RequestCreateCourseDTO, RequestUpdateCourseDTO


class DraftStorage(DraftStorageInterface):
    def save(self ,request:RequestCreateCourseDTO):
        course = Course.objects.create(
            title = request.name,
            status = "DRA",
            overview = request.Overview,
            duration = request.EstimatedDurationInHours,
                                       )

        cat_list = []
        for category in request.categories:
            for part in category.split(">"):
                cat_list.append(part.strip())
            for i in range(2, len(cat_list)):
                parent = Category.objects.get(name=cat_list[i-1])
                if Category.objects.filter(parent = parent,name = cat_list[i]).exists():
                    continue
                else:
                    Category.objects.create(name = cat_list[i],parent = parent)
        category = Category.objects.get(name = cat_list[-1])
        CourseCategory.objects.create(category = category, course = course)

    def update(self, request):
        pass







'''class RequestCreateCourseDTO:
    name : str
    categories : List[str]
    EstimatedDurationInHours: int
    Overview: str

    def __init__(self, name: str, categories: List[str], EstimatedDurationInHours: int, Overview: str):
        self.name = name
        for category in categories:
            if not isinstance(category, str):
                raise InvalidCategoryException("Category path is required")
            if not all(part.strip() for part in category.split(">")):
                raise InvalidCategoryException("Empty category path in {!r}".format(category))
        self.categories = categories
        self.EstimatedDurationInHours = EstimatedDurationInHours
        self.Overview = Overview
        
    class Course(models.Model):
    title = models.CharField(max_length=100)
    statues = models.CharField(max_length=3, choices=course_status, default="DRA")
    prerequisites = models.TextField(null=True,blank=True)
    overview = models.TextField()
    duration = models.IntegerField()
    price = models.IntegerField(null=True,blank=True)
    about_instructor = models.TextField(null=True,blank=True)
    listing_image_metadata = models.TextField(null=True,blank=True)
    preview_content_metadata = models.TextField(null=True,blank=True)
'''