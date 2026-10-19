# ORDERS: the order sheet (orders Brennan places by hand in the Robinhood app)

The assistant does not place orders. When a rule fires it adds a block here (status PENDING) and sends a PushNotification "ORDER for you: ...". Brennan places it, then tells the assistant (or the next check-in sees the fill), and the block moves to DONE with the fill price. Stale PENDING blocks are cancelled by the assistant at the next check-in with a reason.

Format of a block:
```
### [date time ET] PENDING | <SYMBOL> <BUY|SELL> <qty> <market|limit $x|stop $x> <GTC|GFD>
Cancel first: <order id or none>
Why: <rule/thesis, link to trades.md block>
Deadline: <time ET or "before 4pm ET">
After it fills: <the follow-up order, e.g. re-place stop on remaining shares at $x>
```

## PENDING
(none)

## DONE / CANCELLED
(none yet)
