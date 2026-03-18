from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud, database, utils
from .loggers import logger

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Address Book API")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addresses", response_model=schemas.AddressResponse)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    logger.info(f"POST /addresses called with data: {address.dict()}")
    try:
        result = crud.create_address(db, address)
        logger.info(f"Address created successfully with id={result.id}")
        return result

    except Exception as e:
        logger.error(f"Error creating address: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get("/addresses")
def get_addresses(db: Session = Depends(get_db)):
    logger.info("Fetching all addresses from DB")
    try:
        result = crud.get_addresses(db)
        logger.info(f"Fetched {len(result)} addresses")
        return result

    except Exception as e:
        logger.error(f"Error fetching addresses: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.put("/addresses/{address_id}")
def update_address(address_id: int, address: schemas.AddressCreate, db: Session = Depends(get_db)):
    logger.info(f"Updating address id={address_id}")

    try:
        result = crud.update_address(db, address_id, address)

        if not result:
            logger.warning(f"Address with id={address_id} not found")
            raise HTTPException(status_code=404, detail="Address not found")

        logger.info(f"Address with id={address_id} updated successfully")
        return result

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating address: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting address id={address_id}")

    try:
        result = crud.delete_address(db, address_id)

        if not result:
            logger.warning(f"Address with id={address_id} not found")
            raise HTTPException(status_code=404, detail="Address not found")

        logger.info(f"Address with id={address_id} deleted successfully")
        return {"message": "Deleted successfully"}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting address: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get("/addresses/nearby")
def get_nearby_addresses(lat: float, lon: float, distance: float, db: Session = Depends(get_db)):
    logger.info(f"GET /addresses/nearby called with lat={lat}, lon={lon}, distance={distance}")
    try:
        addresses = crud.get_addresses(db)
        result = []

        for addr in addresses:
            dist = utils.calculate_distance(lat, lon, addr.latitude, addr.longitude)
            if dist <= distance:
                result.append(addr)

        logger.info(f"Found {len(result)} addresses within {distance} km")
        return result

    except Exception as e:
        logger.error(f"Error in nearby search: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")