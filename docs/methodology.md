# Methodology

## Source Review

The project uses the completed assessment workbook and presentation PDF as source evidence.

The workbook was inspected for:

- Sheet names and visibility.
- Analytical and source tabs.
- Workbook metadata.
- Formula presence.
- Hidden sheets.
- Defined names.
- Potential confidentiality markers.

The PDF was inspected for page count, metadata, extracted text, and alignment with workbook identifiers.

## Source Tabs

The source data tabs are:

- `Raw Order Data`
- `Inbound Data`
- `Instructions`

The analytical tabs are:

- `SLA Analysis`
- `Performance Summary`
- `Inbound Reconciliation`
- `charts`

## SLA Calculation

The SLA methodology follows the workbook's stated assumption:

```text
orders should ship within two business days of the order date
```

Business days exclude Saturdays and Sundays. The order date is treated as day zero:

```text
NETWORKDAYS(order_date, ship_date) - 1
```

No holidays are included because the workbook does not include a holiday calendar.

## SLA Classification

| Condition | Classification |
| --- | --- |
| Missing ship date | Missing Ship Date |
| Business days to ship greater than 2 | Over SLA |
| Business days to ship 0, 1, or 2 | Within SLA |

Missing ship dates are excluded from the confirmed SLA breach denominator.

## Warehouse Performance

Warehouse performance is calculated using dated orders only:

```text
warehouse breach rate = warehouse over-SLA orders / warehouse orders with ship dates
```

This supports risk prioritization, not final responsibility assignment.

## Outbound Completeness

Outbound completeness is evaluated separately from SLA performance:

```text
unit variance = units shipped - units ordered
```

Negative variances are treated as short shipments and require investigation.

## Inbound Reconciliation

Inbound reconciliation compares expected units and received units:

```text
unit variance = received units - expected units
missing units = max(0, expected units - received units)
```

Purchase orders with negative unit variance are flagged as discrepancies.

## Public-Sharing Review

No hidden workbook sheets were found. No credentials, API keys, tokens, corporate GitHub references, or proprietary employer references were identified in the workbook text scan.

The project is presented as an academic case study. The published filenames are neutral and do not imply production ownership.

## Reproducibility

The script `scripts/validate_metrics.py` independently recalculates key metrics from the source workbook and checks the presentation for the inbound purchase order identifier discrepancy.
