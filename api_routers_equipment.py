"""Endpoints : panneaux, onduleurs, batteries."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database_session import get_db
from models_panel import Panel
from models_inverter import Inverter
from models_battery import Battery

router = APIRouter()


@router.get("/panels")
def list_panels(db: Session = Depends(get_db)):
    return db.query(Panel).all()


@router.get("/inverters")
def list_inverters(db: Session = Depends(get_db)):
    return db.query(Inverter).all()


@router.get("/batteries")
def list_batteries(db: Session = Depends(get_db)):
    return db.query(Battery).all()
