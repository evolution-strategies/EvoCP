def test_mutation_structure():
    from evocp.evolution import mutate_cognitive_operations
    from evocp.api import BASE_PROMPT

    mutated = mutate_cognitive_operations(BASE_PROMPT)
    assert "1." in mutated and "5." in mutated
