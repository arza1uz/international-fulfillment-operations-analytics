from __future__ import annotations

from pathlib import Path
import textwrap

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "screenshots"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "#17324D"
BLUE = "#2F6B9A"
LIGHT_BLUE = "#DCEAF5"
TEAL = "#2C7A7B"
ORANGE = "#D97706"
RED = "#B42318"
GRAY = "#667085"
LIGHT = "#F5F7FA"
INK = "#1F2933"


def save(fig, name: str) -> None:
    fig.savefig(OUT / name, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def add_title(fig, title: str, subtitle: str | None = None) -> None:
    fig.text(0.06, 0.93, title, fontsize=22, fontweight="bold", color=NAVY)
    if subtitle:
        fig.text(0.06, 0.885, subtitle, fontsize=11, color=GRAY)


def sla_performance() -> None:
    labels = ["Within SLA", "Over SLA", "Missing Ship Date"]
    values = [37, 20, 3]
    colors = [TEAL, ORANGE, GRAY]

    fig, ax = plt.subplots(figsize=(12, 7))
    add_title(
        fig,
        "Fulfillment SLA overview",
        "60 orders reviewed. Confirmed breach rate uses 20 over-SLA orders out of 57 dated orders.",
    )
    ax.bar(labels, values, color=colors, width=0.55)
    ax.set_ylim(0, 42)
    ax.set_ylabel("Orders", color=GRAY)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.grid(axis="y", color="#E5E7EB", linewidth=1)
    ax.tick_params(axis="x", labelsize=12, colors=INK)
    ax.tick_params(axis="y", colors=GRAY)
    for i, value in enumerate(values):
        ax.text(i, value + 1, str(value), ha="center", fontsize=16, fontweight="bold", color=INK)

    ax.text(
        1.55,
        34,
        "35.1%",
        fontsize=36,
        fontweight="bold",
        color=ORANGE,
        ha="center",
    )
    ax.text(
        1.55,
        30.5,
        "confirmed SLA breach rate",
        fontsize=12,
        color=GRAY,
        ha="center",
    )
    ax.text(
        1.55,
        27.8,
        "3 records have no ship date and remain unclassified",
        fontsize=10,
        color=GRAY,
        ha="center",
    )
    save(fig, "01-sla-performance.png")


def warehouse_performance() -> None:
    warehouses = ["Devlnd UK", "InterFulfillment CA", "Fidelity NL"]
    rates = [47.4, 31.6, 26.3]
    over = [9, 6, 5]
    dated = [19, 19, 19]
    colors = [RED, BLUE, TEAL]

    fig, ax = plt.subplots(figsize=(12, 7))
    add_title(
        fig,
        "Warehouse SLA performance",
        "Devlnd UK shows the highest observed SLA risk. Responsibility requires further evidence.",
    )
    bars = ax.barh(warehouses, rates, color=colors, height=0.5)
    ax.invert_yaxis()
    ax.set_xlim(0, 55)
    ax.set_xlabel("Breach rate among orders with ship dates", color=GRAY)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.grid(axis="x", color="#E5E7EB")
    ax.tick_params(axis="y", labelsize=12, colors=INK)
    ax.tick_params(axis="x", colors=GRAY)

    for i, bar in enumerate(bars):
        x = bar.get_width()
        ax.text(
            x + 1,
            bar.get_y() + bar.get_height() / 2,
            f"{rates[i]:.1f}%  ({over[i]} of {dated[i]})",
            va="center",
            fontsize=12,
            fontweight="bold" if i == 0 else "normal",
            color=INK,
        )
    save(fig, "02-warehouse-performance.png")


def inbound_reconciliation() -> None:
    pos = ["PO-DE-1005", "PO-FI-1022", "PO-IN-1039", "PO-DE-1056"]
    expected = [100, 100, 100, 100]
    received = [100, 96, 100, 96]

    fig, ax = plt.subplots(figsize=(12, 7))
    add_title(
        fig,
        "Inbound reconciliation",
        "Two purchase orders show four-unit shortages despite matching pallet counts.",
    )
    x = range(len(pos))
    ax.bar([i - 0.18 for i in x], expected, width=0.36, color=LIGHT_BLUE, label="Expected")
    ax.bar([i + 0.18 for i in x], received, width=0.36, color=BLUE, label="Received")
    ax.set_ylim(0, 115)
    ax.set_ylabel("Units", color=GRAY)
    ax.set_xticks(list(x), pos)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.grid(axis="y", color="#E5E7EB")
    ax.tick_params(axis="x", colors=INK)
    ax.tick_params(axis="y", colors=GRAY)
    ax.legend(frameon=False, loc="upper right")
    for i, (e, r) in enumerate(zip(expected, received)):
        if e != r:
            ax.text(i, 102, "-4 units", ha="center", fontsize=12, color=RED, fontweight="bold")
            ax.plot([i - 0.35, i + 0.35], [99, 99], color=RED, linewidth=2)
    save(fig, "03-inbound-reconciliation.png")


def operational_prioritization() -> None:
    rows = [
        ("01", "Client: 49 potentially delayed orders", "Acknowledge, verify exceptions, commit to update"),
        ("02", "Warehouse: PO short four units", "Hold closure and investigate discrepancy"),
        ("03", "Carrier: tomorrow pickup", "Send required shipment details before cutoff"),
        ("04", "Finance: invoice backup EOD", "Prepare and deliver supporting documentation"),
        ("05", "Historical report next week", "Schedule after urgent operational work"),
    ]

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.axis("off")
    add_title(
        fig,
        "Operational prioritization",
        "Requests are ranked by customer impact, irreversible risk, timing, and evidence needs.",
    )

    y = 0.78
    for rank, request, action in rows:
        color = NAVY if rank == "01" else BLUE if rank in {"02", "03"} else GRAY
        fig.patches.append(Rectangle((0.06, y - 0.035), 0.88, 0.085, transform=fig.transFigure, facecolor=LIGHT, edgecolor="#E5E7EB"))
        fig.text(0.085, y, rank, fontsize=16, color=color, fontweight="bold")
        fig.text(0.16, y + 0.014, request, fontsize=12, color=INK, fontweight="bold")
        fig.text(0.16, y - 0.016, action, fontsize=10.5, color=GRAY)
        y -= 0.115
    save(fig, "04-operational-prioritization.png")


def stakeholder_communication() -> None:
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.axis("off")
    add_title(
        fig,
        "Stakeholder communication",
        "Example warehouse escalation based on quantified exceptions and evidence requests.",
    )

    left = [
        "Subject: ORD-0007 - SLA Breach and Shipment Verification",
        "Measured issue: shipped four business days after order date.",
        "Shipment exception: 1 of 2 units shipped.",
        "Evidence requested: dispatch timestamp, carrier scan, and missing-unit explanation.",
        "Follow-up: acknowledge within two business hours and provide initial update by EOD.",
    ]
    right = [
        ("01", "States the measured SLA breach and unit shortage without speculation."),
        ("02", "Requests proof of carrier handoff rather than assuming it occurred."),
        ("03", "Defines response timing and escalation expectations."),
    ]

    fig.patches.append(Rectangle((0.06, 0.18), 0.52, 0.58, transform=fig.transFigure, facecolor=LIGHT, edgecolor="#D0D5DD"))
    fig.text(0.09, 0.70, "Warehouse escalation", fontsize=16, color=NAVY, fontweight="bold")
    y = 0.64
    for line in left:
        wrapped = textwrap.wrap(line, width=58)
        fig.text(0.09, y, wrapped[0], fontsize=10.7, color=INK, fontweight="bold" if line.startswith("Subject") else "normal")
        y -= 0.045
        for continuation in wrapped[1:]:
            fig.text(0.09, y, continuation, fontsize=10.7, color=INK)
            y -= 0.035
        y -= 0.01

    fig.text(0.63, 0.70, "Why it works", fontsize=16, color=NAVY, fontweight="bold")
    y = 0.62
    for num, text in right:
        fig.text(0.63, y, num, fontsize=15, color=BLUE, fontweight="bold")
        wrapped = textwrap.wrap(text, width=38)
        fig.text(0.69, y + 0.004, wrapped[0], fontsize=10.7, color=INK)
        yy = y - 0.033
        for continuation in wrapped[1:]:
            fig.text(0.69, yy, continuation, fontsize=10.7, color=INK)
            yy -= 0.033
        y -= 0.15
    save(fig, "05-stakeholder-communication.png")


def main() -> None:
    sla_performance()
    warehouse_performance()
    inbound_reconciliation()
    operational_prioritization()
    stakeholder_communication()
    print("Generated screenshots in", OUT)


if __name__ == "__main__":
    main()
