# nac-calculus · Python toolkit for NAC v0.2

Signature-only Python implementation of the public-interface axioms,
scoring, falsifiability, and self-incompleteness mechanics from
[NAC v0.2 Universal Form](../architecture-calculus.md).

## What this package is

- A minimal, dependency-free Python library that lets any AI Agent or
  engineer **verify** an architecture against NAC's public axioms.
- A reference for what NAC's signatures look like in code (so other
  AI Agents reading NAC don't need to invent the API).
- A runnable Sagrada Família example (per § 25).

## What this package is NOT

- Not a deployment kit. Concrete basis-set members (M, C, T internals),
  sub-step structure of the AI Ingest Protocol, and per-deployment
  artifact mappings are **NOT** in this package, by design (per § 16).
- Not an opinion about which target your architecture should serve.
  NAC is a gravitational field for evolution, not a standard.

## Install (when published to PyPI)

```bash
pip install nac-calculus
```

## Local install for development

```bash
cd python
pip install -e ".[dev]"
pytest
```

## Quick example

```python
from nac import SHER, Architecture, check_all_axioms, partial_viability

arch = Architecture(
    name="my_system",
    sher=SHER(S=0.85, H=0.7, E=0.8, R=0.9),  # H must be human-judged
    epsilon=0.035,                            # NAC default · seawater anchor
    arch_first_ordering=True,
    has_unmodeled_subspace=True,
    governance_fully_covers=False,
)

for result in check_all_axioms(arch):
    print(result)

print(f"Partial Viability: {partial_viability(arch):.4f}")
```

Run the Sagrada Família case study:

```bash
python examples/sagrada.py
```

## What the API exposes

| Module | Purpose |
|---|---|
| `nac.parameters` | Empirical ε anchors (seawater, quantum, DNA, gold, O₂). Default = seawater 0.035. |
| `nac.scoring` | `SHER` and `Architecture` dataclasses; `sigma()` enforces H human-reservation. |
| `nac.axioms` | A_1 / A_2 / A_3 checks; `check_all_axioms()`; raises `AxiomViolation`. |
| `nac.falsifiability` | Per-element falsifiability conditions per § 21; `partial_viability()` per § 21.2. |
| `nac.incompleteness` | `assert_self_incompleteness()` per § 13; raises `CompletenessClaimError` on `claim ≥ 1−ε`. |

## Hard constraints encoded in code

1. **H is human-reserved** — `sigma()` raises if H is `None`. AI Agents
   cannot self-evaluate cognitive honesty.
2. **A_1 hard constraint** — `partial_viability()` returns `0.0` whenever
   A_1 fails, regardless of other axioms (per § 21.2).
3. **ε bounds** — `validate_epsilon()` rejects `ε < ε_quantum` and `ε > 0.50`.
4. **No completeness claim above 1−ε** — `assert_self_incompleteness()`
   raises if a NAC version claims completeness above the cap.

## License

[CC BY 4.0](../LICENSE)

## Source spec

The canonical NAC specification is in [`../architecture-calculus.md`](../architecture-calculus.md).
This Python package is a partial implementation of the public-interface
signatures only; deployment internals are deliberately omitted.

```
(1 − ε) asymptote · ε always reserved
```
