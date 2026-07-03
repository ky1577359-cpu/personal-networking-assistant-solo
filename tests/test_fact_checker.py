from app.services.fact_checker import fact_check

def test_fact_checker():
    result = fact_check("Python")
    assert isinstance(result, str)