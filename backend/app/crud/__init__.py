from .base import BaseCrud
from .create import Create
from .delete import Delete
from .read import Read
from .update import Update

base = BaseCrud()
create = Create()
delete = Delete()
read = Read()
update = Update()

__all__ = [attr for attr in locals().keys() if not attr.startswith("_")]
