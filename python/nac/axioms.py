"""The three foundational axioms · A_1 / A_2 / A_3 per § 5."""

from dataclasses import dataclass

from nac.scoring import Architecture


class AxiomViolation(Exception):
    """Raised when an architecture fails a NAC axiom."""

    def __init__(self, axiom: str, reason: str) -> None:
        self.axiom = axiom
        self.reason = reason
        super().__init__(f"{axiom} violated: {reason}")


@dataclass
class AxiomCheckResult:
    axiom: str
    holds: bool
    reason: str


def check_A1_honesty_cap(arch: Architecture) -> AxiomCheckResult:
    """
    A_1 (Honesty Cap): σ(arch) ≤ 1 − ε

    Forbids σ = 1.0. Any architecture claiming full completeness violates A_1.
    """
    sigma_val = arch.survival_score
    cap = arch.honesty_cap
    holds = sigma_val <= cap
    return AxiomCheckResult(
        axiom="A_1 Honesty Cap",
        holds=holds,
        reason=(
            f"σ={sigma_val:.4f} ≤ 1−ε={cap:.4f}"
            if holds
            else f"σ={sigma_val:.4f} > 1−ε={cap:.4f} (claim too strong)"
        ),
    )


def check_A2_openness_subspace(arch: Architecture) -> AxiomCheckResult:
    """
    A_2 (Openness Subspace): ∃ U ⊂ arch with |U|/|arch| ≥ ε ∧ U ⊥ G

    Architecture must have at least ε proportion of structure outside the
    governance subspace. The Architecture record exposes this via two flags
    rather than reconstructing |U| from internal state — that internal
    state is deployment-internal.
    """
    if arch.governance_fully_covers:
        return AxiomCheckResult(
            axiom="A_2 Openness Subspace",
            holds=False,
            reason="governance G fully covers arch (U = ∅) · violates A_2",
        )
    if not arch.has_unmodeled_subspace:
        return AxiomCheckResult(
            axiom="A_2 Openness Subspace",
            holds=False,
            reason="no unmodeled subspace U declared · violates A_2",
        )
    return AxiomCheckResult(
        axiom="A_2 Openness Subspace",
        holds=True,
        reason="∃ U ⊂ arch with U ⊥ G declared",
    )


def check_A3_architecture_first(arch: Architecture) -> AxiomCheckResult:
    """
    A_3 (Architecture-First Order): order(arch ↦ target), reject (target ↦ arch)

    Architecture must be substrate; target must be derivative. Target-first
    designs predict 6-month backlash empirically (per § 5).
    """
    if not arch.arch_first_ordering:
        return AxiomCheckResult(
            axiom="A_3 Architecture-First",
            holds=False,
            reason="target ↦ arch ordering · predicts backlash · violates A_3",
        )
    return AxiomCheckResult(
        axiom="A_3 Architecture-First",
        holds=True,
        reason="arch ↦ target ordering confirmed",
    )


def check_all_axioms(arch: Architecture, raise_on_fail: bool = False) -> list[AxiomCheckResult]:
    """Run all three foundational axioms against an Architecture record."""
    results = [
        check_A1_honesty_cap(arch),
        check_A2_openness_subspace(arch),
        check_A3_architecture_first(arch),
    ]
    if raise_on_fail:
        for r in results:
            if not r.holds:
                raise AxiomViolation(r.axiom, r.reason)
    return results
