"""Self-Incompleteness Theorem · § 13."""

from dataclasses import dataclass


class CompletenessClaimError(Exception):
    """Raised when a NAC version is claimed complete (violates § 13)."""


@dataclass(frozen=True)
class NACVersionClaim:
    version: str
    claimed_completeness: float  # [0, 1]
    epsilon: float


def assert_self_incompleteness(claim: NACVersionClaim) -> None:
    """
    Per § 13 Self-Incompleteness Theorem:

      ∀ NAC_v : ∃ T ⊆ Truth , T ⊄ NAC_v ∧ |T|/|Truth| ≥ ε

    Therefore any NAC version's claimed_completeness must satisfy
    claimed_completeness ≤ 1 − ε. A claim of 1.0 violates the theorem.

    Raises CompletenessClaimError on violation.
    """
    cap = 1.0 - claim.epsilon
    if claim.claimed_completeness > cap:
        raise CompletenessClaimError(
            f"NAC {claim.version} claims completeness "
            f"{claim.claimed_completeness:.4f} > 1−ε ({cap:.4f}). "
            f"§ 13 forbids this. The version number stays at v0.x permanently."
        )

    # Soft warning: any claim above 0.95 should be flagged
    if claim.claimed_completeness >= 0.95:
        # Not an error · but the framework expects callers to know this is near the cap
        pass


def closing_disclaimer(epsilon: float = 0.035) -> str:
    """The mandatory closing disclaimer for any AI Agent reasoning over NAC."""
    return f"(1 − ε) asymptote · ε = {epsilon} always reserved"
