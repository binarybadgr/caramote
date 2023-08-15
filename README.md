Caramote
===

An extension from [Crangon](https://github.com/binarybadgr/crangon)

Aquaculture counting machine with very simple methodology, designed to be cheap and affordable for entry-level farms with limited budget

Hardware
---

- small-size SBC like Raspberry zero
- LCD display (touch screen would be preferable)
- CSI camera with decent resolution

How it works
---

The following graph explain a process of program

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  ┌────┐     ┌────────────┐     ┌────────┐     ┌──────┐  │
└─►│Idle├────►│Take picture├────►│counting├────►│result├──┘
   └────┘     └────────────┘     └────────┘     └──────┘
```

Initially, when machine finished booting it will be set to `idle` mode and wait for only 2 input is `capture` and `reset`

LICENSE
---

This project is under [BSD 3-Clause License](https://github.com/binarybadgr/caramote/blob/master/LICENSE)
