BTC Channel
===========

This package contains the system gateway for assigning and making requests to the system default payment channel.

Notes
-----

Upon release, this package and the uses described below conform to v0.1 of the Bitcoin Computer Project API. This version of the API is extremely preliminary.

Installation
------------

1. Download the `btc-system-channel-0.1.tar.gz` from the latest release.
2. Untar and install:

  ```
  $> tar -xvf btc-system-channel-0.1.tar.gz
  $> cd btc-system-channel
  $> ./configure
  $> make
  $> sudo make install
  ```
3. Install and configure a specific payment channel interface. There are currently available interfaces for:
  * [Electrum](https://github.com/BitcoinComputer/btc-channel-electrum)


Configuration
-------------

Assign your payment channel adapter. For example, btc-channel-electrum:
```
$> sudo btc-channel --configure --channel=btc-channel-electrum
```

Use
---



Create a payment request for 0.258 bitcoin. The given amount must be in Satoshi. Provides a payment request id to stdout, eg: `543df896f34321e985fec37ea0de69d5`.
```
$ btc-channel --create --amount=25800000
```

Generate a payment request body for request `543df896f34321e985fec37ea0de69d5`. Request body shall be in Bitcoin URI BIP21 format.
```
btc-channel 543df896f34321e985fec37ea0de69d5 --body
```

Query whether payment request `543df896f34321e985fec37ea0de69d5` has been paid. Will stdout a -1 if unfulfilled, 0 if fulfilled.
```
btc-channel 543df896f34321e985fec37ea0de69d5 --verify-payment
```
