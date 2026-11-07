# Example MCP Tool Contract

**Tool name:** get_public_order_status  
**Purpose:** Read the status of an order belonging to the authenticated user.  
**Access class:** Read-only  
**Required permission:** User-scoped order read permission  
**Side effects:** None  

## Input

| Field | Type | Required | Constraints |
|---|---|---|---|
| order_id | string | yes | Must belong to the authenticated user |

## Output

- order_id: string
- status: enum
- updated_at: ISO 8601 timestamp

## Errors

- INVALID_INPUT
- NOT_FOUND
- NOT_AUTHORIZED
- RATE_LIMITED
- TEMPORARY_UNAVAILABLE

## Security and tests

- Enforce user ownership server-side.
- Do not accept a user_id override from an untrusted caller.
- Redact personal information from logs.
- Test valid order, invalid identifier, another user's order, missing permission, timeout, and retry.
- Never include credentials or production IDs in this template.
