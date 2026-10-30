from typesafe_sdk import Choice, TypeSafeClient
from dotenv import load_dotenv

load_dotenv()

with TypeSafeClient() as client:
    response = client.system_one(
        state={
            "time_of_day": "9am",
            "characters": {
                "character_1": "Tad",
                "character_2": "Cuban Man"
            },
            "scene": "A bus stop in Miami. Tad arrives to head to his destination and the Cuban Man is sitting on the bus stop bench when Tad arrives.",
            "temperature": "85 degrees Fahrenheit"
        },
        questions={
            "nationality": Choice(
                instructions="What nationality was the man on the bench?",
                criteria={
                    "cuban": "As in Cuba",
                    "haitian": "As in Haiti (aka Ayiti)",
                    "other": "None of the other options"
                },
            ),
            "time_of_day": Choice(
                instructions="What time of day did this take place?",
                criteria={
                    "morning": "In the AM",
                    "noon": "Around the middle of the day",
                    "evening": "In the afternoon",
                    "night": "In the nighttime",
                    "other": "None of the other options"
                },
            ),
        },
    )

    print(response.model_dump_json(indent=2))
