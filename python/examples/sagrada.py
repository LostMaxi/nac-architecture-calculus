"""
Sagrada Família case study (per § 25) · runnable example.

Reproduces the axiom-verification table from § 25.5. Does NOT model the
substrate-evolution timeline; per-deployment Sp/Ev tracking is internal.
Models only the public-interface axiom checks.
"""

from nac import (
    SHER,
    Architecture,
    NACVersionClaim,
    assert_self_incompleteness,
    check_all_axioms,
    partial_viability,
)
from nac.incompleteness import closing_disclaimer


def main() -> None:
    # SHER scoring per § 25.4 (independent estimate; H from human evaluator)
    sher = SHER(
        S=0.95,  # catenary structure survived 144 years incl. civil war
        H=0.85,  # placeholder · in real use H comes from foundation board / cultural authority
        E=0.92,  # substrate accommodated tool transitions and master-loss event
        R=0.97,  # UNESCO World Heritage; sustained civic mass for 140+ years
    )

    arch = Architecture(
        name="Sagrada Familia (1882-2030+)",
        sher=sher,
        epsilon=0.035,  # seawater anchor
        arch_first_ordering=True,
        has_unmodeled_subspace=True,
        governance_fully_covers=False,
        notes="Public verifiable case study per Section 25",
    )

    print(f"=== {arch.name} ===")
    print(f"sigma = min(SHER) = {arch.survival_score:.4f}")
    print(f"1 - epsilon       = {arch.honesty_cap:.4f}")
    print()

    print("Axiom checks:")
    for r in check_all_axioms(arch):
        mark = "PASS" if r.holds else "FAIL"
        print(f"  [{mark}] {r.axiom}: {r.reason}")
    print()

    pv = partial_viability(arch)
    print(f"Partial Viability: {pv:.4f}")
    print()

    claim = NACVersionClaim(
        version="v0.2", claimed_completeness=arch.survival_score, epsilon=0.035
    )
    assert_self_incompleteness(claim)
    print("Self-incompleteness check passed for NAC v0.2.")
    print()

    print(closing_disclaimer(arch.epsilon))


if __name__ == "__main__":
    main()
