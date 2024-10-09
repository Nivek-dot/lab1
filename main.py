from fastapi import FastAPI

app = FastAPI()

@app.get("/factorial/{mainnumber}")
def factorial(mainnumber: int):
    if mainnumber == 0:
        return {"return": False}

    resulta = 1
    numero = mainnumber

    while numero > 1:
        resulta *= numero
        numero -= 1

    return {"mainnumber": mainnumber, "factorial": resulta}