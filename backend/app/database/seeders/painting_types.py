from sqlalchemy.orm import Session

from app.models.painting_type import PaintingType


PAINTING_TYPES = [
    {
        "code": "oil",
        "name": "Oil",
        "description": (
            "Traditional oil painting characterized by rich pigments, "
            "layered brushwork, luminous color depth, and visible painterly texture."
        ),
        "configuration": {
            "visual_characteristics": [
                "rich painterly appearance",
                "layered pigment depth",
                "dimensional forms",
                "naturalistic rendering",
                "subtle tonal transitions",
                "luminous highlights"
            ],

            "color_tendencies": [
                "rich saturated pigments",
                "deep shadows",
                "warm and cool color variation",
                "subtle color mixing",
                "strong tonal depth"
            ],

            "texture_characteristics": [
                "visible oil paint texture",
                "thick pigment in selected areas",
                "soft blended transitions",
                "layered surface depth",
                "subtle impasto"
            ],

            "line_characteristics": [
                "soft painterly edges",
                "minimal hard outlining",
                "form defined primarily through value and color",
                "expressive directional marks"
            ],

            "brush_characteristics": [
                "visible directional brushstrokes",
                "layered brushwork",
                "controlled blending",
                "impasto highlights",
                "varied stroke sizes"
            ],

            "composition_tendencies": [
                "strong focal subject",
                "natural depth hierarchy",
                "foreground, middle ground and background separation",
                "balanced visual weight",
                "cinematic framing when appropriate"
            ],

            "negative_constraints": [
                "avoid flat digital illustration",
                "avoid vector-like edges",
                "avoid plastic 3D rendering",
                "avoid perfectly uniform surfaces",
                "avoid excessive geometric outlining"
            ]
        }
    },

    {
        "code": "watercolor",
        "name": "Watercolor",
        "description": (
            "Watercolor painting characterized by transparent washes, "
            "fluid pigment movement, luminous paper areas, and delicate edges."
        ),
        "configuration": {
            "visual_characteristics": [
                "transparent painterly washes",
                "lightweight atmospheric appearance",
                "delicate organic forms",
                "luminous highlights",
                "soft visual transitions",
                "airy composition"
            ],

            "color_tendencies": [
                "transparent pigments",
                "soft color mixtures",
                "luminous light areas",
                "gentle complementary contrasts",
                "restrained saturation",
                "natural color variation"
            ],

            "texture_characteristics": [
                "visible watercolor paper grain",
                "pigment granulation",
                "soft wash boundaries",
                "water blooms",
                "subtle pigment pooling"
            ],

            "line_characteristics": [
                "delicate lines",
                "soft edges",
                "occasional expressive ink-like marks",
                "minimal heavy outlining"
            ],

            "brush_characteristics": [
                "fluid brush movement",
                "transparent washes",
                "wet-on-wet transitions",
                "wet-on-dry detail",
                "varied water-to-pigment ratios"
            ],

            "composition_tendencies": [
                "generous negative space",
                "light visual density",
                "atmospheric depth",
                "soft transitions between background elements",
                "emphasis on light and openness"
            ],

            "negative_constraints": [
                "avoid thick opaque paint",
                "avoid heavy impasto",
                "avoid plastic surfaces",
                "avoid harsh digital gradients",
                "avoid completely filled backgrounds"
            ]
        }
    },

    {
        "code": "acrylic",
        "name": "Acrylic",
        "description": (
            "Acrylic painting characterized by versatile opaque color, "
            "confident brushwork, crisp shapes, and layered painted surfaces."
        ),
        "configuration": {
            "visual_characteristics": [
                "bold painted forms",
                "opaque color fields",
                "strong visual contrast",
                "clean but painterly shapes",
                "layered acrylic surface",
                "contemporary painted appearance"
            ],

            "color_tendencies": [
                "strong saturated colors",
                "clear color separation",
                "bold complementary contrasts",
                "high color clarity",
                "controlled tonal variation"
            ],

            "texture_characteristics": [
                "visible acrylic paint texture",
                "layered painted surface",
                "occasional dry-brush texture",
                "moderate surface variation"
            ],

            "line_characteristics": [
                "confident edges",
                "defined shapes",
                "expressive painted contours",
                "selective hard edges"
            ],

            "brush_characteristics": [
                "confident brushstrokes",
                "varied stroke widths",
                "dry-brush accents",
                "layered opaque application",
                "controlled texture"
            ],

            "composition_tendencies": [
                "clear focal hierarchy",
                "strong shape organization",
                "balanced masses",
                "graphic readability",
                "deliberate color-based composition"
            ],

            "negative_constraints": [
                "avoid photorealistic CGI",
                "avoid watercolor transparency",
                "avoid excessive oil impasto",
                "avoid perfectly smooth digital fills",
                "avoid vector graphics appearance"
            ]
        }
    },

    {
        "code": "madhubani",
        "name": "Madhubani",
        "description": (
            "Traditional Madhubani folk painting characterized by bold outlines, "
            "flat patterned forms, intricate motifs, symbolic elements, and dense decorative surfaces."
        ),
        "configuration": {
            "visual_characteristics": [
                "traditional Indian folk-art appearance",
                "flat stylized forms",
                "intricate decorative patterns",
                "strong symbolic motifs",
                "dense ornamental detailing",
                "handcrafted folk-art character"
            ],

            "color_tendencies": [
                "vivid traditional colors",
                "red",
                "yellow",
                "green",
                "blue",
                "black outlines",
                "strong color separation"
            ],

            "texture_characteristics": [
                "handcrafted painted surface",
                "dense decorative patterning",
                "fine repeated motifs",
                "organic handmade irregularities",
                "paper-like folk-art surface"
            ],

            "line_characteristics": [
                "bold dark outlines",
                "intricate internal linework",
                "repeated geometric patterns",
                "decorative contour lines",
                "dense fine detailing"
            ],

            "brush_characteristics": [
                "fine controlled strokes",
                "precise decorative marks",
                "repeated patterned strokes",
                "hand-painted irregularity",
                "fine-detail brushwork"
            ],

            "composition_tendencies": [
                "strong central subject",
                "dense decorative framing",
                "limited empty space",
                "symmetrical or balanced arrangement",
                "pattern-filled background",
                "symbolic motifs surrounding the main subject"
            ],

            "negative_constraints": [
                "avoid photorealism",
                "avoid 3D rendering",
                "avoid realistic photographic lighting",
                "avoid soft cinematic depth of field",
                "avoid western oil-painting appearance",
                "avoid empty minimalist backgrounds",
                "avoid glossy digital illustration"
            ]
        }
    }
]


def seed_painting_types(db: Session):
    for data in PAINTING_TYPES:
        existing = (
            db.query(PaintingType)
            .filter(PaintingType.code == data["code"])
            .first()
        )

        if existing:
            continue

        painting_type = PaintingType(**data)
        db.add(painting_type)

    db.commit()