#!/usr/bin/env bash
# use testnet settings,  if you need mainnet,  use ~/.stakecubecoin/sccd.pid file instead
export LC_ALL=C

scc_pid=$(<~/.stakecubecoin/testnet3/sccd.pid)
sudo gdb -batch -ex "source debug.gdb" sccd ${scc_pid}
