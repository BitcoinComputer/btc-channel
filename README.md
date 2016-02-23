BTC Channel
===========

This package contains the system gateway for assigning and making requests to the system default payment channel.

Notes
-----

Upon release, this package and the uses described below conform to v0.1 of the Bitcoin Computer Project API. This version of the API is extremely preliminary.


Use
---

Assign the Coinbase channel as the system default.
```
# btc-channel --configure -s=btc-channel-coinbase
```

Create a payment request for 0.258 bitcoin. Provides a payment request id to stdout, eg: `543df896f34321e985fec37ea0de69d5`.
```
$ btc-channel --create -a 0.258
```

Generate a payment request body for request `543df896f34321e985fec37ea0de69d5`. Request body shall be in Bitcoin URI BIP21 format.
```
btc-channel 543df896f34321e985fec37ea0de69d5 --body
```

Query whether payment request `543df896f34321e985fec37ea0de69d5` has been paid. Will stdout a 0 if unfulfilled, 1 if fulfilled.
```
btc-channel 543df896f34321e985fec37ea0de69d5 --verify-payment
```
