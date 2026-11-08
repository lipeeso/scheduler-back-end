from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import exists, select
from api_scheduler.models.users import User
from api_scheduler.schemas.users import UserPublicSchema, UserSchema, UserUpdateSchema, UserListPublicSchema
from api_scheduler.core.database import get_session
from api_scheduler.core.security import get_password_hash


router = APIRouter()

@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserPublicSchema,
    summary="Create a new user",
)
async def create_user(user: UserSchema, session: AsyncSession = Depends(get_session)):
    user_exists = await session.scalar(
        select(exists().where(User.username == user.username))
    )

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    email_exists = await session.scalar(
        select(exists().where(User.email == user.email))
    )

    if email_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password)
    )

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return new_user


@router.get(
    path="/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserPublicSchema,
    summary="Get user by ID"
)
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


@router.put(
    path="/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserPublicSchema,
    summary="Update user by ID"
)
async def update_user(user_id: int, user_update: UserUpdateSchema, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    update_data = user_update.model_dump(exclude_unset=True)

    if 'username' in update_data and update_data['username'] != user.username:
        username_exists = await session.scalar(
            select(exists().where((User.username == update_data['username']) & (User.id != user_id)))
        )

        if username_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )

    await session.commit()
    await session.refresh(user)

    return update_data



@router.delete(
    path="/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user by ID"
)
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    await session.delete(user)
    await session.commit()  
