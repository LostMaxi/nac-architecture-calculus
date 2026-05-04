# NAC Visualizations · Hierarchical Knowledge Map

> Built using the **architect-vision toolkit** logic — visual-first, hierarchical, AI-ingestible diagrams.
> All diagrams use Mermaid (GitHub-native rendering · no external dependencies).

---

## 1 · NAC Architecture Map (Top-Level)

The 5 structural pillars of NAC and how they relate.

```mermaid
graph TB
    NAC([NAC v0.2<br/>Universal Form])

    NAC --> BASIS[Basis Sets · § 2]
    NAC --> SCORE[σ Scoring · § 4]
    NAC --> AXIOMS[3 Axioms · § 5]
    NAC --> OPS[3 Operations · § 6]
    NAC --> CLASSIFY[Classification · § 9<br/>Q_1 / Q_2 / Q_3 / Q_4]

    BASIS --> M[M : meta-layers · 5-set]
    BASIS --> C[C : clusters · 5-set]
    BASIS --> A[A : 4 axes]
    BASIS --> F[F : fire-seeds · n-set]
    BASIS --> W[W : aesthetic weights · Σ=1]
    BASIS --> AB[∂ : foundations<br/>HUMAN-RESERVED · not delegable]
    BASIS --> G[G : governance scope]

    AXIOMS --> A1[A_1 Honesty Cap<br/>σ arch ≤ 1 − ε]
    AXIOMS --> A2[A_2 Openness Subspace<br/>∃ U ⊂ arch ·  U/arch ≥ ε  ∧  U ⊥ G]
    AXIOMS --> A3[A_3 Architecture-First<br/>order arch ↦ target]

    OPS --> SP[Sp · Specialization<br/>substrate-invariant]
    OPS --> EV[Ev · Substrate Evolution<br/>set-extending · trigger saturated]
    OPS --> PHI[Φ · Universal Substrate<br/>iso physical/digital/abstract/chemical]

    SCORE --> S[S · Structural resilience]
    SCORE --> H[H · Cognitive Honesty<br/>HUMAN ONLY · AI cannot self-evaluate]
    SCORE --> E[E · Evolutionary plasticity]
    SCORE --> R[R · Relevance]

    classDef reserved fill:#5a3d7a,stroke:#cc88dd,stroke-width:2px,color:#ffffff
    class AB,H reserved
```

**Key insight**: Pink nodes (`∂`, `H`) are **human-reserved** by axiom. Any AI ingesting NAC must yield to a human judge for these — this is the heart of the framework's safety property.

---

## 2 · Architecture Tuple Structure (arch ∈ Arch)

Every architecture is a 5-tuple. This is what an AI Agent reads / writes / evolves.

```mermaid
graph LR
    ARCH([arch · 5-tuple])
    ARCH --> m[m ⊆ M<br/>active meta-layers]
    ARCH --> c[c ⊆ C<br/>active clusters]
    ARCH --> t[t ∈ T<br/>technical stack]
    ARCH --> f[f ⊆ F<br/>active fire-seeds]
    ARCH --> w[w ∈ W<br/>aesthetic weights]

    m -.invariant under Sp.-> Sp_marker((Sp safe))
    c -.invariant under Sp.-> Sp_marker
    f -.invariant under Sp.-> Sp_marker

    m -.extensible by Ev.-> Ev_marker((Ev only))
    c -.extensible by Ev.-> Ev_marker
    f -.extensible by Ev.-> Ev_marker
```

`Sp` (specialization) keeps `M, C, F` unchanged — only weights and active subsets vary.
`Ev` (substrate evolution) is the **only** operation that can extend these basis sets — and only when `saturated`.

---

## 3 · AI Ingest Decision Tree (10-Step Protocol)

Any AI Agent, on receiving a target, follows this decision tree. Each red `⊥` is an axiom violation that aborts the path.

```mermaid
flowchart TD
    Start([target]) --> S1[1 · S = Φ target]
    S1 -->|S = ∅| Stop1((⊥ Φ undefined))
    S1 -->|S exists| S2{2 · order check<br/>target ↦ arch?}
    S2 -->|yes| Stop2((⊥ A_3 violation<br/>Architecture-First))
    S2 -->|no| S3[3 · arch_new = Sp arch_cur, target]
    S3 --> S4{4 · saturated for<br/>≥ N rounds with δ?}
    S4 -->|yes| S4b[arch_new = Ev arch_cur, σ_singular]
    S4 -->|no| S5[5 · σ_new = min S, H, E, R<br/>H requires HUMAN]
    S4b --> S5
    S5 --> S6{6 · σ_new ≤ 1 − ε?}
    S6 -->|no| Stop3((⊥ A_1 violation<br/>Honesty Cap))
    S6 -->|yes| S7{7 · ∃ U ⊂ arch<br/>U/arch ≥ ε?}
    S7 -->|no| Stop4((⊥ A_2 violation<br/>Openness))
    S7 -->|yes| S8{8 · craft ∧ structure ∧ discipline?}
    S8 -->|no| Stop5((⊥ CARGO CULT ALERT))
    S8 -->|yes| S9[9 · classify → Q_1-Q_4]
    S9 --> S10[10 · return arch_new, q]
    S10 --> End([viable arch* delivered])

    classDef stop fill:#3d1f5c,stroke:#a060c0,stroke-width:3px,color:#dfceea
    class Stop1,Stop2,Stop3,Stop4,Stop5 stop
    classDef pass fill:#7a4da0,stroke:#a78bfa,stroke-width:3px,color:#ffffff
    class End pass
```

