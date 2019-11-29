import pytest

from fcc_coin.block_chain import BlockChain
from fcc_coin.block import Block


@pytest.fixture
def block_chain():
    return BlockChain(Block)


def test_can_be_instantiated(block_chain):
    assert isinstance(block_chain, BlockChain)


def test_can_add_new_blocks_to_chain(block_chain):
    block_a = block_chain.construct_block(0, 0, 0)
    block_b = block_chain.construct_block(0, 0, 0)

    assert block_chain.chain[0] == block_a
    assert block_chain.chain[1] == block_b
