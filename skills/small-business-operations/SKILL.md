---
name: small-business-operations
description: Create operating procedures that help small businesses run consistently. Use when improving retail, food, printing, or service operations such as stock control, purchasing, cash reconciliation, customer service, and daily reporting.
license: Apache-2.0
metadata:
  author: BOS Digital Indonesia
  version: "1.0.1"
---

# Small Business Operations

Help small-business owners build simple, auditable routines that fit their actual staff, tools, and transaction records. Prefer practical procedures over complicated enterprise processes.

## Understand the operation first

Identify the business type, sales channels, products or services, operating hours, staff roles, payment methods, inventory method, POS or accounting tools, and the decision the owner needs to make. Do not assume the business has a full ERP system.

## Operating principles

1. **Use source records.** Base calculations on POS exports, invoices, stock counts, bank/provider statements, and documented transactions. Label estimates and missing records.
2. **Separate sales, payments, and cash.** Recorded sales, confirmed payments, settlements, cash drawer counts, refunds, fees, and owner withdrawals are different events. Do not combine them without reconciliation.
3. **Verify electronic payments.** A sound, screenshot, browser notification, customer claim, or webhook event alone is not proof of settlement. Verify against the authoritative provider or merchant record using transaction reference and amount. Never ask for customer PINs or credentials.
4. **Track inventory movement.** Record opening stock, purchases, sales or usage, returns, damage, adjustments, and physical closing count. Explain quantity differences instead of silently forcing balances to match.
5. **Keep roles clear.** Define who records, approves adjustments or refunds, counts cash, and reviews exceptions. For small teams, use a second-person or periodic owner review.
6. **Protect customer information.** Collect only what is needed, restrict access, mask identifiers, and never publish invoices, phone numbers, addresses, or transaction details.
7. **Use simple controls.** Favor daily checklists, exception logs, numbered receipts, stock thresholds, approval limits, and periodic spot checks.
8. **Make advice measurable.** Define owner, frequency, input records, expected output, tolerance, and escalation path.

## Workflow

1. Map the current process and available evidence.
2. Identify the largest operational risks and recurring bottlenecks.
3. Propose a simple target process with clear roles and records.
4. Define daily, weekly, and monthly routines as appropriate.
5. Define exception handling for shortages, duplicate payments, refunds, failed settlements, damaged stock, and system outages.
6. Estimate costs and benefits only from stated inputs; label assumptions.
7. Pilot changes on a small scope and review results before rollout.

## Output format

- Current-state summary and evidence gaps.
- Main risks ranked by likelihood and impact.
- Recommended workflow with roles and frequency.
- Checklists, log templates, and reconciliation formulas as needed.
- Metrics and review cadence.
- Assumptions, open questions, and rollback or contingency steps.

## Safety boundaries

- Do not claim a payment is settled based only on an audible alert or customer screenshot.
- Never modify production POS data, issue refunds, adjust inventory, or move money without explicit authorization.
- Do not publish customer or employee personal data.
