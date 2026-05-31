# SSP/2026 — Stefan Stefanov Portfolio Terminal 

> **Young Investor 2026** · Finance Club at Sofia High School of Mathematics (SMG)  
> Prepared by **Mariela Bedrova and Team** · MAY 2026

---

## Overview

An interactive, browser-based investment portfolio terminal built for the **Young Investor 2026** competition. The terminal presents a complete €700,000 investment mandate for the hypothetical client **Stefan Stefanov** — a 37-year-old Bulgarian entrepreneur who sold his EV charging station maintenance company in Germany (Dec 2025) and deposited €700,000 into a Bulgarian bank account on January 1, 2026.

---

## Client Profile

| Field | Detail |
|---|---|
| **Name** | Stefan Stefanov |
| **Age** | 37 · Sofia, Bulgaria |
| **Background** | Sold EV charging station maintenance company (Germany) — exited Dec 2025 |
| **Capital** | €700,000 (post-exit, after German taxes) |
| **Status** | Unmarried · no children · no family formation planned |
| **Interests** | Cooking · skiing · music · annual 10-day Alps resort trip |
| **Personality** | Practical · analytical · disciplined · patient · detail-oriented |

---

## Portfolio at a Glance

| Metric | Value |
|---|---|
| **Total Mandate** | €700,000 |
| **Target Return** | 6.0–6.5% p.a. (inflation + 3%) |
| **Investment Horizon** | 20–28 years (retirement 2052–2056) |
| **Risk Profile** | Moderate — max drawdown −22%, volatility 9–11% |
| **Blended TER** | 0.22% p.a. |
| **Instruments** | 13 UCITS ETFs & listed bonds |
| **Sharpe Ratio** | ~0.60 |

### Asset Allocation

| Class | Weight | EUR Value |
|---|---|---|
| Equities | 55% | €385,000 |
| Fixed Income | 35% | €245,000 |
| Real Assets | 7% | €49,000 |
| Cash | 3% | €21,000 |

---

## Features

- **Boot sequence** terminal animation on load
- **Live NAV** with animated sparkline (simulated)
- **Interactive allocation sliders** — drag to remodel weights, live IPS compliance scorecard
- **Drift visualiser** — real-time ±5% IPS threshold monitoring
- **20-year projection** with bull/base/bear scenarios
- **Monte Carlo simulation** — 300 paths, P10/P50/P90 percentiles
- **Correlation heatmap** — 13×13 matrix
- **Efficient frontier** scatter plot
- **Factor radar** (Value, Growth, Quality, Momentum, Low Vol, ESG)
- **ESG scorecard** (E: 72 AA · S: 68 A · G: 76 AA)
- **Backtest chart** (Jan 2020–Apr 2026)
- **Drawdown chart** vs −22% IPS limit
- **Crisis stress tests** — GFC, COVID, Rate Shock, Geopolitical
- **Behavioral finance quiz** — 5 questions on IPS rules & biases
- **Scenario calculator** — input capital & horizon, compute bull/base/bear
- **Glide path** visualiser (55% → 40% equity into retirement)
- **Command palette** (`Ctrl+K`) and full keyboard shortcuts
- **Print / PDF export** ready

---

## Sections

| # | Section | Content |
|---|---|---|
| §01 | Executive Summary | KPIs, performance chart, investment thesis |
| §02 | Client Profile & IPS | Dossier, 6 core IPS rules, compliance scorecard, 3 goals |
| §03 | Asset Allocation | Doughnut chart, sliders, drift, projection, glide path, frontier |
| §04 | Holdings | 13-instrument table, factor radar, ESG, correlation heatmap |
| §05 | Risk & Behavioral | Stress tests, Monte Carlo, bias cards, behavioral quiz |
| §06 | Implementation | Entry strategy, benchmark, milestones timeline, tax efficiency |
| §07 | Conclusion | 3-pillar synthesis, Benjamin Graham quote, 9 references |

---

## Running Locally

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

---

## Competition

- **Event:** Young Investor 2026 — Finance Club, Sofia High School of Mathematics
- **Mentor:** Dr. Boyan Ivanchev (founder of behavioral finance & neuroeconomics in Bulgaria)
- **Submission:** [mlad.investitor@outlook.com](mailto:mlad.investitor@outlook.com)
- **Team size:** 1–5 participants · Grades 9–12
