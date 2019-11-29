class BlockChain:

    def __init__(self, block):
        self.block = block
        self.chain = []

    def construct_block(self, proof_no, prev_hash, data):
        block = self.block(
            index=len(self.chain),
            proof_no=proof_no,
            prev_hash=prev_hash,
            data=data
        )

        self.chain.append(block)
        return block
