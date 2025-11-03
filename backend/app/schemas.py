from pydantic import BaseModel, Field, validator
from typing import Optional, Literal, List

# Product I/O
class ProductCreate(BaseModel):
    seller_id: int = Field(..., ge=1)
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    category: Optional[str] = Field(None, max_length=50)
    image_url: Optional[str] = None
    status: Literal["available","sold","under_review"] = "available"

    @validator("name")
    def _strip_name(cls, v):
        v = v.strip()
        if not v: raise ValueError("name cannot be empty")
        return v

    @validator("image_url")
    def _clean_url(cls, v):
        if v is None: return None
        v = v.strip()
        if not v: return None
        if len(v) > 1024: raise ValueError("image_url too long (>1024)")
        if not (v.startswith("http://") or v.startswith("https://")):
            raise ValueError("image_url must start with http:// or https://")
        return v

class ProductOut(BaseModel):
    product_id: int
    seller_id: int
    name: str
    description: Optional[str] = None
    price: float
    category: Optional[str] = None
    image_url: Optional[str] = None
    status: Literal["available","sold","under_review"]

class ProductListOut(BaseModel):
    total: int
    items: List[ProductOut]

# Order I/O
class OrderCreate(BaseModel):
    buyer_id: int
    product_id: int

class OrderOut(BaseModel):
    order_id: int
    buyer_id: int
    product_id: int
    order_status: Literal["pending","paid","shipped","completed","cancelled"]
    # 簡要商品資訊
    product_name: Optional[str] = None
    product_price: Optional[float] = None
    product_image: Optional[str] = None

class OrderListOut(BaseModel):
    total: int
    items: List[OrderOut]
