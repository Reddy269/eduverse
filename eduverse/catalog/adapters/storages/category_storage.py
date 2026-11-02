from catalog.interactors.ports import CategoryStorageInterface
from dtos import RequestCreateCourseDTO
from catalog.models import Category
from exceptions import InvalidCategoryException


class CategoryStorage(CategoryStorageInterface):
    def is_root_parent(self,request: RequestCreateCourseDTO) -> bool:
        for category in request.categories:
            category = category.split(">")
            parent = category[0]
            if not Category.objects.filter(name = parent,parent__isnull=True).exists():
                return False
        return True