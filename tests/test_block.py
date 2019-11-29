from fcc_coin.block import Block


def test_calculate_hash():
    block = Block(0, 0, 0, 0, 0)

    hash = "15e8d1deeb2d39979fc46431b914d5731197637450bb76dd297fe9fb5ea0de7a"

    assert block.calculate_hash() == hash
