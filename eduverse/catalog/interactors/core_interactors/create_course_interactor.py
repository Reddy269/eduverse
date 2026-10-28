from catalog.interactors.dtos import RequestCreateCourseDTO,RequestAssignCategoryDTO
from catalog.interactors.ports import DraftStorageInterface
from catalog.interactors.ports import CategoryStorageInterface
from catalog.interactors.exceptions import InvalidCategoryException


class CreatCourseInteractor:
    def __init__(self,
                 draft_storage: DraftStorageInterface,
                 category_storage: CategoryStorageInterface,
                 ):
        self.draft_storage = draft_storage
        self.category_storage = category_storage
    def save(self,request: RequestCreateCourseDTO):
        # rules for category:check if first parent(has parent = null) is part of main division
        if not self.category_storage.is_root_parent(request):
            raise InvalidCategoryException
        self.draft_storage.save(request)










