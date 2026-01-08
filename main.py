
from fastapi import FastAPI
from pydantic import BaseModel
from test_api import get_weather_data, API_KEY

app = FastAPI()

class WeatherQuery(BaseModel):
    city: str

@app.post("/query_weather")
def query_weather(item: WeatherQuery):
    result = get_weather_data(item.city, API_KEY)
    return {"Reply":result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
