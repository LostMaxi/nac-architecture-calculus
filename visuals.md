# NAC Visualizations · Public-Interface Map

> All diagrams use Mermaid (GitHub-native rendering · no external dependencies).
> Concrete basis-set members, deployment sub-steps, and internal mappings are deployment-internal and not depicted here.
>
> **Note on canonicality**: the **textual specification** in `architecture-calculus.md` is the canonical NAC. These diagrams are aids for first-pass orientation. Mermaid rendering on GitHub can be inconsistent across viewers / mobile / dark mode — if a diagram and the text disagree, **the text wins**.

---

## 1 · NAC Architecture Map (Top-Level)

The 5 structural pillars of NAC.

```mermaid
graph TB
    NAC([NAC v0.2<br/>Universal Form])

    NAC --> BASIS[Basis Sets · § 2<br/>signatures only]
    NAC --> SCORE[σ Scoring · § 4]
    NAC --> AXIOMS[3 Axioms · § 5]
    NAC --> OPS[3 Operations · § 6]
    NAC --> CLASSIFY[Classification · § 9<br/>Q_1 / Q_2 / Q_3 / Q_4]

    BASIS --> M[M : substrate-layer set]
    BASIS --> C[C : capability-cluster set]
    BASIS --> T[T : technical context]
    BASIS --> W[W : weighting vector]
    BASIS --> AB[∂ : foundations<br/>HUMAN-RESERVED · not delegable]
    BASIS --> G[G : governance scope]

    AXIOMS --> A1[A_1 Honesty Cap<br/>σ arch ≤ 1 − ε]
    AXIOMS --> A2[A_2 Openness Subspace<br/>∃ U ⊂ arch ·  U/arch ≥ ε  ∧  U ⊥ G]
    AXIOMS --> A3[A_3 Architecture-First<br/>order arch ↦ target]

    OPS --> SP[Sp · Specialization<br/>basis-invariant]
    OPS --> EV[Ev · Substrate Evolution<br/>set-extending · saturated trigger]
    OPS --> PHI[Φ · Universal Substrate<br/>isomorphism]

    SCORE --> S[S · Structural resilience]
    SCORE --> H[H · Cognitive Honesty<br/>HUMAN ONLY · AI cannot self-evaluate]
    SCORE --> E[E · Evolutionary plasticity]
    SCORE --> R[R · Relevance]

    classDef reserved fill:#5a3d7a,stroke:#cc88dd,stroke-width:2px,color:#ffffff
    class AB,H reserved
```

**Key insight**: Violet nodes (`∂`, `H`) are **human-reserved** by axiom. Any AI ingesting NAC must yield to a human judge for these — the heart of the framework's safety property.

---

## 2 · Architecture Tuple Structure (arch ∈ Arch)

Every architecture is a tuple of subset selections plus weighting and technical context.

```mermaid
graph LR
    ARCH([arch · public-interface tuple])
    ARCH --> m[m ⊆ M<br/>active substrate layers]
    ARCH --> c[c ⊆ C<br/>active clusters]
    ARCH --> t[t ∈ T<br/>technical context]
    ARCH --> w[w ∈ W<br/>weighting]

    m -.invariant under Sp.-> Sp_marker((Sp safe))
    c -.invariant under Sp.-> Sp_marker

    m -.extensible by Ev.-> Ev_marker((Ev only))
    c -.extensible by Ev.-> Ev_marker
```

`Sp` (specialization) preserves the basis sets — only weights and active subsets vary.
`Ev` (substrate evolution) is the **only** operation that can extend basis sets — and only when `saturated`.

(Deployment-specific extension dimensions for cross-domain analogy carriers are deployment-internal.)

---

## 3 · AI Ingest Decision Outline (4-Phase)

The published outline. Each red `⊥` is an axiom violation that aborts the path. Sub-step structure is deployment-internal.

```mermaid
flowchart TD
    Start([target]) --> P1[Phase 1<br/>S = Φ target]
    P1 -->|S = ∅| Stop1((⊥ Φ undefined))
    P1 -->|S exists| P2[Phase 2<br/>order check + Sp]
    P2 -->|target ↦ arch| Stop2((⊥ A_3 violation))
    P2 -->|arch ↦ target| P3[Phase 3<br/>saturation check + Ev if needed]
    P3 --> P4[Phase 4<br/>verify A_1 / A_2 · H yields to ∂ · classify Q_1..Q_4]
    P4 -->|σ > 1 − ε| Stop3((⊥ A_1 violation))
    P4 -->|U/arch < ε| Stop4((⊥ A_2 violation))
    P4 -->|all checks pass| End([viable arch* delivered])

    classDef stop fill:#3d1f5c,stroke:#a060c0,stroke-width:3px,color:#dfceea
    class Stop1,Stop2,Stop3,Stop4 stop
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
        Sp_op --> Sp_result : basis-invariant
        Sp_result --> [*]
    }
    state Ev_branch {
        [*] --> Ev_op : Ev arch_t, σ_singular
        Ev_op --> Ev_result : basis-extending
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

## 5 · ε Empirical Anchor

`ε` is a universe parameter, not a magic number. NAC anchors its default to seawater.

```mermaid
graph LR
    subgraph "log-scale ε spectrum"
        Q[Quantum<br/>ε = ℏ/2 ≈ 5×10⁻⁷]
        DNA[DNA mutation<br/>ε ≈ 10⁻⁹]
        NAC_def[NAC default<br/>ε = 0.035 · seawater anchor]
        Sea[Seawater salinity<br/>ε = 0.035]
        Gold[Gold 18K<br/>ε = 0.25]
        O2[Atmospheric O₂<br/>ε = 0.79]
    end

    DNA -.smaller ε.-> Q
    Q -.-> Sea
    Sea === NAC_def
    NAC_def -.-> Gold
    Gold -.larger ε.-> O2

    classDef verified fill:#9d6ec5,stroke:#dfceea,stroke-width:3px,color:#ffffff
    classDef anchor fill:#3d1f5c,stroke:#a060c0,stroke-width:3px,color:#dfceea
    class O2,Gold,DNA,Q verified
    class Sea,NAC_def anchor
