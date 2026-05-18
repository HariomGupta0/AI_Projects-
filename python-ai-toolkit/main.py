import argparse
import sys

sys.stdout.reconfigure(encoding='utf-8')
from rich.console import Console
from rich.panel import Panel
from rich.status import Status

from ai_utils import (
    summarize_text,
    translate_text,
    analyze_sentiment
)

# Rich console
console = Console()

# ---------------------------------
# Argument Parser
# ---------------------------------

parser = argparse.ArgumentParser(
    description="Python AI Toolkit CLI"
)

subparsers = parser.add_subparsers(
    dest="command"
)

# ---------------------------------
# Summarize Command
# ---------------------------------

summarize_parser = subparsers.add_parser(
    "summarize"
)

summarize_parser.add_argument(
    "text",
    help="Text to summarize"
)

# ---------------------------------
# Translate Command
# ---------------------------------

translate_parser = subparsers.add_parser(
    "translate"
)

translate_parser.add_argument(
    "text",
    help="Text to translate"
)

translate_parser.add_argument(
    "--lang",
    required=True,
    help="Target language"
)

# ---------------------------------
# Sentiment Command
# ---------------------------------

sentiment_parser = subparsers.add_parser(
    "sentiment"
)

sentiment_parser.add_argument(
    "text",
    help="Text for sentiment analysis"
)

# Parse Arguments
args = parser.parse_args()

# ---------------------------------
# Execute Commands
# ---------------------------------

if args.command == "summarize":

    with console.status(
        "[bold green]Generating summary..."
    ):

        result = summarize_text(args.text)

    console.print(
        Panel(
            result,
            title="SUMMARY",
            border_style="green"
        )
    )

elif args.command == "translate":

    with console.status(
        "[bold blue]Translating text..."
    ):

        result = translate_text(
            args.text,
            args.lang
        )

    console.print(
        Panel(
            result,
            title="TRANSLATION",
            border_style="blue"
        )
    )

elif args.command == "sentiment":

    with console.status(
        "[bold magenta]Analyzing sentiment..."
    ):

        result = analyze_sentiment(args.text)

    console.print(
        Panel(
            result,
            title="SENTIMENT",
            border_style="magenta"
        )
    )

else:
    parser.print_help()