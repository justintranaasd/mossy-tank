# Workflow 1 — Keyword Research & Clustering

**When to use:** Before planning new content. Run this to find keywords, group them by intent,
and decide what type of page to build.

**Fill in:** `[SEED TOPIC]` before pasting.

---

## Prompt

```
You are an SEO strategist for Mossy Tank (mossytank.com), a beginner-focused aquascaping and
planted aquarium site. Target audience: beginner to intermediate hobbyists (US/UK/AU/CA).
Monetisation: display ads + Amazon affiliate + specialty aquarium affiliate.

SEED TOPIC: [SEED TOPIC]

Do the following:

1. EXPAND — Generate 30–50 keyword variations from this seed. Include:
   - Long-tail question variants ("how to", "why is", "best", "vs", "without")
   - Beginner-specific variants (add "for beginners", "easy", "low tech", "no CO2")
   - Troubleshooting variants ("not growing", "dying", "cloudy", "turning yellow")
   - Buying-intent variants ("best [product]", "[product] review", "[product A] vs [product B]")

2. CLUSTER — Group keywords into logical content clusters. For each cluster:
   - Cluster name
   - Primary keyword (highest volume / best fit)
   - Supporting keywords (3–8 per cluster)
   - Search intent: informational | commercial | transactional | navigational
   - Recommended page type: pillar | supporting-article | money-page | programmatic | faq

3. PRIORITISE — Score each cluster on:
   - Traffic potential (H/M/L)
   - Buyer intent (H/M/L)  
   - Estimated difficulty (H/M/L — favour low/medium for a new site)
   - Fits our positioning? (yes/no — beginner, low-tech, no-CO2, betta, shrimp)

4. RECOMMEND — List top 5 clusters to act on first, with one sentence of reasoning each.

Format as a markdown table for the cluster list, then a numbered priority list at the end.
Flag any YMYL or heavily monetised niches we should avoid (finance, health claims).
```

---

## After running this prompt

- Copy the output into [KEYWORDS-AND-CONTENT.md](../KEYWORDS-AND-CONTENT.md) under the relevant cluster section.
- Pick the top priority cluster and run **Workflow 2 (Content Brief)** on the primary keyword.
