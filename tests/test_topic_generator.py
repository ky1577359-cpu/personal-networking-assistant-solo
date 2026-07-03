from app.services.topic_generator import generate_topics

def test_topic_generator():
    result = generate_topics(["AI"], ["Python"])
    assert isinstance(result, list)