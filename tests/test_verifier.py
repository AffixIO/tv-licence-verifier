import pytest
from tv_licence import CheckInput, TvLicenceVerifier

def test_live_tv_requires_coverage_and_uses_current_fee():
    result = TvLicenceVerifier().check(CheckInput(True, False))
    assert result.status == "LICENCE_LIKELY_REQUIRED"
    assert result.annual_fee_gbp == 180.0

def test_free_over_75_concession_is_flagged_not_asserted():
    result = TvLicenceVerifier().check(CheckInput(False, True, age=75, receives_pension_credit=True))
    assert result.status == "CONCESSION_POSSIBLE"
    assert result.annual_fee_gbp == 0.0

def test_no_live_or_iplayer_activity():
    assert TvLicenceVerifier().check(CheckInput(False, False)).status == "NO_LICENCE_INDICATED"

def test_official_and_suspicious_links():
    verifier = TvLicenceVerifier()
    assert verifier.check_link("https://www.gov.uk/find-licences/tv-licence")[0]
    assert not verifier.check_link("https://tv-licence-refund.example/pay")[0]
    assert not verifier.check_link("http://tvlicensing.co.uk/")[0]

def test_invalid_age_fails_closed():
    with pytest.raises(ValueError): TvLicenceVerifier().check(CheckInput(False, True, age=-1))
