# Workflow 2 — Content Brief Generator

**When to use:** Once you have a target keyword. Run this to get a full brief before drafting.
Always run this before Workflow 3 (Draft Writer).

**Fill in:** all `[VARIABLES]` before pasting.

---

## Prompt

```
You are an SEO content strategist for Mossy Tank (mossytank.com), a beginner-focused aquascaping
and planted aquarium site. Monetisation: display ads + Amazon affiliate + specialty aquarium
programs.

TARGET KEYWORD: [PRIMARY KEYWORD]
SECONDARY KEYWORDS: [2–5 SUPPORTING KEYWORDS FROM CLUSTER]
CLUSTER: [CLUSTER NAME e.g. "low-tech planted tanks"]
PAGE TYPE: [pillar | supporting-article | money-page | troubleshooting]
AUDIENCE: beginner to intermediate aquarium hobbyists; skew anxious/uncertain beginners

Generate a full content brief with the following sections:

1. PAGE GOAL
   - What does the reader want when they search this keyword?
   - What do we want them to do after reading? (e.g. click affiliate link, read pillar, subscribe)

2. SEO METADATA
   - Suggested H1 (max 60 chars, includes primary keyword)
   - Title tag (max 60 chars)
   - Meta description (max 155 chars, includes keyword, has a hook)
   - URL slug (lowercase, hyphens, max 5–6 words)

3. CONTENT OUTLINE
   - Suggested word count range
   - H2 and H3 headings structure (in order)
   - For each H2: one sentence on what it should cover
   - Flag which sections are good spots for: affiliate links | internal links | images | FAQ schema

4. ENTITIES & TERMS TO INCLUDE
   - List 10–15 related terms, product names, and concepts Google expects to see on this topic
   - Flag any products worth linking to on Amazon

5. INTERNAL LINKS
   - Suggest 3–5 pages on our site this article should link to (use our site architecture:
     pillars = low-tech guide, planted betta, shrimp/nano, plants-for-beginners;
     money pages = filters, lights, substrate, tanks, starter kits;
     troubleshooting = cloudy water, new tank syndrome, algae, plant melt)
   - Suggest what anchor text to use

6. SCHEMA TYPE
   - Recommended schema: Article | HowTo | FAQPage | ItemList | Product
   - Note any FAQ questions worth marking up

7. E-E-A-T HOOKS
   - List 3–5 specific questions or prompts the operator should answer from personal experience
     (e.g. "describe the first time you set up a low-tech tank — what went wrong?")
   - These become the first-hand experience sections that differentiate us from AI-only content

8. COMPETITOR NOTES
   - What angle or gap can we exploit vs. generic results? (be specific)
```

---

## After running this prompt

- Save the brief as a comment or companion file alongside the draft.
- Paste the brief into **Workflow 3 (Draft Writer)** to generate the full article.