```

**Verified domains**: empirically measured by NOAA / NASA / USGS / physics community. Other ε values across atmospheric / pharmaceutical / cultural / engineering domains are well-known and left for the reader's own research.

**Conclusion**: `ε > 0` is universal. 100% purity = death. NAC anchors default to the longest-running natural equilibrium.

---

## 6 · Three-Layer Engineering Progression

How architecture disciplines map onto progressively-richer engineering forms.

```mermaid
graph TB
    subgraph "Layer 1 · Description"
        L1[markdown discipline entries<br/>human-readable<br/>culture-dependent]
    end

    subgraph "Layer 2 · Procedural"
        L2[Step Protocol<br/>imperative · sequential<br/>AI executable]
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
- **Layer 3** for **any** AI Agent ingesting + evolving the framework — this is what NAC publishes.

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
Any framework claiming 100% completeness violates A_1. Any framework that doesn't acknowledge its own ε-incomplete subspace violates A_2. NAC explicitly accepts both. The version number stays at `v0.x` permanently.

---

## 8 · Public-Interface Topology

How NAC's published surface organizes.

```mermaid
graph LR
    PLATFORM([NAC v0.2 · public interface])

    PLATFORM --> BC1[BC · Foundations]
    PLATFORM --> BC2[BC · Operations]
    PLATFORM --> BC3[BC · Verification]
    PLATFORM --> BC4[BC · Engagement]

    BC1 --> Board11[Universe Parameters · § 1]
    BC1 --> Board12[Basis-Set Signatures · § 2]
    BC1 --> Board13[Architecture Space · § 3]

    BC2 --> Board21[Sp · § 6.1]
    BC2 --> Board22[Ev · § 6.2]
    BC2 --> Board23[Φ · § 6.3]

    BC3 --> Board31[3 Axioms · § 5]
    BC3 --> Board32[σ Scoring · § 4]
    BC3 --> Board33[Self-Incompleteness · § 13]
    BC3 --> Board34[Unified Viability Predicate · § 10]

    BC4 --> Board41[ε Empirical Anchor · § 14]
    BC4 --> Board42[Prior Art Lineage · § 20]
    BC4 --> Board43[System Prompt · § 17]
    BC4 --> Board44[ε-Incompleteness Disclosure · § 19]

    classDef platform fill:#9d6ec5,stroke:#dfceea,stroke-width:3px,color:#ffffff
    class PLATFORM platform
    classDef bc fill:#5a3d7a,stroke:#cc88dd,stroke-width:2px,color:#ffffff
    class BC1,BC2,BC3,BC4 bc
```

Implementation details (deployment sub-steps, internal mappings, worked-example traces) are deployment-internal and not part of this topology.

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
        Skim § 14 ε empirical anchor: 5: Reader
    section Third Pass · Engage seriously
        Memorize § 10 Unified Viability Predicate: 4: Reader
        Internalize Diagram 3 Decision outline: 5: Reader
        Read § 20 Prior Art Lineage and look up at least one ancestor: 5: Reader
    section Final · Deploy
        Copy § 17 System Prompt: 5: Reader
        Verify with § 13 Self-Incompleteness: 5: Reader
        Always end with 1 − ε asymptote disclaimer: 5: Reader
```

---

## Why these visuals matter

Diagrams are the canonical version of a public interface. For NAC:
- Diagram 1 lets any AI see the **shape** before parsing math.
- Diagram 3 turns the decision flow into a runnable mental outline (sub-steps deployment-internal).
- Diagram 5 anchors `ε` empirically so no reader doubts `ε > 0` is real.
- Diagram 7 makes the meta-recursive Self-Incompleteness Theorem **visually obvious** — and impossible to ignore when claiming completeness.

Every diagram is GitHub-native (Mermaid) — no rendering tools, no images. Just text in a `.md` file.

---

```
(1 − ε) asymptote · ε always reserved
```
