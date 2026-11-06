from catalog.interactors.ports.storage_interfaces import LessonStorageInterface
from dtos import RequestCreateLessonDTO
from catalog.models import Lesson

class LessonStorage(LessonStorageInterface):
    def create_lesson(self,request:RequestCreateLessonDTO):
        lesson_data = {
            "title": request.title,
            "lesson_type": request.lesson_type.value,  # store the enum's value, not the enum object
        }

        if request.description is not None:
            lesson_data["description"] = request.description

        lesson = Lesson.objects.create(**lesson_data)


    '''
    @dataclass
    class RequestCreateLessonDTO:
    title: str
    description: Optional[str]
    lesson_type: str

    def __post_init__(self):

        if self.title is None:
            raise InvalidInputException()

        try:
            self.lesson_type = LessonType(self.lesson_type)
        except ValueError:
            InvalidLessonTypeException(self.lesson_type)

    '''