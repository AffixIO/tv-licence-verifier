from tv_licence import CheckInput, TvLicenceVerifier

verifier = TvLicenceVerifier()
for label, facts in {
    "ordinary household": CheckInput(True, False),
    "over-75 with Pension Credit": CheckInput(False, True, age=78, receives_pension_credit=True),
    "not watching live TV or iPlayer": CheckInput(False, False),
}.items():
    result = verifier.check(facts)
    print(label, "=>", result.status, "|", result.reason)
print("link check =>", verifier.check_link("https://www.tvlicensing.co.uk/"))
