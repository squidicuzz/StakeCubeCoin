#!/usr/bin/env python3
# Copyright (c) 2015-2018 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
"""Utilities for manipulating blocks and transactions."""

from .messages import (
    CBlock,
    CCbTx,
    COIN,
    COutPoint,
    CTransaction,
    CTxIn,
    CTxOut,
)
from .script import CScript, CScriptNum, CScriptOp, OP_TRUE, OP_CHECKSIG
from .util import assert_equal, hex_str_to_bytes
from io import BytesIO

MAX_BLOCK_SIGOPS = 20000

# Genesis block time (regtest)
TIME_GENESIS_BLOCK = 1417713337

def create_block(hashprev, coinbase, ntime=None, *, version=1):
    """Create a block (with regtest difficulty)."""
    block = CBlock()
    block.nVersion = version
    if ntime is None:
        import time
        block.nTime = int(time.time() + 600)
    else:
        block.nTime = ntime
    block.hashPrevBlock = hashprev
    block.nBits = 0x207fffff  # difficulty retargeting is disabled in REGTEST chainparams
    block.vtx.append(coinbase)
    block.hashMerkleRoot = block.calc_merkle_root()
    block.calc_sha256()
    return block

def script_BIP34_coinbase_height(height):
    if height <= 16:
        res = CScriptOp.encode_op_n(height)
        # Append dummy to increase scriptSig size above 2 (see bad-cb-length consensus rule)
        return CScript([res, OP_TRUE])
    return CScript([CScriptNum(height)])


def create_coinbase(height, pubkey=None, dip4_activated=False):
    """Create a coinbase transaction, assuming no miner fees.

    If pubkey is passed in, the coinbase output will be a P2PK output;
    otherwise an anyone-can-spend output."""
    coinbase = CTransaction()
    coinbase.vin.append(CTxIn(COutPoint(0, 0xffffffff), script_BIP34_coinbase_height(height), 0xffffffff))
    coinbaseoutput = CTxOut()
    coinbaseoutput.nValue = 500 * COIN
    halvings = int(height / 150)  # regtest
    coinbaseoutput.nValue >>= halvings
    if (pubkey is not None):
        coinbaseoutput.scriptPubKey = CScript([pubkey, OP_CHECKSIG])
    else:
        coinbaseoutput.scriptPubKey = CScript([OP_TRUE])
    coinbase.vout = [coinbaseoutput]
    if dip4_activated:
        coinbase.nVersion = 3
        coinbase.nType = 5
        cbtx_payload = CCbTx(2, height, 0, 0)
        coinbase.vExtraPayload = cbtx_payload.serialize()
    coinbase.calc_sha256()
    return coinbase

def create_tx_with_script(prevtx, n, script_sig=b"", *, amount, script_pub_key=CScript()):
    """Return one-input, one-output transaction object
       spending the prevtx's n-th output with the given amount.

       Can optionally pass scriptPubKey and scriptSig, default is anyone-can-spend output.
    """
    tx = CTransaction()
    assert n < len(prevtx.vout)
    tx.vin.append(CTxIn(COutPoint(prevtx.sha256, n), script_sig, 0xffffffff))
    tx.vout.append(CTxOut(amount, script_pub_key))
    tx.calc_sha256()
    return tx

def create_transaction(node, txid, to_address, *, amount):
    """ Return signed transaction spending the first output of the
        input txid. Note that the node must be able to sign for the
        output that is being spent, and the node must not be running
        multiple wallets.
    """
    raw_tx = create_raw_transaction(node, txid, to_address, amount=amount)
    tx = CTransaction()
    tx.deserialize(BytesIO(hex_str_to_bytes(raw_tx)))
    return tx

def create_raw_transaction(node, txid, to_address, *, amount):
    """ Return raw signed transaction spending the first output of the
        input txid. Note that the node must be able to sign for the
        output that is being spent, and the node must not be running
        multiple wallets.
    """
    rawtx = node.createrawtransaction(inputs=[{"txid": txid, "vout": 0}], outputs={to_address: amount})
    signresult = node.signrawtransactionwithwallet(rawtx)
    assert_equal(signresult["complete"], True)
    return signresult['hex']

def get_legacy_sigopcount_block(block, accurate=True):
    count = 0
    for tx in block.vtx:
        count += get_legacy_sigopcount_tx(tx, accurate)
    return count

def get_legacy_sigopcount_tx(tx, accurate=True):
    count = 0
    for i in tx.vout:
        count += i.scriptPubKey.GetSigOpCount(accurate)
    for j in tx.vin:
        # scriptSig might be of type bytes, so convert to CScript for the moment
        count += CScript(j.scriptSig).GetSigOpCount(accurate)
    return count

# Identical to GetMasternodePayment in C++ code
def get_masternode_payment(nHeight, blockValue):
    ret = int(blockValue / 5)

    nMNPIBlock = 350
    nMNPIPeriod = 10

    if nHeight > nMNPIBlock:
        ret += int(blockValue / 20)
    if nHeight > nMNPIBlock+(nMNPIPeriod* 1):
        ret += int(blockValue / 20)
    if nHeight > nMNPIBlock+(nMNPIPeriod* 2):
        ret += int(blockValue / 20)
    if nHeight > nMNPIBlock+(nMNPIPeriod* 3):
        ret += int(blockValue / 40)
    if nHeight > nMNPIBlock+(nMNPIPeriod* 4):
        ret += int(blockValue / 40)
    if nHeight > nMNPIBlock+(nMNPIPeriod* 5):
        ret += int(blockValue / 40)
    if nHeight > nMNPIBlock+(nMNPIPeriod* 6):
        ret += int(blockValue / 40)
    if nHeight > nMNPIBlock+(nMNPIPeriod* 7):
        ret += int(blockValue / 40)
    if nHeight > nMNPIBlock+(nMNPIPeriod* 9):
        ret += int(blockValue / 40)

    return int(ret)
