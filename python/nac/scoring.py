"""Scoring · σ = min(SHER) per § 4."""

from dataclasses import dataclass, field
from typing import Optional

from nac.parameters import NAC_DEFAULT_EPSILON, validate_epsilon


@dataclass
class SHER:
    """
    SHER 4-dimensional scoring components.

    H is human-reserved (∂-axiom). AI Agents MUST NOT self-evaluate H.
    Setting H from inside an automated pipeline is a discipline violation.
    """

    S: float  # Structural resilience · AI-evaluable
    H: Optional[float]  # Cognitive Honesty · MUST be human-judged
    E: float  # Evolutionary plasticity · AI-evaluable
    R: float  # Relevance · AI-evaluable

    def __post_init__(self) -> None:
        for label, val in [("S", self.S), ("E", self.E), ("R", self.R)]:
            if not 0.0 <= val <= 1.0:
                raise ValueError(f"{label} must be in [0, 1], got {val}")
        if self.H is not None and not 0.0 <= self.H <= 1.0:
            raise ValueError(f"H must be None or in [0, 1], got {self.H}")


def sigma(sher: SHER) -> float:
    """
    Compute σ = min(S, H, E, R).

    Raises ValueError if H is None — H must be filled by a human evaluator
    before σ can be computed. This enforces the ∂-axiom at the type level.
    """
    if sher.H is None:
        raise ValueError(
            "σ cannot be computed: H is None. "
            "H is human-reserved (∂-axiom); fill H via human evaluation first."
        )
    return min(sher.S, sher.H, sher.E, sher.R)


@dataclass
class Architecture:
    """
    Public-interface architecture record.

    This dataclass deliberately does NOT model:
      - basis-set members (M, C, T concrete cardinality and naming)
      - sub-step structure of the AI Ingest Protocol
      - any specific deploying system's internal artifacts

    These are deployment-internal per § 2 / § 11 / § 16. Implementers must
    grow their own internal substrate and only summarize axiom-relevant
    properties here.
    """

    name: str
    sher: SHER
    epsilon: float = NAC_DEFAULT_EPSILON.epsilon
    arch_first_ordering: bool = True
    has_unmodeled_subspace: bool = True
    governance_fully_covers: bool = False
    notes: str = ""
    extras: dict = field(default_factory=dict)

    def __post_init__(self) -> None:
        validate_epsilon(self.epsilon)

    @property
    def survival_score(self) -> float:
        """σ(arch) = min(SHER). Raises if H not yet human-judged."""
        return sigma(self.sher)

    @property
    def honesty_cap(self) -> float:
        """1 − ε. The maximum σ allowed by A_1."""
        return 1.0 - self.epsilon