---

## 4 · Evolution Dynamics (Time-Stepped)

The `Sp / Ev` switch controls how architecture moves through `Arch` space over time.

```mermaid
stateDiagram-v2
    [*] --> arch_t : initial
    arch_t --> sat_check : at each goal arrival
    sat_check --> Sp_branch : ¬saturated
    sat_check --> Ev_branch : saturated for ≥ N rounds

    state Sp_branch {
        [*] --> Sp_op : Sp arch_t, goal_t
        Sp_op --> Sp_result : substrate-invariant
        Sp_result --> [*]
    }
    state Ev_branch {
        [*] --> Ev_op : Ev arch_t, σ_singular
        Ev_op --> Ev_result : substrate-extending
        Ev_result --> [*]
    }

    Sp_branch --> arch_t1 : continue specialization
    Ev_branch --> arch_t1 : substrate jump

    arch_t1 --> arch_t : t := t + 1

    note right of Ev_branch
        Triggered only when
        specialization saturates
        - common case is Sp
        - rare jumps are Ev
    end note
```

---

## 5 · ε Empirical Examples (Cross-Domain)

`ε` is a universe parameter, not a magic number. Each domain selects its own `ε` via natural / engineering pressure.

```mermaid
graph LR
    subgraph "log-scale ε spectrum"
        Q[Quantum<br/>ε = ℏ/2 ≈ 5×10⁻⁷]
        DNA[DNA mutation<br/>ε ≈ 10⁻⁹]
        Persian[Persian rug<br/>ε ≈ 0.01]
        Drug[Pharma USP<br/>ε = 0.05]
        NAC_def[NAC default<br/>ε = 0.035 · seawater anchor]
        Sea[Seawater salinity<br/>ε = 0.035]
        Wabi[Wabi-sabi<br/>ε ≈ 0.05-0.15]
        Wood[Wood furniture<br/>ε ≈ 0.10]
        Gold[Gold 18K<br/>ε = 0.25]
        O2[Atmospheric O₂<br/>ε = 0.79]
    end

    DNA -.smaller ε.-> Q
    Q -.-> Persian
    Persian -.-> Sea
    Sea === NAC_def
    NAC_def -.-> Drug
    Drug -.-> Wabi
    Wabi -.-> Wood
    Wood -.-> Gold
    Gold -.larger ε.-> O2

    classDef verified fill:#9d6ec5,stroke:#dfceea,stroke-width:3px,color:#ffffff
    classDef anchor fill:#3d1f5c,stroke:#a060c0,stroke-width:3px,color:#dfceea
    class O2,Gold,DNA,Q verified
    class Sea,NAC_def anchor
```

**Verified domains** (blue): empirically measured by NOAA / NASA / USGS / physics community / etc.

**Conclusion**: `ε > 0` is universal. 100% purity = death (burn / break / dissolve / extinct). Every viable system has its own `ε`.

---

## 6 · Three-Layer Engineering Progression

How NDB-Architect-Agent disciplines map onto progressively-richer engineering forms.

```mermaid
graph TB
    subgraph "Layer 1 · Description"
        L1[markdown ML-XX entries<br/>human-readable<br/>culture-dependent]
    end

    subgraph "Layer 2 · Procedural"
        L2[8-step Protocol<br/>imperative · sequential<br/>AI executable]
    end

    subgraph "Layer 3 · Mathematical"
        L3[NAC v0.2<br/>declarative · parallel<br/>ANY AI ingestible<br/>cross-language]
    end

    L1 -->|distill into protocol| L2
    L2 -->|formalize into calculus| L3
    L3 -.->|self-reference via § 13| L3_meta((Self-Incompleteness<br/>NAC ε-incomplete))

    classDef richest fill:#9d6ec5,stroke:#dfceea,stroke-width:3px,color:#ffffff
    class L3 richest
```

Each layer serves a different audience.
- **Layer 1** for humans documenting tacit knowledge.
- **Layer 2** for AI Agents executing decision flows.
- **Layer 3** for **any** AI Agent ingesting + evolving the framework — this is what NAC delivers.

---

## 7 · Self-Incompleteness Theorem (Meta-Recursive)

NAC applies its own openness axiom to itself.

