


# exceptions during creating new course draft
class InvalidInputException(Exception):
    """Base class for all input exceptions"""
    message = "Invalid input"

    def __init__(self, message: str | None = None) -> None:
        self.message = message or self.message
        super().__init__(self.message)          # makes str(e) return the message


class InvalidCategoryException(InvalidInputException):
    message = "The draft input has an invalid category"

    def __init__(self, category_id: int) -> None:
        self.category_id = category_id
        super().__init__(f"{self.message}: category_id: {category_id}")

class EmptyTitleException(InvalidInputException):
    message = 'please enter a valid title'

class EmptyCategoryException(InvalidInputException):
    message = 'enter atleast one valid category'

class IncompleteCategoryException(InvalidInputException):
    message = 'please enter complete category path'

    def __init__(self, category_id: int) -> None:
        self.category_id = category_id
        super().__init__(f"{self.message}: category_id: {category_id}")

class TooManyCategoriesException(InvalidInputException):
    message = 'sub_categories can only belong to upto 2 categories'

class TooManySubCategoriesException(InvalidInputException):
    message = 'there can only be upto 4 sub-categories'

class InvalidCourseException(InvalidInputException):
    message = 'Please enter a valid course'
    def __init__(self, x) -> None:
        if isinstance(x, str):
            course_title = x
            super().__init__(f"{self.message}: course_title: {course_title}")
        elif isinstance(x, int):
            course_id = x
            super().__init__(f"{self.message}: course_id: {course_id}")

class CourseNotEditableException(InvalidInputException):
    pass

class InvalidLessonTypeException(InvalidInputException):
    message = 'Please enter a valid lesson type'

    def __init__(self, lesson_type: str) -> None:
        self.lesson_type = lesson_type
        super().__init__(f"{self.message}: lesson_type: { lesson_type}")