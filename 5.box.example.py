from pathlib import Path
from typesafe_sdk import Image, TypeSafeClient, Box
from dotenv import load_dotenv
from PIL import Image as PILimage, ImageDraw

load_dotenv()

with TypeSafeClient() as client:
    response = client.system_one(
        state=[Image(Path("media/dog.jpg"))],
        questions={
            "dog": Box(
                instructions="The dog in the photo",
            ),
        },
        extra_headers={"TypeSafe-Danger-Zone-Images": "true"},
    )
    
    print(response.model_dump_json(indent=2))

    image = PILimage.open("media/dog.jpg")
    width, height = image.size
    edges = response.boxes["dog"].box

    box = (
        round(edges.left * width),
        round(edges.top * height),
        round(edges.right * width),
        round(edges.bottom * height),
    )
    draw = ImageDraw.Draw(image)
    draw.rectangle(box, outline="blue", width=4)
    image.save("media/dog_with_box.jpg")