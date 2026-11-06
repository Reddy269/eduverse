from catalog.adapters.storages.category_storage import CategoryStorage
from catalog.interactors.exceptions import InvalidCategoryException, IncompleteCategoryException, TooManyCategoriesException, TooManySubCategoriesException

class CategoryRules:
    def __init__(self,
                 category_storage: CategoryStorage,):
        self.category_storage = category_storage

    def __call__(self,category) -> bool:

        parent_categories = {}
        parent_count = 2

        for category_id in category:
            if not self.category_storage.is_valid_category(category_id):
                raise InvalidCategoryException(category_id)

            parent_id = self.category_storage.get_parent_id(category_id)
            if parent_id is None:
                raise IncompleteCategoryException(category_id)
            if parent_id not in parent_categories:
                if parent_count == 0:
                    raise TooManyCategoriesException
            else:
                parent_categories[parent_id] = parent_categories.get(parent_id, 0) + 1
                if parent_categories[parent_id] > 4:
                    raise TooManySubCategoriesException

        return True


