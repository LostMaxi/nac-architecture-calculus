"""
nac-calculus · Python toolkit for NAC v0.2 Universal Form

Signature-only public interface. Concrete basis-set members, deployment
sub-steps, and internal mappings are deployment-internal and NOT
modeled in this package. Implementations must derive their own internal
substrate from the axioms in this module.

License: CC BY 4.0
Source spec: https://github.com/LostMaxi/nac-architecture-calculus
"""

from nac.parameters import (
    EPSILON_SEAWATER,
    EPSILON_QUANTUM,
    EPSILON_DNA,
    EPSILON_GOLD_18K,
    EPSILON_O2,
    NAC_DEFAULT_EPSILON,
    EmpiricalAnchor,
)
from nac.scoring import (
    Architecture,
    sigma,
    SHER,
)
from nac.axioms import (
    check_A1_honesty_cap,
    check_A2_openness_subspace,
    check_A3_architecture_first,
    check_all_axioms,
    AxiomViolation,
)
from nac.falsifiability import (
    FalsifiabilityCondition,
    get_falsifiability_conditions,
    partial_viability,
)
from nac.incompleteness import (
    assert_self_incompleteness,
    NACVersionClaim,
    CompletenessClaimError,
)

__version__ = "0.2.0"
__all__ = [
    "EPSILON_SEAWATER",
    "EPSILON_QUANTUM",
    "EPSILON_DNA",
    "EPSILON_GOLD_18K",
    "EPSILON_O2",
    "NAC_DEFAULT_EPSILON",
    "EmpiricalAnchor",
    "Architecture",
    "sigma",
    "SHER",
    "check_A1_honesty_cap",
    "check_A2_openness_subspace",
    "check_A3_architecture_first",
    "check_all_axioms",
    "AxiomViolation",
    "FalsifiabilityCondition",
    "get_falsifiability_conditions",
    "partial_viability",
    "assert_self_incompleteness",
    "NACVersionClaim",
    "CompletenessClaimError",
]
