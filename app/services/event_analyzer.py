from transformers import pipeline
from app.config import MODEL_NAMES

classifier = pipeline(
    "zero-shot-classification",
    model=MODEL_NAMES["event_analysis"]
)


CANDIDATE_LABELS = [
    "AI",
    "Healthcare",
    "Robotics",
    "Education",
    "Cybersecurity",
    "Finance",
    "Sustainability"
]


def extract_event_themes(description: str):
    result = classifier(
        description,
        CANDIDATE_LABELS,
        multi_label=True
    )

    return result["labels"][:3] # top 3 themes 