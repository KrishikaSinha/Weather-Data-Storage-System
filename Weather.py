from dataclasses import dataclass

@dataclass
class WeatherRecord:
    date: str       # Format: "dd/mm/yyyy"
    city: str
    temperature:float; 