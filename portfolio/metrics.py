"""Statistical estimators with explicit units, assumptions, and failure conditions."""
from math import isfinite, sqrt
from numbers import Integral, Real
from scipy.stats import norm, chisquare


def _count(value, name):
    """Prevent truncated / fractional / boolean event counts from entering inference."""
    if isinstance(value, bool) or not isinstance(value, Integral) or value < 0:
        raise ValueError(f'{name} must be a nonnegative integer')
    return int(value)


def _probability(value, name):
    if isinstance(value, bool) or not isinstance(value, Real) or not isfinite(value) or not 0 < value < 1:
        raise ValueError(f'{name} must be a finite number strictly between 0 and 1')
    return float(value)


def proportion_interval(successes, total, confidence=0.95):
    """Wilson interval for a binomial proportion; independent trials assumed."""
    successes = _count(successes, 'successes')
    total = _count(total, 'total')
    confidence = _probability(confidence, 'confidence')
    if total == 0 or successes > total:
        raise ValueError('Require 0 <= successes <= total and total > 0')
    z = norm.ppf(1 - (1 - confidence) / 2)
    p = successes / total
    denominator = 1 + z*z / total
    center = (p + z*z / (2*total)) / denominator
    half = z*sqrt(p*(1-p)/total + z*z/(4*total*total)) / denominator
    return max(0., center-half), min(1., center+half)


def experiment(control_success, control_n, treatment_success, treatment_n,
               expected_treatment_share=0.5):
    """Two-sided pooled z-test with a Newcombe-Wilson difference interval.

    The sample-ratio mismatch (SRM) check is diagnostic, not proof of randomization.
    Set expected_treatment_share to the actual planned allocation when not 50:50.
    Session/user independence cannot be established without event identifiers.
    """
    control_success = _count(control_success, 'control_success')
    control_n = _count(control_n, 'control_n')
    treatment_success = _count(treatment_success, 'treatment_success')
    treatment_n = _count(treatment_n, 'treatment_n')
    expected_treatment_share = _probability(expected_treatment_share, 'expected_treatment_share')
    lo_a, hi_a = proportion_interval(control_success, control_n)
    lo_b, hi_b = proportion_interval(treatment_success, treatment_n)
    a, b = control_success / control_n, treatment_success / treatment_n
    delta = b-a
    pooled = (control_success+treatment_success)/(control_n+treatment_n)
    se = sqrt(pooled*(1-pooled)*(1/control_n+1/treatment_n))
    pvalue = float(2*norm.sf(abs(delta/se))) if se else 1.0
    n = control_n+treatment_n
    srm_expected = float(chisquare(
        [control_n, treatment_n],
        f_exp=[n*(1-expected_treatment_share), n*expected_treatment_share]
    ).pvalue)
    result = dict(control_n=control_n, treatment_n=treatment_n,
                  control_rate=a, treatment_rate=b, absolute_lift=delta,
                  relative_lift=delta/a if a else None,
                  difference_ci_low=delta-sqrt((b-lo_b)**2+(hi_a-a)**2),
                  difference_ci_high=delta+sqrt((hi_b-b)**2+(a-lo_a)**2),
                  p_value=pvalue,
                  srm_p_value_50_50=float(chisquare([control_n, treatment_n]).pvalue),
                  confidence_level=0.95)
    # Preserve committed default-allocation report schemas, while supporting
    # an explicit alternative assignment ratio for new experiments.
    if expected_treatment_share != 0.5:
        result['srm_p_value_expected_allocation'] = srm_expected
        result['expected_treatment_share'] = expected_treatment_share
    return result


def ratio(numerator, denominator):
    return numerator / denominator if denominator else None
