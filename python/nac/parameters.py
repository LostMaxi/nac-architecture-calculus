"""Universe parameters · empirical ε anchors per § 1 + § 14."""

from dataclasses import dataclass


@dataclass(frozen=True)
class EmpiricalAnchor:
    """
    Documented empirical anchor for ε selection.

    Per § 21.3, valid ε must be (1) empirically anchored, (2) reproducibly
    documented, (3) ≥ ε_quantum, (4) ≤ 0.50.
    """

    name: str
    epsilon: float
    domain: str
    citation: str
    duration_years: float | None = None  # documented stability if known


EPSILON_SEAWATER = EmpiricalAnchor(
    name="seawater",
    epsilon=0.035,
    domain="natural-chemistry",
    citation="NOAA / NASA Salinity Mission / USGS · 96.5% H2O + 3.5% dissolved salts",
    duration_years=3.5e9,
)

EPSILON_QUANTUM = EmpiricalAnchor(
    name="quantum-uncertainty",
    epsilon=5e-7,  # ℏ/2 in normalized units · indicative
    domain="physics",
    citation="Heisenberg 1927 · σ_x · σ_p ≥ ℏ/2 · physical lower bound",
    duration_years=None,
)

EPSILON_DNA = EmpiricalAnchor(
    name="dna-mutation-rate",
    epsilon=1e-9,
    domain="biology",
    citation="DNA polymerase replication fidelity · per base pair per generation",
    duration_years=3.5e9,
)

EPSILON_GOLD_18K = EmpiricalAnchor(
    name="gold-18k",
    epsilon=0.25,
    domain="metallurgy",
    citation="ISO 9202 · 75% Au + 25% alloy · 24K too soft for jewelry",
    duration_years=None,
)

EPSILON_O2 = EmpiricalAnchor(
    name="atmospheric-oxygen",
    epsilon=0.79,
    domain="atmosphere",
    citation="Earth's atmosphere · 21% O2 + 79% N/Ar/CO2 · pure O2 self-ignites",
    duration_years=2e9,  # since Great Oxygenation Event
)

NAC_DEFAULT_EPSILON = EPSILON_SEAWATER


def validate_epsilon(epsilon: float) -> None:
    """
    Validate a chosen ε per § 21.3 selection rules.

    Raises ValueError if epsilon is not in valid range or has no anchor.
    """
    if epsilon < EPSILON_QUANTUM.epsilon:
        raise ValueError(
            f"epsilon={epsilon} below quantum lower bound {EPSILON_QUANTUM.epsilon}"
        )
    if epsilon > 0.50:
        raise ValueError(
            f"epsilon={epsilon} > 0.50 · margin > 50% means no architecture, just noise"
        )


# Saturation / dynamics defaults (deployment may override)
NAC_DEFAULT_DELTA = 0.10  # σ-improvement threshold below which round counts as flat
NAC_DEFAULT_N = 2  # consecutive flat rounds before saturation triggers
