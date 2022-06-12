from pymongo import MongoClient 
from __future__ import annotations
from typing import TYPE_CHECKING
from config import MONGODB_URL
from errors import RedirectNotFound

if TYPE_CHECKING:
    from typing_extensions import Self

class Database:
    def __init__(self: Self, client: str = MONGODB_URL):
        self.client: MongoClient = MongoClient(MONGODB_URL)
        self.domain_client = self.client.domain.list
    
    def get_redirect_destination(self: Self, redirect: str):
        result: dict[str, str] = self.domain_client.find_one({"_id": redirect})
        if result == None:
            raise RedirectNotFound(redirect_name=redirect)
        return result['destination']
