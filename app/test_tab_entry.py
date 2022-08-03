from typing import List

from fastapi import APIRouter, HTTPException, Path

from app import crud
from models.test_tab import TestTabSchema, TestTabDB

router = APIRouter()

@router.post("/", response_model=TestTabDB, status_code=201)
async def create_entry(payload: TestTabSchema):
    entry_id = await crud.post(payload)
    response_obj = {
        "id": entry_id,
        "name": payload.name,
        "descr": payload.descr
    }
    return response_obj

@router.get("/{id}/", response_model=TestTabDB)
async def read_entry(id: int = Path(..., gt=0)):
    test_entry = await crud.get(id)
    if not test_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return test_entry

@router.get("/", response_model=List[TestTabDB])
async def read_all_entry():
    return crud.get_all()

@router.put("/{id}/", response_model=TestTabDB)
async def update_entry(payload: TestTabSchema, id: int = Path(..., gt=0)):
    entry = await crud.get(id)
    if not entry :
        raise HTTPException(status_code=404, detail="Entry not found")
    entry_id = await crud.put(id, payload)
    response_obj = {
        "id": entry_id,
        "name":payload.name,
        "descr":payload.descr
    }
    return response_obj

@router.delete("/{id}/", response_model=TestTabDB)
async def del_entry(id: int = Path(..., gt=0)):
    entry = await crud.get(id)
    if not entry :
        raise HTTPException(status_code=404, detail="Entry not found")
    await crud.delete(id)
    return entry

