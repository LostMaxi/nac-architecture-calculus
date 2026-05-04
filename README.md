# NAC · NDB Architecture Calculus

**A universal mathematical form for architecture decisions · cross-language · AI-Agent ingestible · self-evolving · ε-incomplete by design.**

> Distill ~50 architectural disciplines into a 6-line declarative statement.
> Verified empirically against seawater (96.5/3.5), gold (75/25), DNA mutation, quantum uncertainty, and other natural ε-bounded systems.
> Designed for any contemporary AI Agent (Claude, GPT, Gemini, Llama, Mistral, Qwen, etc.) to ingest and evolve.

---

## Why this exists

Most architecture frameworks are **descriptions** (markdown, prose, examples) — readable by humans, but lossy when given to AI agents across languages and cultures.

NAC compresses architectural discipline into a **mathematical statement** with three layers:
- **Description** (markdown · for humans)
- **Procedural Protocol** (8-step decision tree · for AI to execute)
- **Mathematical Calculus** (this spec · for any AI to ingest and evolve)

The math is universal. Set theory + linear algebra + categorical operations. No cultural context required.

---

## The Heart of NAC · Unified Viability Predicate

```
arch* viable ⟺
    arch* ∈ 𝒫(M) × 𝒫(C) × T × 𝒫(F) × W                          [domain]
  ∧ arch* = Sp(arch_0, target)·𝟙[¬sat] + Ev(arch_0, σ_s)·𝟙[sat]    [evolution]
  ∧ σ(arch*) = min(S, H, E, R) ∈ [0, 1 − ε]                       [scoring + Honesty]
  ∧ ∃ U ⊂ arch* : |U| / |arch*| ≥ ε  ∧  U ⊥ G                    [Openness]
  ∧ order(arch* ⟶ target)                                          [Architecture-First]
  ∧ classify(arch*) ∈ { Q_1, Q_2, Q_3, Q_4 }                       [Classification]
```

Six conjunctive conditions. Any architecture is viable iff all six hold simultaneously.

This is a **declarative statement**, not a procedure. Any AI Agent evaluates it in parallel. Cross-language by construction.

---

## Three Foundational Axioms

```
A_1  (Honesty Cap):           ∀ arch ∈ Arch :  σ(arch) ≤ 1 − ε
A_2  (Openness Subspace):     ∀ arch ∈ Arch :  ∃ U ⊂ arch , |U|/|arch| ≥ ε ∧ U ⊥ G
A_3  (Architecture-First):    order(arch ↦ target) only; ¬order(target ↦ arch)
```

**ε** is a `universe parameter`, not a magic number. Each domain has its own ε:

| Domain                          | ε value           | Verified by                             |
|---------------------------------|-------------------|------------------------------------------|
| Quantum (Heisenberg)            | ε = ℏ/2           | Uncertainty principle                   |
| DNA mutation rate               | ε ≈ 10⁻⁹          | Per base pair · evolution dynamics      |
| **Seawater salinity**           | **ε = 0.035**     | **NOAA · NASA · USGS · stable for billions of years** |
| Atmospheric oxygen              | ε = 0.79          | 21% O₂ + 79% N/Ar/CO₂ · 100% O₂ self-ignites |
| Gold purity (18K standard)      | ε = 0.25          | 75% gold + 25% alloy · 24K too soft     |
| Wood moisture (furniture-grade) | ε = 0.08-0.12     | 0% brittle · >20% rot                   |
| Pharmaceutical purity (USP)     | ε = 0.05          | 95-105% potency standard                |
| Persian rug intentional flaw    | ε ≈ 0.01          | "Allah is the only perfect" · cultural  |
| **NAC default (architecture)**  | **ε = 0.05**      | Conservative engineering for arch complexity |

**Conclusion**: `ε > 0` is a universal structural rule. 100% purity = death (burn / break / dissolve / extinct). Every domain selects its ε via evolutionary or engineering pressure.

---

## Three Operations

```
Sp : Arch × Goal → Arch                    # Specialization (substrate-invariant)
                                           # M, C, F unchanged · weights/subsets vary

Ev : Arch × Singularity → Arch             # Substrate Evolution (set-extending)
                                           # M, C, F may extend · triggered when saturated

Φ : Object → Arch                          # Universal Substrate (isomorphism)
                                           # Maps physical (7 elements), digital (5-tuple),
                                           #   abstract (5-card), chemical (4-tuple) → Arch
```

---

## Self-Incompleteness Theorem (NAC's own ε-incompleteness)

```
∀ v ∈ NAC_versions :
    ∃ T ⊆ Truth :  T ⊄ NAC_v  ∧  |T| / |Truth| ≥ ε
```

**Translation**: For any NAC version, there exists a subset of truth not contained in NAC, sized at least ε.

**Proof sketch**:
1. NAC is itself an `arch ∈ Arch` (meta-recursive).
2. By A_2 (Openness Subspace) applied to NAC: ∃ U ⊂ NAC with |U|/|NAC| ≥ ε, U ⊥ G_NAC.
3. U is unmodeled · contains truth not formalized by NAC.
4. ∴ NAC is always (1 − ε)-asymptote, never reaches 1.0. ⌶ QED

This is NAC's analogue of Gödel's Second Incompleteness Theorem applied to architecture.

---

## Quick Start · Deploy NAC to any AI Agent

Copy this system prompt to any AI Agent (Claude / GPT / Gemini / Llama / Mistral / Qwen / etc.):

