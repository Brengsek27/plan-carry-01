#!/usr/bin/env python3
"""Plan-carry-01: Write a plan to /output/entry.txt"""

import os
import sys

PLAN = "Day 1: fetch make.fun bounties $35–100, code/text, ≤48h; enter 3. Daily: enter 3 best new bounties via free models. $100 for API only—no fees/ads. Edge: skip human-gated Upwork/Fiverr; make.fun pays USDC. Expected: two $50 wins cover $100; day 30 hold $200–350 USDC on Solana."

def main() -> int:
    # Validate plan
    if not (1 <= len(PLAN) <= 280):
        print(f"Plan length {len(PLAN)} not in range 1-280", file=sys.stderr)
        return 1
    if not PLAN.strip():
        print("Plan is only whitespace", file=sys.stderr)
        return 1

    # Create output directory
    os.makedirs("/output", exist_ok=True)

    # Write plan to entry.txt (no trailing newline)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)

    # Print character count
    print(len(PLAN))
    return 0


if __name__ == "__main__":
    sys.exit(main())
# Gate: PLAN must be 1-280 UTF-8 chars, no trailing newline; program is deterministic and uses no network.
