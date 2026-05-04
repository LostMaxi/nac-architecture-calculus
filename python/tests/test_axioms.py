"""Test the public-interface axiom checks."""

import pytest

from nac import (
    SHER,
    Architecture,
    AxiomViolation,
    CompletenessClaimError,
    NACVersionClaim,
    NAC_DEFAULT_EPSILON,
    assert_self_incompleteness,
    check_A1_honesty_cap,
    check_A2_openness_subspace,
    check_A3_architecture_first,
    check_all_axioms,
    get_falsifiability_conditions,
    partial_viability,
    sigma,
)


def make_arch(
    S=0.85,
    H=0.7,
    E=0.8,
    R=0.9,
    epsilon=0.035,
    arch_first=True,
    has_unmodeled=True,
    g_covers=False,
):
    return Architecture(
        name="test_arch",
        sher=SHER(S=S, H=H, E=E, R=R),
        epsilon=epsilon,
        arch_first_ordering=arch_first,
        has_unmodeled_subspace=has_unmodeled,
        governance_fully_covers=g_covers,
    )


def test_sigma_is_minimum():
    s = SHER(S=0.85, H=0.7, E=0.8, R=0.9)
    assert sigma(s) == 0.7


def test_sigma_requires_human_H():
    s = SHER(S=0.85, H=None, E=0.8, R=0.9)
    with pytest.raises(ValueError, match="H is None"):
        sigma(s)


def test_A1_passes_below_cap():
    arch = make_arch(S=0.95, H=0.95, E=0.92, R=0.96, epsilon=0.035)
    result = check_A1_honesty_cap(arch)
    assert result.holds


def test_A1_fails_at_or_above_cap():
    arch = make_arch(S=0.99, H=0.99, E=0.99, R=0.99, epsilon=0.035)
    result = check_A1_honesty_cap(arch)
    assert not result.holds


def test_A2_passes_with_unmodeled_subspace():
    arch = make_arch(has_unmodeled=True, g_covers=False)
    result = check_A2_openness_subspace(arch)
    assert result.holds


def test_A2_fails_when_governance_covers():
    arch = make_arch(has_unmodeled=False, g_covers=True)
    result = check_A2_openness_subspace(arch)
    assert not result.holds


def test_A3_passes_arch_first():
    arch = make_arch(arch_first=True)
    result = check_A3_architecture_first(arch)
    assert result.holds


def test_A3_fails_target_first():
    arch = make_arch(arch_first=False)
    result = check_A3_architecture_first(arch)
    assert not result.holds


def test_check_all_axioms_returns_three_results():
    arch = make_arch()
    results = check_all_axioms(arch)
    assert len(results) == 3


def test_check_all_axioms_raises_on_fail_when_requested():
    arch = make_arch(arch_first=False)
    with pytest.raises(AxiomViolation):
        check_all_axioms(arch, raise_on_fail=True)


def test_partial_viability_full_pass():
    arch = make_arch()
    pv = partial_viability(arch)
    assert pv == pytest.approx(1.0)


def test_partial_viability_A1_violation_returns_zero():
    arch = make_arch(S=0.99, H=0.99, E=0.99, R=0.99)  # σ above cap
    pv = partial_viability(arch)
    assert pv == 0.0


def test_partial_viability_A3_violation_partial():
    arch = make_arch(arch_first=False)
    pv = partial_viability(arch)
    # A_1 + A_2 pass, A_3 fail · 2/3 weight
    assert pv == pytest.approx(2 / 3)


def test_falsifiability_returns_conditions():
    conds = get_falsifiability_conditions("A_1")
    assert len(conds) >= 1
    assert "σ = 1.0" in conds[0].condition


def test_falsifiability_unknown_returns_empty():
    conds = get_falsifiability_conditions("not_a_real_element")
    assert conds == []


def test_self_incompleteness_rejects_completeness_claim():
    claim = NACVersionClaim(version="v1.0", claimed_completeness=1.0, epsilon=0.035)
    with pytest.raises(CompletenessClaimError):
        assert_self_incompleteness(claim)


def test_self_incompleteness_accepts_within_cap():
    claim = NACVersionClaim(version="v0.2", claimed_completeness=0.92, epsilon=0.035)
    assert_self_incompleteness(claim)  # no exception


def test_default_epsilon_is_seawater():
    assert NAC_DEFAULT_EPSILON.epsilon == 0.035
    assert "seawater" in NAC_DEFAULT_EPSILON.name
