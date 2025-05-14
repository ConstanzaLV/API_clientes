from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr = Field(...,
        description="Correo electrónico del usuario",
        example="usuario@dominio.com"
    )
    full_name: Optional[str] = Field(
        None,
        description="Nombre completo del usuario",
        max_length=100,
        example="Juan Pérez"
    )

class UserCreate(UserBase):
    password: str = Field(...,
        min_length=8,
        description="Contraseña con al menos 8 caracteres",
        example="securepassword@gmail.com"
    )

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = Field(
        None,
        description="Nuevo correo electrónico si se va a actualizar",
        example="nuevo@dominio.com"
    )
    full_name: Optional[str] = Field(
        None,
        description="Nuevo nombre completo si se va a actualizar",
        max_length=100,
        example="Juan A. Pérez"
    )
    password: Optional[str] = Field(
        None,
        min_length=8,
        description="Nueva contraseña si se va a actualizar",
        example="Nuevapass"
    )
