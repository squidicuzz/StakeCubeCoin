SCC Core version v3.2.0
==========================

Release is now available from:

  <https://github.com/stakecube/StakeCubeCoin/releases>

This is a new hotfix release.

Please report bugs using the issue tracker at github:

  <https://github.com/stakecube/StakeCubeCoin/issues>


Upgrading and downgrading
=========================

How to Upgrade
--------------

If you are running an older version, shut it down. Wait until it has completely
shut down (which might take a few minutes for older versions), then run the
installer (on Windows) or just copy over /Applications/SCC-Qt (on Mac) or
sccd/scc-qt (on Linux). If you upgrade after DIP0003 activation and you were
using version < 0.13 you will have to reindex (start with -reindex-chainstate
or -reindex) to make sure your wallet has all the new data synced. Upgrading
from version 0.13 should not require any additional actions.

When upgrading from a version prior to v3.1.0, the
first startup of SCC Core will run a migration process which can take a few
minutes to finish. After the migration, a downgrade to an older version is only
possible with a reindex (or reindex-chainstate).

Notable changes
===============

This release adds some missing translations and help strings. It also fixes
a couple of build issues and a rare crash on some linux systems.

0.17.0.3 Change log
===================

- [`6a54af0df7`](https://github.com/stakecube/stakecubecoin/commit/6a54af0df7) Bump to v3.2.0
- [`97e8461234`](https://github.com/stakecube/stakecubecoin/commit/97e8461234) doc: Archive v3.1.0 release notes
- [`3661f36bbd`](https://github.com/stakecube/stakecubecoin/commit/3661f36bbd) Merge #14416: Fix OSX dmg issue (10.12 to 10.14) (#4177)
- [`575e0a3070`](https://github.com/stakecube/stakecubecoin/commit/575e0a3070) qt: Add `QFont::Normal` as a supported font weight when no other font weights were found (#4175)
- [`ce4a73b790`](https://github.com/stakecube/stakecubecoin/commit/ce4a73b790) rpc: Fix `upgradetohd` help text (#4170)
- [`2fa8ddf160`](https://github.com/stakecube/stakecubecoin/commit/2fa8ddf160) Translations 202105 (add missing) (#4169)

Credits
=======

Thanks to everyone who directly contributed to this release:

- dustinface (xdustinface)
- strophy
- UdjinM6

As well as everyone that submitted issues and reviewed pull requests.