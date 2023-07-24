#!/usr/bin/env bash
# use testnet settings,  if you need mainnet,  use ~/.stakecubecoin/sccd.pid file instead
# Copyright (c) 2018-2020 The Dash Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
export LC_ALL=C

scc_pid=$(<~/.stakecubecoin/testnet3/sccd.pid)
sudo gdb -batch -ex "source debug.gdb" sccd ${scc_pid}
