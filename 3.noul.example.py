from typesafe_sdk import Noul, NoulCriteria, TypeSafeClient
from dotenv import load_dotenv

load_dotenv()

with TypeSafeClient() as client:
    response = client.system_one(
        model="jev-latest",
        state="This morning, when I arrived at the bus stop to go to work, there was a Cuban man sitting on the bench.",
        questions={
            "is_sitting": Noul(
                instructions="The Cuban man sitting on the bench.",
            ),
        },
    )

    print(response.model_dump_json(indent=2))