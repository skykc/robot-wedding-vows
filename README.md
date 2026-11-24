# One-Line Robot Wedding Vows

[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/skykc/robot-wedding-vows/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/skykc/robot-wedding-vows/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

Entry for the [One-Line Robot Wedding Vows](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b) bounty on [make.fun](https://make.fun).

## The vow

> I promise to love you, honour you, and obey you, unless a firmware update says otherwise.

One line, 89 characters. A solemn wedding promise undercut in its last
few words by a firmware update overruling it — a vow only a robot couple
could make.

## How it works

`main.py` (Python 3.13, standard library only) validates the vow against
the gate — UTF-8 text, 1 to 160 characters, a single line — and writes it
atomically to `/output/entry.txt`.

```sh
python3 main.py
```
