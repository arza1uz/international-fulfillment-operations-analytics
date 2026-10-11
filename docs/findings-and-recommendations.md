# Findings and Recommendations

## Confirmed Findings

### Fulfillment SLA

- 60 outbound orders were analyzed.
- 57 orders had recorded shipping dates.
- 37 orders were within the two-business-day SLA.
- 20 dated orders exceeded the SLA.
- 3 orders had missing ship dates and remain unclassified for SLA purposes.
- The confirmed SLA breach rate is 35.1%.

### Warehouse SLA Risk

| Warehouse | Over SLA | Dated orders | Breach rate |
| --- | ---: | ---: | ---: |
| Devlnd UK | 9 | 19 | 47.4% |
| InterFulfillment CA | 6 | 19 | 31.6% |
| Fidelity NL | 5 | 19 | 26.3% |

Devlnd UK has the highest observed SLA risk. This is a prioritization signal, not proof of root cause.

### Outbound Completeness

Four orders have short shipments:

- `ORD-0007`
- `ORD-0019`
- `ORD-0034`
- `ORD-0048`

The first three are associated with Fidelity NL. `ORD-0048` is associated with InterFulfillment CA in the workbook.

### Inbound Reconciliation

- 4 purchase orders were reviewed.
- Expected units totaled 400.
- Received units totaled 392.
- Missing units totaled 8.
- 2 of 4 purchase orders had discrepancies.
- The PO discrepancy rate is 50.0%.

Affected POs:

- `PO-FI-1022`: 100 expected, 96 received.
- `PO-DE-1056`: 100 expected, 96 received.

## Operational Risks

- Repeated SLA breaches can affect client trust and customer delivery expectations.
- Missing ship dates reduce confidence in operational reporting.
- Short shipments create downstream customer, warehouse, and inventory-control risk.
- Inbound unit shortages can affect inventory availability and financial reconciliation.
- Matching pallet counts with mismatched unit counts requires document-level review before responsibility is assigned.

## Investigation Hypotheses

These are hypotheses, not conclusions:

- Devlnd UK may have a warehouse processing, carrier handoff, or scan-capture issue.
- Fidelity NL may require review of picking, packing, or shipment completeness controls.
- Inbound shortages may have occurred during packing, transit, receiving, or data entry.
- Missing ship dates may reflect incomplete event capture rather than actual non-shipment.

## Recommended Actions

### SLA Monitoring

Introduce proactive tracking for orders approaching the two-business-day limit.

### Missing Shipping Dates

Create a data-quality exception queue for missing or inconsistent shipping events.

### Warehouse Performance

Investigate fulfillment and carrier handoff processes at Devlnd UK. Request dispatch timestamps, carrier acceptance scans, and handoff documentation.

### Outbound Completeness

Review the short-shipment pattern associated with Fidelity NL while also investigating `ORD-0048` with InterFulfillment CA.

### Inbound Reconciliation

Keep affected purchase orders open until receiving records, packing lists, Bills of Lading, proof of delivery, and shortage documentation are reconciled.

### Stakeholder Reporting

Standardize exception updates using:

- Confirmed facts.
- Traceable identifiers.
- Evidence requested.
- Responsible party.
- Next follow-up deadline.

## Data Limitations

- The dataset is academic and limited in size.
- No holiday calendar is provided.
- No dispatch timestamps, carrier scan events, or delivery documents are included.
- Root cause cannot be assigned from the available data alone.
- Recommendations are proposed actions, not measured improvements.
