from typesafe_sdk import Score, TypeSafeClient
from dotenv import load_dotenv

load_dotenv()

with TypeSafeClient() as client:
    response = client.system_one(
        state="I asked my AI agent how many points Kobe Bryant scored in his NBA playoff career? My AI agent said 5,000. The correct answer is 5,640",
        questions={
            "judge": Score(
                instructions="How would you rate the AI's answer?",
                criteria=[
                    "Bad",
                    "Not too bad",
                    "Neutral",
                    "Good",
                    "Great",
                ],
            ),
        },
    )

    print(response.model_dump_json(indent=2))