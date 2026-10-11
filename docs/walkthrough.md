# Project Walkthrough

## Business Context

The business problem is to evaluate international fulfillment performance, identify shipment and inventory exceptions, and translate those findings into operational action.

The analysis follows an operations lifecycle:

```text
Operational data -> KPI measurement -> Exception detection -> Investigation -> Stakeholder communication -> Operational decisions
```

This project is not a production data platform. It is an operations analytics case study that shows how an analyst can use structured data to identify risk, request evidence, and support decisions.

## Dataset Overview

The workbook contains two source tabs:

- `Raw Order Data`: outbound order records with order dates, ship dates, warehouse, carrier, units ordered, and units shipped.
- `Inbound Data`: inbound purchase order records with expected units, received units, issue flags, and operational notes.

Analytical tabs include:

- `SLA Analysis`
- `Performance Summary`
- `Inbound Reconciliation`
- `charts`

All workbook sheets are visible. No hidden sheets were identified during review.

## SLA Methodology

The SLA target is two business days. The workbook uses a business-day formula equivalent to:

```text
NETWORKDAYS(order_date, ship_date) - 1
```

This treats the order date as day zero and excludes Saturdays and Sundays. No holiday calendar is included in the assessment, so public holidays are not excluded.

Orders without ship dates remain unclassified for SLA purposes. The confirmed breach rate is therefore calculated as:

```text
20 over-SLA orders / 57 orders with ship dates = 35.1%
```

It is not calculated as 20 out of 60 because the three missing ship dates require verification before SLA classification.

## Warehouse Analysis

The warehouse comparison uses dated orders only.

| Warehouse | Over SLA | Dated orders | Breach rate |
| --- | ---: | ---: | ---: |
| Devlnd UK | 9 | 19 | 47.4% |
| InterFulfillment CA | 6 | 19 | 31.6% |
| Fidelity NL | 5 | 19 | 26.3% |

Devlnd UK has the highest observed SLA risk. This does not prove the warehouse caused the delays. It identifies where dispatch timestamps, carrier handoff evidence, and process review should be prioritized.

## Outbound Completeness

Four orders have lower shipped units than ordered units:

| Order | Warehouse | Units ordered | Units shipped | SLA status |
| --- | --- | ---: | ---: | --- |
| ORD-0007 | Fidelity NL | 2 | 1 | Over SLA |
| ORD-0019 | Fidelity NL | 2 | 1 | Within SLA |
| ORD-0034 | Fidelity NL | 6 | 5 | Over SLA |
| ORD-0048 | InterFulfillment CA | 1 | 0 | Within SLA |

These are shipment quantity discrepancies. They are related to operational completeness, but they are not the same thing as SLA breaches. An order can be within SLA and still be short shipped.

## Inbound Reconciliation

Inbound reconciliation compares expected and received units for each purchase order.

| PO | Expected units | Received units | Missing units |
| --- | ---: | ---: | ---: |
| PO-DE-1005 | 100 | 100 | 0 |
| PO-FI-1022 | 100 | 96 | 4 |
| PO-IN-1039 | 100 | 100 | 0 |
| PO-DE-1056 | 100 | 96 | 4 |

The analysis confirms:

- 4 purchase orders reviewed
- 400 expected units
- 392 received units
- 8 missing units
- 2 purchase orders with discrepancies
- 50.0% PO discrepancy rate

The operational notes indicate matching pallet counts but mismatched unit quantities. That does not establish whether the shortage occurred during packing, transit, or receiving.

## Exception Investigation

The analysis separates facts from hypotheses.

Confirmed facts:

- 20 dated orders exceeded the SLA.
- 3 orders are missing ship dates.
- 4 orders have outbound short-shipment records.
- 2 inbound POs have four-unit shortages.

Evidence needed:

- Warehouse dispatch timestamps.
- Carrier acceptance scans.
- Packing lists.
- Bills of Lading.
- Proof of delivery.
- Receiving records.
- Shortage or inspection reports.

## Stakeholder Communication

The presentation includes three communication examples:

1. Warehouse escalation for `ORD-0007`.
2. Freight forwarder investigation for `PO-FI-1022`.
3. Client operational update.

Each communication is structured around confirmed facts, traceable identifiers, evidence requests, and next-step expectations. The communication avoids assigning responsibility before the supporting evidence is reviewed.

## Prioritization

Five operational requests are ranked according to customer impact, irreversible risk, cutoff timing, and evidence needs:

| Rank | Request | Immediate action |
| ---: | --- | --- |
| 1 | Client: 49 potentially delayed orders | Acknowledge, commit to update, verify exceptions |
| 2 | Warehouse: PO short four units | Hold closure, investigate discrepancy |
| 3 | Carrier: tomorrow pickup | Send required shipment details before cutoff |
| 4 | Finance: invoice backup EOD | Prepare and deliver supporting documentation |
| 5 | Historical report next week | Schedule after urgent operational work |

## Key Lessons

- Accurate KPI measurement depends on clear denominators.
- Missing data should be treated as an exception, not forced into a metric.
- Reconciliation requires both quantity comparison and evidence review.
- Operational communication should separate facts, hypotheses, and requests.
- Prioritization should reflect business impact and timing, not just request order.
