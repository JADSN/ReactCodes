from datetime import datetime, timezone

from schemas import CreateTaskIem, UpdateTaskIem
from models import TaskIem

from dependencies import Session, Depends, HTTPException, status, get_db


def read_all(db: Session = Depends(get_db)):
    return db.query(TaskIem).all()


def read_one(id: int, db: Session = Depends(get_db)):
    item = db.query(TaskIem).where(TaskIem.id == id)
    task = item.one()
    return task


def create(req_body: CreateTaskIem, db: Session = Depends(get_db)):
    # ts_now = datetime.now(timezone.utc).timestamp()
    # ts_now_int = int(ts_now * 1000)

    new_data = TaskIem(
        text=req_body.text, day=req_body.day, reminder=False)

    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data


def update_one(id: int, req_body: UpdateTaskIem, db: Session = Depends(get_db)):

    item = db.query(TaskIem).where(TaskIem.id == id)

    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {id} not found")

    # ts_now = datetime.now(timezone.utc).timestamp()
    # ts_now_int = int(ts_now * 1000)

    item.update(
        {"reminder": req_body.reminder})

    db.commit()

    return item.first()


def delete_one(id: int, db: Session = Depends(get_db)):
    item = db.query(TaskIem).where(TaskIem.id == id)

    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {id} not found")

    item.delete(synchronize_session=False)
    db.commit()

    return item.first()
