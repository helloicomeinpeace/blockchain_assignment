# fccCoin

A simple cryptocurrency call fccCoin.

```
>>> from fcc_coin.block import Block
>>> from fcc_coin.block_chain import BlockChain

>>> block_chain = BlockChain(Block)
>>> print(block_chain.chain)
[<fcc_coin.block.Block object at 0x107038fd0>]

>>> last_block = block_chain.last_block
>>> last_proof_no = last_block.proof_no
>>> proof_no = block_chain.proof_of_work(last_proof_no)
>>> data = 'Bob Geldof'
>>> last_hash = last_block.calculate_hash()
>>> new_block = block_chain.construct_block(proof_no, last_hash, data)
>>> print(block_chain.chain)
[<fcc_coin.block.Block object at 0x107038fd0>, <fcc_coin.block.Block object at 0x10703dbd0>]

>>> BlockChain.check_validity(new_block, last_block)
True
```
