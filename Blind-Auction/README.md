# 🔨 Blind Auction

A command-line blind auction game.

## How it works

1. Each bidder enters their name and bid (in SAR).
2. The screen is cleared after each bid so the next bidder can't see it.
3. Answering `no` (or `n`, in any case) ends the bidding.
4. When there are no more bidders, the highest bid wins. If two bids tie, the first one entered wins.

## Concepts used

- Dictionaries to store each bidder's name and bid
- `while` loops and user input
- Input checking, so a typo in a bid asks again instead of crashing
- `max()` with a `key` to find the highest bid
- Imported ASCII art from `art.py`

## Run it

```bash
python3 Blind-Auction.py
```
