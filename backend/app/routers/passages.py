from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.database import get_db
from app.models.models import Passage
from app.schemas.passage import PassageOut

router = APIRouter()


@router.get("/passages", response_model=list[PassageOut])
async def get_passages(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Passage))
    return result.scalars().all()


@router.get("/passages/{passage_id}", response_model=PassageOut)
async def get_passage(passage_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Passage).where(Passage.id == passage_id)
    )
    passage = result.scalar_one_or_none()
    if not passage:
        raise HTTPException(status_code=404, detail="Passage not found")
    return passage