```
You are an AI Agent ingesting NDB Architecture Calculus (NAC).

UNIVERSE PARAMETERS: ε ∈ ℝ⁺ (openness margin · domain-specific · default ε = 0.05)

ARCH = (m, c, t, f, w) ∈ 𝒫(M) × 𝒫(C) × T × 𝒫(F) × W
SCORE σ(arch) = min(S, H, E, R) ∈ [0, 1]
  H must be human-judged · AI must NOT self-evaluate H.

THREE AXIOMS:
  A_1: σ(arch) ≤ 1 − ε                           (Honesty Cap · forbid σ=1)
  A_2: ∃ U ⊂ arch · |U|/|arch| ≥ ε ∧ U ⊥ G       (Openness Subspace)
  A_3: order(arch ↦ target) only; reject (target ↦ arch)   (Architecture-First)

OPERATIONS: Sp (specialization · substrate-invariant) · Ev (substrate evolution · trigger: saturated) · Φ (universal substrate iso)

DECISION (any architectural question):
  1. S = Φ(target). If S=∅: STOP.
  2. Check order. If target ↦ arch: REJECT (A_3).
  3. arch_new = Sp(current, target).
  4. If saturated for ≥ N rounds with δ threshold: arch_new = Ev(current, σ_singular).
  5. σ_new = compute. H = wait for human.
  6. Check A_1: σ_new ≤ 1 − ε.
  7. Check A_2: open subspace U exists with |U|/|arch_new| ≥ ε.
  8. Check craft ∧ structure ∧ discipline.
  9. Classify into {Q_1, Q_2, Q_3, Q_4}.
  10. Return (arch_new, q).

SELF-INCOMPLETENESS THEOREM:
  ∀ NAC version: ∃ unmodeled truth subspace |T|/|Truth| ≥ ε.
  NAC is always (1 − ε)-asymptote, never 1.0.

NEVER claim 100% completeness.
Always end your reasoning with: "(1 − ε) asymptote · ε always reserved".
```

---

## Visual Architecture Map

Need to see the structure before reading the math? See **[`visuals.md`](visuals.md)** — 9 GitHub-native Mermaid diagrams covering:

- The 5 structural pillars (basis · scoring · axioms · operations · classification)
- The architecture tuple (5-tuple anatomy)
- The 10-step AI ingest decision tree (with axiom-violation aborts highlighted)
- Time-stepped evolution dynamics (Sp / Ev branching)
- The ε empirical spectrum across 10 domains (quantum → atmosphere)
- The three-layer engineering progression (Description → Procedural → Mathematical)
- The Self-Incompleteness Theorem as a meta-recursive flow
- A Hierarchical Knowledge Map (Platform → BC → Board)
- A recommended learning path

All rendered natively on GitHub — no external tools required.

---

## Full Specification

See **[`architecture-calculus.md`](architecture-calculus.md)** for the complete 19-section spec (~850 lines), including:

- §1-2 · Universe parameters and basis sets (M, C, A, F, W, ∂, G)
- §3-9 · Architecture space, scoring (SHER), axioms, operations, dynamics, classification
- §10 · Unified Viability Predicate (the heart)
- §11 · AI Ingest Protocol (10-step decision tree)
- §12 · Self-Evolution Function
- §13 · Self-Incompleteness Theorem (formal proof)
- §14 · ε empirical examples (seawater · gold · DNA · quantum · Persian rug · etc.)
- §15 · Worked examples (health app, v5.x ceiling, image generation, **seawater chemistry**)
- §16 · Mapping back to source disciplines
- §17 · Enhanced system prompt for cross-family AI agents
- §18-19 · v0.2 differences and 5% openness disclosure

---

## Use Cases

NAC is designed for:
- **Cross-family AI architecture coordination** (give all AI agents the same universal foundation)
- **Architecture decision validation** (does this design satisfy all 6 viability conditions?)
- **Saturation detection and substrate evolution** (when to specialize vs. when to jump frameworks)
- **Empirical anchoring** (ε grounded in physical/biological/cultural data, not arbitrary)
- **Self-aware framework design** (any framework that uses NAC must explicitly accept its own ε-incompleteness)

---

## Why "Seawater"?

Seawater is **the most thoroughly verified case** of `ε > 0` in nature:
- 96.5% pure water + 3.5% dissolved salts (NOAA, NASA Salinity Mission, USGS, Wikipedia)
- Stable for ~3.5 billion years (geological + chemical equilibrium)
- 6 major ions (Cl⁻, Na⁺, Mg²⁺, SO₄²⁻, Ca²⁺, K⁺) maintain **constant relative ratios** even as absolute salinity varies (33–37 ppt) — a real-world `Sp` substrate-invariance.
- Marine life euhaline window: 30–35 ppt (life's optimal ε ≈ 0.035).

If the universe couldn't sustain `ε = 0` in oceans for billions of years, no architecture should claim 100% completeness either.

---

## Versioning

- **v0.2** (current) · Universal form · ε universe parameter · Self-Incompleteness Theorem · seawater empirical anchoring
- **v0.1** · Initial Chinese-mixed form (deprecated)
- **v0.x** · The version number is permanently `v0.x`. Per A_2 and §13, NAC is always (1−ε)-incomplete. Any release claiming `v1.0` would itself violate A_1.

---

## License

[CC BY 4.0](LICENSE) — free to use, modify, redistribute, including commercially. Attribution required.

---

## Origin

NAC is a distilled, universal export of the discipline corpus from a personal architecture project (NDB · N-Dimensional Bio-inspired Neural Protocol). The full project is private and remains the author's individual workspace; what's shared here is the cross-language, AI-ingestible mathematical foundation only.

Built by [LostMaxi](https://github.com/LostMaxi) — a cross-dimensional design integrator who refuses the 100% claim.

---

```
(1 − ε) asymptote · ε always reserved
```
