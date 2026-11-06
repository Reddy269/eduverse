from typing import Optional, List

from catalog.interactors.ports.storage_interfaces import CategoryStorageInterface
from catalog.interactors.dtos import RequestDraftCourseDTO
from catalog.models import Course, Category, CourseCategory

class CategoryStorage(CategoryStorageInterface):
    def assign_category_to_course(self, category_id: int, course_id : int) -> None:
        course = Course.objects.get(id=course_id)
        category = Category.objects.get(id=category_id)
        CourseCategory.objects.create(course=course, category=category)

    def is_valid_category(self, category_id: int) -> bool:
        if Category.objects.filter(id=category_id).exists():
            return True
        return False

    def has_parent_category(self, category_id: int) -> bool:
        pass

    def get_parent_id(self, category_id: int) -> Optional[int]:
        return Category.objects.get(id=category_id).parent_id

    def get_category_tree(self):
        pass

    def remove_category_from_course(self, category_id: int, course_id: int) -> None:
        pass

    def get_categories_of_course(self, category_id: int) -> List[Category]:
        pass




'''
class CategoryStorageInterface(ABC):
    @abstractmethod
    def is_valid_category(self, category_id: int) -> bool:
        pass

    @abstractmethod
    def has_parent_category(self, category_id: int) -> bool:
        pass

    @abstractmethod
    def get_parent_id(self, category_id: int) -> Optional[int]:
        pass

    @abstractmethod
    def get_category_tree(self):
        pass

    @abstractmethod
    def assign_category_to_course(self, category_id: int, course_id: int):
        pass

    @abstractmethod
    def remove_category_from_course(self,category_id: int,course_id: int):
        pass

    @abstractmethod
    def get_categories_of_course(self,category_id: int):
        pass

'''