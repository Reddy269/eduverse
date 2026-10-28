from typing import Optional , List
from dataclasses import dataclass

@dataclass
class StudentRegistredDTO:
    id: int
    name: str
    email: str