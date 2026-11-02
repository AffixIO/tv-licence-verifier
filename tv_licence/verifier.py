from __future__ import annotations
from dataclasses import dataclass
from urllib.parse import urlparse

OFFICIAL_DOMAINS = {"gov.uk", "tvlicensing.co.uk"}
CURRENT_ANNUAL_COLOUR_FEE_GBP = 180.00

@dataclass(frozen=True)
class CheckInput:
    watches_live_tv: bool
    watches_bbc_iplayer: bool
    age: int | None = None
    receives_pension_credit: bool = False
    severely_sight_impaired: bool = False
    lives_in_care_home: bool = False
    student: bool = False

@dataclass(frozen=True)
class CheckResult:
    status: str
    reason: str
    official_next_step: str
    annual_fee_gbp: float | None

class TvLicenceVerifier:
    """Rules helper, not a personal licence-account lookup or legal decision."""
    def check(self, facts: CheckInput) -> CheckResult:
        if facts.age is not None and facts.age < 0: raise ValueError("age cannot be negative")
        needs_licence = facts.watches_live_tv or facts.watches_bbc_iplayer
        if not needs_licence:
            return CheckResult("NO_LICENCE_INDICATED", "The supplied activities do not indicate live TV or BBC iPlayer use.", "Confirm the current rules on GOV.UK.", None)
        if facts.age is not None and facts.age >= 75 and facts.receives_pension_credit:
            return CheckResult("CONCESSION_POSSIBLE", "A free licence may be available for eligible people aged 75 or over receiving Pension Credit.", "Check eligibility with TV Licensing.", 0.0)
        if facts.severely_sight_impaired:
            return CheckResult("CONCESSION_POSSIBLE", "A 50% concession may be available for a severely sight-impaired person.", "Check the evidence requirements with TV Licensing.", CURRENT_ANNUAL_COLOUR_FEE_GBP / 2)
        if facts.lives_in_care_home:
            return CheckResult("CONCESSION_POSSIBLE", "A residential-care concession may apply depending on the accommodation and circumstances.", "Ask the care home or TV Licensing about an ARC licence.", None)
        return CheckResult("LICENCE_LIKELY_REQUIRED", "The supplied activities normally require coverage under the current rules.", "Use the official TV Licensing service to buy or confirm coverage.", CURRENT_ANNUAL_COLOUR_FEE_GBP)

    def check_link(self, url: str) -> tuple[bool, str]:
        parsed = urlparse(url)
        host = (parsed.hostname or "").lower().removeprefix("www.")
        if parsed.scheme != "https": return False, "Use an HTTPS official link."
        if host in OFFICIAL_DOMAINS or host.endswith(".gov.uk"):
            return True, "Official-domain link; still verify the exact page and avoid sharing credentials."
        return False, "This is not an official GOV.UK or TV Licensing domain. Do not enter payment details."
