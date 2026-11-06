import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eduverse.settings")
django.setup()


from catalog.interactors.dtos import RequestDraftCourseDTO
from catalog.interactors.core.course.create_course_draft_interactor import CreatCourseDraftInteractor, CategoryRules
from catalog.adapters.storages.course_storage import CourseStorage
from catalog.adapters.storages.category_storage import CategoryStorage

course_storage = CourseStorage()
category_storage = CategoryStorage()
category_rules = CategoryRules(category_storage)

interactor = CreatCourseDraftInteractor(course_storage, category_storage,category_rules)

request = RequestDraftCourseDTO(title="Python 207",  category=[11,12], overview="become a python expert")
print(interactor.save_draft(request))