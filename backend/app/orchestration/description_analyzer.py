import json

from huggingface_hub import InferenceClient

from app.core.config import settings
from app.orchestration.generation_spec import (
    ColorDirectionSpec,
    EnvironmentSpec,
    LightingSpec,
    SubjectSpec,
)


class DescriptionAnalyzer:

    def __init__(self):
        self.client = InferenceClient(
            api_key=settings.hf_token
        )

    def analyze(
        self,
        description: str
    ) -> tuple[
        SubjectSpec,
        EnvironmentSpec,
        LightingSpec,
        ColorDirectionSpec
    ]:

        system_prompt = """
You are a visual scene analysis engine for an AI painting generation system.

Your job is to analyze a user's painting description and extract only
information that is explicitly stated or strongly implied by the description.

You are NOT responsible for:
- choosing the painting style
- choosing the painting type
- deciding canvas orientation
- deciding composition rules
- writing the final image-generation prompt

Your job is ONLY to understand the visual content of the user's description.

Extract:

1. SUBJECT
- Identify the primary subject.
- Identify important secondary subjects or objects.
- Describe meaningful relationships between subjects.

2. ENVIRONMENT
- Identify the setting or environment.
- Identify important background elements.
- Identify useful foreground, middle-ground, or background depth elements.

3. LIGHTING
- Identify lighting conditions only when the description provides them.
- Identify light direction only when stated or strongly implied.
- Identify light quality when supported by the description.

4. COLOR
- Extract explicitly mentioned or strongly implied colors.
- Identify contrast only when supported by the description.
- Identify saturation only when supported by the description.

IMPORTANT:
Do not invent details that are not present in the description.

If information is not specified, use "unspecified".

Keep extracted information concise and useful for downstream image generation.
"""

        response_format = {
            "type": "json_schema",
            "json_schema": {
                "name": "DescriptionAnalysis",
                "schema": {
                    "type": "object",
                    "properties": {
                        "subject": SubjectSpec.model_json_schema(),
                        "environment": EnvironmentSpec.model_json_schema(),
                        "lighting": LightingSpec.model_json_schema(),
                        "color_direction": ColorDirectionSpec.model_json_schema(),
                    },
                    "required": [
                        "subject",
                        "environment",
                        "lighting",
                        "color_direction",
                    ],
                    "additionalProperties": False,
                },
                "strict": True,
            },
        }

        response = self.client.chat_completion(
            model=settings.hf_analysis_model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt.strip(),
                },
                {
                    "role": "user",
                    "content": description,
                },
            ],
            response_format=response_format,
            temperature=0.1,
            max_tokens=1000,
        )

        content = response.choices[0].message.content

        if not content:
            raise ValueError(
                "Description analyzer returned an empty response."
            )

        data = json.loads(content)

        return (
            SubjectSpec.model_validate(data["subject"]),
            EnvironmentSpec.model_validate(data["environment"]),
            LightingSpec.model_validate(data["lighting"]),
            ColorDirectionSpec.model_validate(
                data["color_direction"]
            ),
        )