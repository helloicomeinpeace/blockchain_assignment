import pytest

from fcc_coin.block_chain import BlockChain
from fcc_coin.block import Block


@pytest.fixture
def block_chain():
    return BlockChain(Block)


def test_can_be_instantiated(block_chain):
    assert isinstance(block_chain, BlockChain)


def test_creates_genesis_block(block_chain):
    genesis_block = block_chain.chain[0]

    assert genesis_block.proof_no == 0
    assert genesis_block.prev_hash == 0
    assert genesis_block.data == 0


def test_can_add_new_blocks_to_chain(block_chain):
    block = block_chain.construct_block(0, 0, 0)

    assert block_chain.chain[1] == block
