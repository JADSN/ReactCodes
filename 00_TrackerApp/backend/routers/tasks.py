from datetime import datetime, timezone

from dependencies import *

from schemas import CreateTaskIem, UpdateTaskIem

from repositories import task

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.get("/", status_code=200)
async def read_all(db: Session = Depends(get_db)):
    return task.read_all(db)


@router.get("/{id}", status_code=200)
async def read_one(id: int, db: Session = Depends(get_db)):
    return task.read_one(id, db)


@router.post("/", status_code=200)
async def create(req_body: CreateTaskIem, db: Session = Depends(get_db)):
    return task.create(req_body, db)


@router.put("/{id}", status_code=200)
async def update_one(id: int, req_body: UpdateTaskIem, db: Session = Depends(get_db)):
    return task.update_one(id, req_body, db)


@router.delete("/{id}", status_code=200)
async def delete_one(id: int, db: Session = Depends(get_db)):
    return task.delete_one(id, db)
