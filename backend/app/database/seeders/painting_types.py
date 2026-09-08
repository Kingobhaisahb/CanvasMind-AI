from sqlalchemy.orm import Session

from app.models.painting_type import PaintingType


PAINTING_TYPES = [
    {
        "code": "OIL_PAINTING",
        "name": "Oil Painting",
        "description": "A traditional painting medium characterized by layered pigments, visible brushwork, blending, depth, and rich surface texture.",
        "configuration": {
            "visual_characteristics": [
                "rich layered pigments",
                "visible brushwork",
                "smooth blending where appropriate",
                "strong depth and dimensionality",
                "expressive paint application"
            ],
            "texture_characteristics": [
                "canvas texture",
                "layered paint surface",
                "subtle impasto where appropriate"
            ],
            "color_tendencies": [
                "rich saturated colors",
                "deep tonal variation",
                "smooth color transitions"
            ],
            "composition_tendencies": [
                "strong depth",
                "clear foreground middle-ground background separation",
                "balanced visual hierarchy"
            ],
            "line_characteristics": [
                "organic painted edges",
                "soft transitions where appropriate"
            ],
            "brush_characteristics": [
                "visible directional brushwork",
                "varied brush stroke scale"
            ],
            "negative_constraints": [
                "avoid flat digital illustration appearance",
                "avoid plastic CGI appearance"
            ],
            "generation_guidance": [
                "emphasize physical paint application",
                "preserve painterly depth",
                "use brushwork appropriate to the subject"
            ]
        }
    },

    {
        "code": "WATERCOLOR",
        "name": "Watercolor",
        "description": "A transparent painting medium characterized by luminous washes, paper texture, soft edges, pigment diffusion, and controlled color bleeding.",
        "configuration": {
            "visual_characteristics": [
                "transparent color washes",
                "light luminous appearance",
                "soft transitions",
                "delicate visual treatment"
            ],
            "texture_characteristics": [
                "visible watercolor paper texture",
                "pigment granulation",
                "subtle wash variation"
            ],
            "color_tendencies": [
                "transparent colors",
                "lighter tonal values",
                "natural color variation"
            ],
            "composition_tendencies": [
                "effective use of white space",
                "light visual density",
                "soft atmospheric depth"
            ],
            "line_characteristics": [
                "soft or minimal outlines",
                "natural pigment edges"
            ],
            "brush_characteristics": [
                "wash-based brushwork",
                "fluid strokes"
            ],
            "negative_constraints": [
                "avoid heavy opaque paint",
                "avoid photorealistic rendering",
                "avoid hard digital gradients"
            ],
            "generation_guidance": [
                "preserve paper showing through transparent washes",
                "use controlled pigment diffusion",
                "maintain a delicate handmade appearance"
            ]
        }
    },

    {
        "code": "ACRYLIC",
        "name": "Acrylic",
        "description": "A versatile painting medium characterized by opaque colors, crisp edges, layered paint, varied brush textures, and a contemporary appearance.",
        "configuration": {
            "visual_characteristics": [
                "strong opaque colors",
                "clear shapes",
                "layered paint",
                "contemporary painted appearance"
            ],
            "texture_characteristics": [
                "varied brush texture",
                "layered acrylic surface",
                "subtle physical paint texture"
            ],
            "color_tendencies": [
                "bold colors",
                "high color clarity",
                "strong tonal contrast"
            ],
            "composition_tendencies": [
                "clear subject hierarchy",
                "defined shapes",
                "balanced contemporary composition"
            ],
            "line_characteristics": [
                "crisp edges where appropriate",
                "defined painted boundaries"
            ],
            "brush_characteristics": [
                "visible brush texture",
                "varied stroke direction",
                "layered application"
            ],
            "negative_constraints": [
                "avoid photographic appearance",
                "avoid excessive watercolor transparency"
            ],
            "generation_guidance": [
                "emphasize opaque paint",
                "preserve crisp painted forms",
                "maintain physical acrylic texture"
            ]
        }
    },

    {
        "code": "MADHUBANI",
        "name": "Madhubani",
        "description": "A traditional Indian folk painting form characterized by distinctive linework, ornamental patterns, traditional motifs, dense detailing, and flat color treatment.",
        "configuration": {
            "visual_characteristics": [
                "distinctive decorative linework",
                "ornamental patterns",
                "traditional motifs",
                "dense visual detailing",
                "decorative flat-color treatment"
            ],
            "texture_characteristics": [
                "hand-painted appearance",
                "decorative surface detailing"
            ],
            "color_tendencies": [
                "strong flat color regions",
                "vibrant traditional colors",
                "high color contrast"
            ],
            "composition_tendencies": [
                "dense decorative composition",
                "symbolic arrangement of subjects",
                "limited empty space where appropriate",
                "strong ornamental balance"
            ],
            "line_characteristics": [
                "defined outlines",
                "repeated decorative patterns",
                "intricate line details"
            ],
            "brush_characteristics": [
                "fine controlled strokes",
                "decorative mark-making"
            ],
            "negative_constraints": [
                "avoid photorealistic rendering",
                "avoid cinematic photographic composition",
                "avoid generic digital illustration appearance"
            ],
            "generation_guidance": [
                "emphasize traditional ornamental motifs",
                "use dense decorative detailing",
                "preserve distinctive linework",
                "maintain a handcrafted folk-art appearance"
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