import time
from sqlmodel import SQLModel, Field, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine

class BaseModel(SQLModel):
    id: int = Field(primary_key=True, description="主键ID")
    created_at: int = Field(default_factory=lambda: int(time.time()), description="创建时间")
    created_by: int = Field(default=0, description="创建者ID")
    updated_at: int = Field(default=0, description="更新时间")
    updated_by: int = Field(default=0, description="更新者ID")
    deleted_at: int = Field(default=0, description="删除时间")
    deleted_by: int = Field(default=0, description="删除者ID")
    is_deleted: bool = Field(default=False, description="是否已删除")

class User(BaseModel, table=True):
    name: str = Field(description="用户名")
    email: str = Field(description="用户邮箱")

class Product(BaseModel, table=True):
    name: str = Field(description="产品名称")
    price: float = Field(description="产品价格")

class Purchase(BaseModel, table=True):
    user_id: int = Field(description="用户ID")
    product_id: int = Field(description="产品ID")
    purchase_date: int = Field(default_factory=lambda: int(time.time()), description="购买日期")

class Return(BaseModel, table=True):
    purchase_id: int = Field(description="购买记录ID")
    return_date: int = Field(default_factory=lambda: int(time.time()), description="退货日期")
    reason: str = Field(description="退货原因")


# 创建 SQLite 数据库引擎
sqlite_file_name = "database.db"
sqlite_url = f"sqlite+aiosqlite:///{sqlite_file_name}"
engine = create_async_engine(sqlite_url, echo=True)

# 创建所有表
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

# 在启动时创建表
if __name__ == "__main__":
    import asyncio
    asyncio.run(create_db_and_tables())
