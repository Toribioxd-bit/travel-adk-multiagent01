from travel_assistant.tools.culture_tools import recommend_local_culture


def test_recommend_local_culture_for_cusco():
    result = recommend_local_culture("Cusco")

    assert result["status"] == "success"
    assert result["destination"] == "Cusco"
    assert len(result["foods"]) >= 1
    assert len(result["customs"]) >= 1
    assert len(result["phrases"]) >= 1


def test_recommend_local_culture_default_case():
    result = recommend_local_culture("Unknown destination")

    assert result["status"] == "success"
    assert result["foods"]
    assert result["customs"]
    assert result["phrases"]