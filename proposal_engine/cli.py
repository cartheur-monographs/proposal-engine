from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="proposal-engine",
        description="Create and refine persuasive proposals with structured workflows.",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show the current Proposal Engine version.",
    )
    parser.add_argument(
        "--name",
        default="The Proposal Engine",
        help="Name of the project context for this session.",
    )
    return parser


def run(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        from proposal_engine import __version__

        print(__version__)
        return 0

    print(f"{args.name} is ready. Start building proposal workflows.")
    return 0
