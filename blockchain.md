# Blockchain implementation
Since the requirements are very vague, there were many assumption.

Also nonce (proof) wasn't implemented as well as mining algorithm. Don't know if it is required.

Linked list was implemented to chain Blocks.

New block is added to the head.

During add, new block validates previous hash and in case of mismatch block is not added.

There is also a tail pointer in case we need access genesis.

Adding block time complexity is O(1)
Getting a block by index takes O(n)

Genesis block is created during Blockchain initialization.