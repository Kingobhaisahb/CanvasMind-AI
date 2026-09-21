from pathlib import Path
from uuid import uuid4

from PIL import Image


class ImageStorage:

    def __init__(self):
        self.storage_directory = (
            Path(__file__).resolve().parent / "generated"
        )

        self.storage_directory.mkdir(
            parents=True,
            exist_ok=True
        )

    def save_image(self, image: Image.Image) -> str:
        """
        Save a generated image using a unique filename.

        Returns the relative path to the saved image.
        """

        filename = f"{uuid4()}.png"

        file_path = self.storage_directory / filename

        image.save(
            file_path,
            format="PNG"
        )

        return str(
            Path("generated") / filename
        )