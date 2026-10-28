from typing import Optional

from interactors.ports.storage_interfaces import (
    AdminStorageInterface,
)
from interactors.ports.storage_interfaces import AdminDTO
from accounts.models import Admin


class AdminStorage(AdminStorageInterface):

    def get_admin(self, user_id: int) -> Optional[AdminDTO]:
        admin = Admin.objects.filter(user_id=user_id).first()
        if admin is None:
            return None
        return AdminDTO(user_id=admin.user_id, name=admin.name, email=admin.email)

    def is_admin(self, user_id: int) -> bool:
        return Admin.objects.filter(user_id=user_id).exists()
