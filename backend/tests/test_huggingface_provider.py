from PIL import Image

from app.providers.image_generation_provider import (
    HuggingFaceImageGenerationProvider
)


class FakeInferenceClient:

    def __init__(self):
        self.received_width = None
        self.received_height = None
        self.received_prompt = None
        self.received_model = None

    def text_to_image(
        self,
        prompt,
        model,
        width,
        height
    ):

        self.received_prompt = prompt
        self.received_model = model
        self.received_width = width
        self.received_height = height

        return Image.new(
            "RGB",
            (width, height)
        )


def test_huggingface_provider_passes_dimensions():

    provider = HuggingFaceImageGenerationProvider()

    fake_client = FakeInferenceClient()

    provider.client = fake_client

    result = provider.generate(
        prompt="A beautiful Madhubani village",
        width=1024,
        height=1024
    )

    assert fake_client.received_width == 1024
    assert fake_client.received_height == 1024

    assert result.image.size == (
        1024,
        1024
    )

    assert result.provider_name == "huggingface"

    assert result.metadata["requested_width"] == 1024
    assert result.metadata["requested_height"] == 1024

    assert result.metadata["actual_width"] == 1024
    assert result.metadata["actual_height"] == 1024