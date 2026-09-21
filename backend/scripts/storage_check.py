from PIL import Image

from app.storage.image_storage import ImageStorage


storage = ImageStorage()

image = Image.new(
    "RGB",
    (100, 100),
    "white"
)

path = storage.save_image(image)

print("IMAGE STORAGE SUCCESSFUL")
print("Saved:", path)