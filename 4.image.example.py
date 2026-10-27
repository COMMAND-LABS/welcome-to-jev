from pathlib import Path
from typesafe_sdk import Choice, Image, Noul, TypeSafeClient
from dotenv import load_dotenv

load_dotenv()

with TypeSafeClient() as client:
    response = client.system_one(
        state=[Image(Path("media/dog.jpg"))],
        questions={
            "dog_present": Noul(instructions="Is there a dog in the photo?"),
            "breed": Choice(
                instructions="What type of dog is in the photo?",
                criteria={
                    "Pug": "Pug",
                    "Golden Retriever": "Golden Retriever",
                    "Cocker Spaniel": "Cocker Spaniel",
                    "Other": "Other",
                },
            ),
        },
        extra_headers={"TypeSafe-Danger-Zone-Images": "true"},
    )
    
    print(response.model_dump_json(indent=2))