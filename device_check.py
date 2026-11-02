"""Consent-based local helper.

It does not inspect applications, network traffic, cameras, microphones,
licence databases or device identifiers. The user supplies the viewing facts.
"""
import argparse
from tv_licence import CheckInput, TvLicenceVerifier

parser = argparse.ArgumentParser(description="Check TV Licence guidance from facts you choose to provide")
parser.add_argument("--live-tv", action="store_true", help="You watch or record live television")
parser.add_argument("--iplayer", action="store_true", help="You use BBC iPlayer")
parser.add_argument("--age", type=int)
parser.add_argument("--pension-credit", action="store_true")
parser.add_argument("--severely-sight-impaired", action="store_true")
parser.add_argument("--care-home", action="store_true")
args = parser.parse_args()
result = TvLicenceVerifier().check(CheckInput(args.live_tv, args.iplayer, args.age, args.pension_credit, args.severely_sight_impaired, args.care_home))
print(f"{result.status}: {result.reason}")
print(f"Next step: {result.official_next_step}")
print("No device scan, licence lookup, network inspection or personal data collection was performed.")
