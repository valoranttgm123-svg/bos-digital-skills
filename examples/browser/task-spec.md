# Example Browser Task Specification

- Objective: collect publicly displayed product prices from a named supplier's catalog.
- Scope: public product pages only.
- Allowed actions: open pages, read product names, visible prices, availability labels, and public product URLs.
- Disallowed actions: sign in, submit orders, add items to cart, contact sellers, bypass access restrictions, or collect personal data.
- Output: CSV with product name, displayed price, currency, availability text, URL, and observation date.
- Rate: follow site rules and use reasonable request pacing.
- Stop conditions: login wall, CAPTCHA, rate-limit warning, terms restriction, or ambiguous price.
- Verification: open a sample of collected URLs and confirm the captured value remains visible.
