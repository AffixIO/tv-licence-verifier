# UK TV Licence verifier

A small, source-aware helper for answering common UK TV Licence questions without pretending to access a person's licence account or make a legal decision.

## Current themes covered

- The colour TV Licence fee listed for 2026/27 is £180 from 1 April 2026.
- Live television and BBC iPlayer are the key activities to check.
- Possible concessions include eligible people aged 75 or over receiving Pension Credit, severely sight-impaired customers and some residential-care settings.
- Student arrangements depend on the accommodation and circumstances.
- Fake renewal and failed-payment messages are a recurring scam pattern, so the demo checks whether a link uses an official GOV.UK or TV Licensing domain.

## Quickstart

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install pytest
pytest -q
python demo.py
```

## Result meanings

- `LICENCE_LIKELY_REQUIRED`: the supplied activities normally need coverage.
- `CONCESSION_POSSIBLE`: a concession may apply, but the official service must confirm it.
- `NO_LICENCE_INDICATED`: the supplied facts do not indicate live TV or BBC iPlayer use.

## Safety boundary

This is not an official TV Licensing checker. It does not look up personal accounts, accept payments, store addresses, process licence numbers or determine liability. Rules and fees can change, so users should confirm the result through official sources.

The link checker is deliberately conservative. A domain check is not proof that a page is safe; users should navigate independently from official GOV.UK or TV Licensing pages and never submit payment credentials through a suspicious message.

## Official sources

- [GOV.UK TV Licence](https://www.gov.uk/find-licences/tv-licence)
- [GOV.UK 2026/27 fee announcement](https://www.gov.uk/government/news/cost-of-tv-licence-fee-set-for-202627)
- [TV Licensing concessions](https://www.tvlicensing.co.uk/faqs/FAQ101)
- [Trading Standards Scotland scam guidance](https://www.tsscot.co.uk/tv-licence-scams/)

## AffixIO integration boundary

The local rules helper is intentionally dependency-light. A production AffixIO integration could attest to the version of the public rules used for a decision and record a privacy-minimised evidence digest. It should not make a proof look like an official licence or replace TV Licensing's own account systems.

## Status

Research example. Fictional inputs only. Not government software, legal advice or a payment service.

## Contributing

Keep rule changes source-linked, add tests for every change, and never commit personal licence details, payment data or credentials.

## License

MIT
