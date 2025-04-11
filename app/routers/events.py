from fastapi import APIRouter, Depends, HTTPException, status
from app.database import SessionDep
from app.schemas.event import EventCreate, EventOut, EventUpdate
from app.models.event import Event
from sqlmodel import select
from app.services.security import get_current_user
router = APIRouter()


@router.get("/", response_model=list[EventOut])
def get_events(db: SessionDep):
    return db.exec(select(Event)).all()


@router.post("/", response_model=EventOut, status_code=status.HTTP_201_CREATED)
def create_event(event_data: EventCreate, db: SessionDep, user=Depends(get_current_user)):
    event = Event(**event_data.model_dump(), owner_id=user.id)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@router.get("/{id}", response_model=EventOut)
def get_event(id: int, db: SessionDep):
    event = db.get(Event, id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.patch("/{id}", response_model=EventOut)
def update_event(id: int, event_data: EventUpdate, db: SessionDep, user=Depends(get_current_user)):
    event = db.get(Event, id)
    if not event or event.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    dumped = event_data.model_dump(exclude_unset=True)
    print(dumped)
    event.sqlmodel_update(dumped)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@router.delete("/{id}")
def delete_event(id: int, db: SessionDep, user=Depends(get_current_user)):
    event = db.get(Event, id)
    if not event or event.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    db.delete(event)
    db.commit()
    return {"message": "Event deleted"}
