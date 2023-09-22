from parser_pro.lexer.tokens import generate_tokens


def test_statement_split_success():
    expr = 'hobbies | $join("|")'
    assert generate_tokens(expr) == ["hobbies", '$join("|")']

    expr = "hobbies | hobbies"
    assert generate_tokens(expr) == ["hobbies", "hobbies"]

    expr = '$split("|")'
    assert generate_tokens(expr) == ['$split("|")']
