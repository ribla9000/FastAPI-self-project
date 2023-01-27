from fastapi import HTTPException


def read_log(result):
    error = HTTPException(status_code=404, detail="Not found")
    if not result:
        return {"error": error, "status": False, "payload": result}
    return {"error": None, "status": True, "payload": result}
