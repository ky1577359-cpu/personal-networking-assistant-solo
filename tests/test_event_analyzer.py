from app.services.event_analyzer import extract_event_themes

def test_event_analyzer():
    result = extract_event_themes("AI conference")
    assert isinstance(result, list)