```mermaid
graph TB
    NAC_v([NAC_v · any version])
    NAC_v -->|NAC is itself an arch ∈ Arch| Self_arch[NAC_v ∈ Arch]
    Self_arch -->|apply A_2 to NAC_v| Open[∃ U ⊂ NAC_v<br/>|U|/|NAC_v| ≥ ε<br/>U ⊥ G_NAC]
    Open --> Truth[T = U is unmodeled truth]
    Truth -->|T ⊄ NAC_v| Theorem[Theorem · § 13<br/>NAC always 1 − ε asymptote<br/>ε-incomplete forever]

    Theorem -.->|next release| NAC_v_next([NAC_v+1])
    NAC_v_next -.-|same theorem still holds| Theorem

    classDef axiom fill:#5a3d7a,stroke:#cc88dd,stroke-width:2px,color:#ffffff
    class Open axiom
    classDef self fill:#3d1f5c,stroke:#a060c0,stroke-width:3px,color:#dfceea
    class Theorem self
```

**This is NAC's analogue of Gödel's Second Incompleteness Theorem applied to architecture.**
Any framework claiming to be 100% complete violates A_1. Any framework that doesn't acknowledge its own ε-incomplete subspace violates A_2.
NAC explicitly accepts both. The version number stays at `v0.x` permanently.

---

## 8 · Hierarchical Knowledge Map (Platform → BC → Board)

Mapping NAC into the **architect-vision toolkit** structure (Platform = NAC framework, BC = bounded contexts, Board = leaf concepts).

```mermaid
graph LR
    PLATFORM([Platform · NAC v0.2])

    PLATFORM --> BC1[BC · Foundations]
    PLATFORM --> BC2[BC · Operations]
    PLATFORM --> BC3[BC · Verification]
    PLATFORM --> BC4[BC · Deployment]

    BC1 --> Board11[Universe Parameters · § 1]
    BC1 --> Board12[Basis Sets · § 2]
    BC1 --> Board13[Architecture Space · § 3]

    BC2 --> Board21[Sp Specialization · § 6.1]
    BC2 --> Board22[Ev Substrate Evolution · § 6.2]
    BC2 --> Board23[Φ Universal Substrate · § 6.3]
    BC2 --> Board24[Saturation + Dynamics · § 7-8]

    BC3 --> Board31[3 Axioms · § 5]
    BC3 --> Board32[σ Scoring · § 4]
    BC3 --> Board33[Self-Incompleteness Theorem · § 13]
    BC3 --> Board34[Unified Viability Predicate · § 10]

    BC4 --> Board41[AI Ingest Protocol · § 11]
    BC4 --> Board42[Self-Evolution Function · § 12]
    BC4 --> Board43[ε Empirical Examples · § 14]
    BC4 --> Board44[Worked Examples · § 15]
    BC4 --> Board45[System Prompt for AI · § 17]

    classDef platform fill:#9d6ec5,stroke:#dfceea,stroke-width:3px,color:#ffffff
    class PLATFORM platform
    classDef bc fill:#5a3d7a,stroke:#cc88dd,stroke-width:2px,color:#ffffff
    class BC1,BC2,BC3,BC4 bc
```

---

## 9 · Reading Order for Newcomers

```mermaid
journey
    title Recommended NAC Learning Path
    section First Pass · Get the gist
        Read README intro: 5: Reader
        Skim Diagram 1 NAC overview: 5: Reader
        Read Diagram 6 Three-layer progression: 5: Reader
    section Second Pass · Get the math
        Read § 1-4 Universe / Basis / Arch / σ: 4: Reader
        Read § 5 Three Axioms: 4: Reader
        Skim § 14 ε empirical examples: 5: Reader
    section Third Pass · Use it
        Memorize § 10 Unified Viability Predicate: 4: Reader
        Internalize Diagram 3 Decision tree: 5: Reader
        Walk through § 15 Worked Examples: 4: Reader
    section Final · Deploy to AI
        Copy § 17 System Prompt: 5: Reader
        Verify with § 13 Self-Incompleteness: 5: Reader
        Always end with 1 − ε asymptote disclaimer: 5: Reader
```

---

## Why these visuals matter

The **architect-vision toolkit** principle is *Architecture-as-Truth* — diagrams are the canonical version of the system, not text descriptions.

For NAC specifically:
- Diagram 1 lets any AI immediately see the **shape** of the framework before parsing math.
- Diagram 3 turns the 10-step protocol into a runnable mental flowchart.
- Diagram 5 anchors `ε` empirically across 10 domains so no reader doubts whether `ε > 0` is real.
- Diagram 7 makes the meta-recursive Self-Incompleteness Theorem **visually obvious** — and impossible to ignore when claiming completeness.

Every diagram is GitHub-native (Mermaid) — no rendering tools, no images, no LFS. Just text in a `.md` file.

---

```
(1 − ε) asymptote · ε always reserved
```
