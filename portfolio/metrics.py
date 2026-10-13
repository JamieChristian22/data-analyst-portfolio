"""Statistical estimators with explicit units and failure conditions."""
from math import sqrt
from scipy.stats import norm, chisquare


def proportion_interval(successes, total, confidence=0.95):
    """Wilson interval for a binomial proportion; independent trials assumed."""
    if total <= 0 or not 0 <= successes <= total:
        raise ValueError('Require 0 <= successes <= total and total > 0')
    z = norm.ppf(1 - (1-confidence)/2)
    p = successes / total
    denominator = 1 + z*z/total
    center = (p + z*z/(2*total))/denominator
    half = z*sqrt(p*(1-p)/total + z*z/(4*total*total))/denominator
    return max(0., center-half), min(1., center+half)


def experiment(control_success, control_n, treatment_success, treatment_n):
    """Two-sided pooled z-test plus Newcombe-Wilson difference interval.

    The 50:50 sample-ratio test is a diagnostic assumption, not verified
    experiment metadata. Session independence cannot be established without IDs.
    """
    lo_a, hi_a = proportion_interval(control_success, control_n)
    lo_b, hi_b = proportion_interval(treatment_success, treatment_n)
    a, b = control_success/control_n, treatment_success/treatment_n
    delta = b-a
    pooled = (control_success+treatment_success)/(control_n+treatment_n)
    se = sqrt(pooled*(1-pooled)*(1/control_n+1/treatment_n))
    pvalue = float(2*norm.sf(abs(delta/se))) if se else 1.0
    return dict(control_n=int(control_n), treatment_n=int(treatment_n),
                control_rate=a, treatment_rate=b, absolute_lift=delta,
                relative_lift=delta/a if a else None,
                difference_ci_low=delta-sqrt((b-lo_b)**2+(hi_a-a)**2),
                difference_ci_high=delta+sqrt((hi_b-b)**2+(a-lo_a)**2),
                p_value=pvalue,
                srm_p_value_50_50=float(chisquare([control_n,treatment_n]).pvalue),
                confidence_level=0.95)


def ratio(numerator, denominator):
    return numerator/denominator if denominator else None
