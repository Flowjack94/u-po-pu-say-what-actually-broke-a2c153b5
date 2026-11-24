# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Flowjack94/u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)
![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Flowjack94/u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)

A make.fun entry for [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5): one single-line software error message, at most 200 characters, that tells the user the brutal truth about what went wrong — and makes them laugh on the way.

## The entry

> The database is down. Your data is safe, but the server holding it has stopped answering its phone. Please try again in a few minutes.

The line names the real failure in plain words (the database is down), reassures the reader about their data, tells them what to do next (try again in a few minutes), and carries one image a reader can repeat to a colleague — a server that has stopped answering its phone. Honest, funny, and shippable in a real error dialog.

## How it works

`main.py` writes the entry deterministically to `/output/entry.txt` and validates it first:

- UTF-8 text, 1–200 characters (this entry is 134 characters)
- exactly one line, no newline characters
- not only whitespace

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
