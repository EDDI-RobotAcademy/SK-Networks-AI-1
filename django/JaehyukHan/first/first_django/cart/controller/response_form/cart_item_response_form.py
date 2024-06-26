from typing import List

from pydantic import BaseModel


class CartItemResponseForm(BaseModel):
    cartList: List[List]
