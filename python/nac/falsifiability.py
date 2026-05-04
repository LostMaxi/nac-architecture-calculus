"""Falsifiability conditions + Partial Viability per § 21."""

from dataclasses import dataclass

from nac.axioms import check_all_axioms
from nac.scoring import Architecture


@dataclass(frozen=True)
class FalsifiabilityCondition:
    nac_element: str
    condition: str
    verification_path: str


_CONDITIONS: dict[str, list[FalsifiabilityCondition]] = {
    "A_1": [
        FalsifiabilityCondition(
            nac_element="A_1",
            condition="An architecture with σ = 1.0 sustains stable operation ≥ 10 years without self-deception",
            verification_path="Catalogue 100+ architectures with σ history; check upper bound",
        ),
    ],
    "A_2": [
        FalsifiabilityCondition(
            nac_element="A_2",
            condition="An architecture with G fully covering arch sustains evolutionary capacity ≥ N rounds",
            verification_path="Apply Kolmogorov / entropy estimators; track plasticity",
        ),
    ],
    "A_3": [
        FalsifiabilityCondition(
            nac_element="A_3",
            condition="A long-running (≥ 5 years) architecture demonstrably built target-first shows no structural backlash",
            verification_path="Sample N target-first vs N arch-first projects; compare 5-year survival",
        ),
    ],
    "Sp": [
        FalsifiabilityCondition(
            nac_element="Sp",
            condition="A specialization sequence shows gradual basis-set drift without any Ev event",
            verification_path="Define basis-set identity; trace specialization sequences",
        ),
    ],
    "Ev": [
        FalsifiabilityCondition(
            nac_element="Ev",
            condition="Substrate evolution successfully completed without preceding saturation",
            verification_path="Track saturation predicate + σ-trajectory across architecture histories",
        ),
    ],
    "Phi": [
        FalsifiabilityCondition(
            nac_element="Phi",
            condition="An object class admits no consistent substrate representation while still being meaningful as architecture",
            verification_path="Probe Φ on physical / digital / abstract / chemical objects",
        ),
    ],
    "sigma_min": [
        FalsifiabilityCondition(
            nac_element="sigma_min",
            condition="Averaging or weighted-sum aggregation predicts long-term outcomes more accurately than min()",
            verification_path="Catalogue case histories; rank by min vs avg; correlate with outcomes",
        ),
    ],
    "SelfIncompleteness": [
        FalsifiabilityCondition(
            nac_element="SelfIncompleteness",
            condition="A constructive proof of NAC version completeness within the same formal language",
            verification_path="Formal verification in a proof assistant (Coq / Lean)",
        ),
    ],
    "epsilon": [
        FalsifiabilityCondition(
            nac_element="epsilon",
            condition="A stable system with ε = 0 sustained for cosmologically meaningful duration (≥ 10⁹ years)",
            verification_path="Cross-domain ε survey; long-term stability correlation",
        ),
    ],
}


def get_falsifiability_conditions(nac_element: str) -> list[FalsifiabilityCondition]:
    """Return falsifiability conditions for a NAC element. Empty list if unknown."""
    return list(_CONDITIONS.get(nac_element, []))


def partial_viability(
    arch: Architecture,
    weights: dict[str, float] | None = None,
) -> float:
    """
    Compute partial viability score PV(arch) ∈ [0, 1] per § 21.2.

    PV = Σ c_i · 𝟙[condition_i holds]   ,   Σ c_i = 1

    Default weights are equal across the three foundational axioms (A_1, A_2,
    A_3). Domain-specific weight schemes are deployment-internal.

    Constraint: A_1 violation always returns PV = 0, regardless of other
    conditions. A_1 (Honesty Cap) is non-negotiable per § 21.2.
    """
    if weights is None:
        weights = {"A_1": 1 / 3, "A_2": 1 / 3, "A_3": 1 / 3}

    total = sum(weights.values())
    if not (0.999 <= total <= 1.001):
        raise ValueError(f"weights must sum to 1.0, got {total}")

    results = {r.axiom.split()[0]: r.holds for r in check_all_axioms(arch)}
    a1_passes = results.get("A_1", False)

    if not a1_passes:
        return 0.0  # A_1 hard constraint per § 21.2

    pv = 0.0
    for axiom_key, weight in weights.items():
        if results.get(axiom_key, False):
            pv += weight
    return pv
