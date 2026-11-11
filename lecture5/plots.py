"""Helpers shared by the Lecture 5 plotting programs."""

from pathlib import Path

PLOTS = Path(__file__).parent / "plots"  # Where the programs save PNGs
BLUE, ORANGE, GRAY = "#2a78d6", "#eb6834", "#777777"  # Marks
BLUE_TEXT = "#2f6fb5"  # For text: 5.17:1 on white (BLUE is 4.42:1)


def tag(ax, x, y, n):
    """Draw a numbered tag (white on a dark circle) at (x, y)."""
    ax.annotate(
        str(n),
        (x, y),
        ha="center",
        va="center",
        color="white",
        fontsize=8,
        fontweight="bold",
        bbox={"boxstyle": "circle,pad=0.2", "fc": "#1b1b1b", "lw": 0},
    )


def save(fig, name):
    """Save fig as plots/<name>.png, 300 dots per inch."""
    PLOTS.mkdir(exist_ok=True)
    fig.savefig(PLOTS / f"{name}.png", dpi=300)
    print(f"saved plots/{name}.png")
