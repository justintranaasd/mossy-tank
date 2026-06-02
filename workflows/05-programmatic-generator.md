# Workflow 5 — Programmatic Page Generator

**When to use:** Phase 2 onwards. For each row in the plant/fish/shrimp dataset, run this
to generate non-thin, unique page content. Do a pilot batch of 10 first and QA before scaling.

**Fill in:** paste the dataset row as JSON, and set `[PAGE TYPE]`.

---

## Dataset schema (reference)

Each row in `src/content/plants/` should include:
```json
{
  "commonName": "Java Fern",
  "scientificName": "Microsorum pteropus",
  "difficulty": "easy",
  "light": "low",
  "co2": "not required",
  "growth": "slow",
  "placement": "midground / background",
  "maxHeight": "20–35cm",
  "temperature": "18–28°C",
  "ph": "6.0–7.5",
  "substrate": "attach to hardscape (rhizome must not be buried)",
  "propagation": "rhizome division / adventitious plantlets",
  "tankMates": ["betta", "shrimp", "nano fish", "community fish"],
  "commonProblems": ["brown spots (too much light)", "slow growth", "rhizome rot if buried"],
  "affiliateProducts": ["fluval plant substrate", "seachem flourish", "zoo med nano light"],
  "internalLinks": ["low-tech-planted-tank-beginners-guide", "planted-betta-tank"]
}
```

---

## Prompt

```
You are a content writer for Mossy Tank (mossytank.com), a beginner-focused aquascaping site.
Write a complete, non-thin plant/species care guide page using the data below.

DATASET ROW:
[PASTE JSON ROW HERE]

PAGE TYPE: [plant-care | fish-care | shrimp-care]

Requirements:
- Write 400–700 words of genuine, useful prose — not just a data table regurgitated
- Structure:
  1. Opening paragraph: what makes this species great for beginners (or who it suits)
  2. Care stats card (format as a markdown table: parameter | value | beginner-friendliness)
  3. H2: Setup & Placement — practical advice beyond just the numbers
  4. H2: Common Problems & Fixes — specific to this species, not generic
  5. H2: Tank Mates — which combinations work well and why
  6. H2: Where to Buy — 1 short paragraph with [AFFILIATE: product] placeholders
  7. Closing CTA: link to the most relevant pillar page using [INTERNAL LINK: page-slug]

- Tone: warm, practical, encouraging — like advice from an experienced hobbyist
- Every page must feel unique — vary sentence structure, opening hooks, and emphasis
- Do NOT pad with filler. 400 good words beats 700 generic words.
- Flag with [THIN RISK] if any section feels too generic to add real value

Output the page content in MDX format, ready to save as a .mdx file in src/content/plants/.
Include frontmatter:
---
commonName: [value]
scientificName: [value]  
difficulty: [value]
light: [value]
co2: [value]
draft: false
---
```

---

## QA checklist before scaling (run on first 10 pages)

- [ ] Each page reads differently — no copy-paste feel between species
- [ ] Care stats are accurate (cross-check one or two against a trusted source)
- [ ] No `[THIN RISK]` flags remaining
- [ ] Internal links resolve to real pages
- [ ] Affiliate placeholders replaced with real tracked URLs
- [ ] Run a sample through Workflow 4 (On-Page SEO QA) with the species name as target keyword
- [ ] Check schema validates at schema.org/validator

Only scale to 50+ pages once the pilot batch passes QA.
