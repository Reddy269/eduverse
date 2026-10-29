from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List, Union, BinaryIO

from catalog.storages.category_storage import CategoryStorage
from .exceptions import InvalidCategoryException

class LessonType(str, Enum):
    VIDEO = "video"
    ARTICLE = "article"

class ItemType(str, Enum):
    LESSON = "lesson"
    QUIZ = "quiz"
class QuestionType(str, Enum):
    MCQ = "MCQ"
    CODING = "CODING"

class Scope(str, Enum):
    LESSON = "lesson"
    MODULE = "module"
    FINAL = "final"

@dataclass
class LessonDTO:
    name: str
    description: str
    LessonType: LessonType
    filename: str

@dataclass
class QuestionDTO:
    QuestionType: QuestionType
    QuestionContent: str
    Solution: str
    Scope: Scope


@dataclass()
class ExamDTO:
    Questions : List[QuestionDTO]


@dataclass
class CourseListingDTO:
    code: str
    name: str
    duration: int
    instructorId: int
    ListingImageMetaData : str
    price: int
    # example : Category>Sub-Category>Sub-Sub-Category
    CategoryHierarchy : str


@dataclass
class PathItemDTO:
    ItemType: ItemType
    ItemDTO: Union[LessonDTO,ExamDTO]
    Topic: str
    Subtopic: str


@dataclass
class RequestSaveCourseDTO:
    CourseListingDTO: CourseListingDTO
    LearningPath : List[PathItemDTO] = field(default_factory=list)
    ModuleExam : List[ExamDTO] = field(default_factory=list)


@dataclass
class RequestAssignCategoryDTO:
    parent: str
    path: tuple[str, ...]

    def __init__(self, category: str):
        if not isinstance(category, str) or not category.strip():
            raise InvalidCategoryException("Category path is required")

        segments = tuple(s.strip() for s in category.split(">"))

        if any(s == "" for s in segments):
            raise InvalidCategoryException(f"Empty segment in {category!r}")

        self.parent = segments[0]
        self.path = segments[1:]


@dataclass
class RequestCreateCourseDTO:
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

@dataclass
class RequestUpdateCourseDTO:
    name: Optional[str]
    categories: Optional[List[str]]
    prerequisites: Optional[str]
    about: Optional[str]
    lessons: Optional[List[LessonDTO]]
    listing_image_filename: Optional[str]
    preview_content_filename: Optional[str]



@dataclass
class RequestAddContentDTO:
    content_type: LessonType | str
    content: BinaryIO
    filename: str

    def __post_init__(self):
        self.content_type = LessonType(self.content_type)



@dataclass
class RequestDeleteContentDTO:
    content_type: LessonType
    filename: str














