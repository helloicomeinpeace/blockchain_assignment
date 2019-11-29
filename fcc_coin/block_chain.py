class BlockChain:

    def __init__(self, block):
        self.block = block
        self.chain = []
        self.construct_genesis()

    def construct_block(self, proof_no, prev_hash, data):
        block = self.block(
            index=len(self.chain),
            proof_no=proof_no,
            prev_hash=prev_hash,
            data=data
        )

        self.chain.append(block)
        return block

    def construct_genesis(self):
        genesis_block = self.construct_block(proof_no=0, prev_hash=0, data=0)

        return genesis_block

    @staticmethod
    def check_validity(block, prev_block):
        if prev_block.index + 1 != block.index:
            return False
        elif prev_block.calculate_hash() != block.prev_hash:
            return False
        elif prev_block.timestamp and block.timestamp:
            if prev_block.timestamp > block.timestamp:
                return False

        return True
