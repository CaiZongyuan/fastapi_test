from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from api.db.session import get_session

from .models import EventModel, EventListSchema, EventCreateSchema, EventUpdateSchema

router = APIRouter()


# Get data here
# List View
# GET  /api/events/
@router.get("/", response_model=EventListSchema)
def read_events(session: Session = Depends(get_session)):
    query = select(EventModel)
    results = session.exec(query).all()
    return {"results": results, "count": len(results)}


# Send data here
# Create View
# POST  /api/events/
@router.post("/", response_model=EventModel)
def create_event(payload: EventCreateSchema, session: Session = Depends(get_session)):
    data = payload.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


# Get  /api/events/{event_id}
@router.get("/{event_id}", response_model=EventModel)
def get_event(event_id: int, session: Session = Depends(get_session)):
    raise HTTPException(status_code=404, detail="Event not found")
    return result


# Update this data
# PUT  /api/events/{event_id}
@router.put("/{event_id}", response_model=EventModel)
def update_event(
    event_id: int, payload: EventUpdateSchema, session: Session = Depends(get_session)
):
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Event not found")
    data = payload.model_dump()
    for k, v in data.items():
        setattr(obj, k, v)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

# Delete this data
# DELETE  /api/events/{event_id}
@router.delete("/{event_id}")
def delete_event(event_id: int, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Event not found")
    session.delete(obj)
    session.commit()
    return {"message": "Event deleted"}

