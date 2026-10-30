from typesafe_sdk import Choice, TypeSafeClient
from dotenv import load_dotenv

load_dotenv()

with TypeSafeClient() as client:
    response = client.system_one(
        state="""
Today, when I arrived at the bus stop to go to work, there was a man sitting on the bench.
        """,
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
