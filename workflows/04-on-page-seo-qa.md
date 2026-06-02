# Workflow 4 — On-Page SEO QA

**When to use:** After draft is written and edited (post your 20%). Run this before every
publish. Paste the finished article + this prompt.

**Fill in:** `[TARGET KEYWORD]`, `[PAGE TYPE]`, and paste the full article draft.

---

## Prompt

```
You are an on-page SEO auditor reviewing a draft for Mossy Tank (mossytank.com) before publish.

TARGET KEYWORD: [TARGET KEYWORD]
PAGE TYPE: [pillar | supporting-article | money-page | troubleshooting]
ARTICLE DRAFT:
[PASTE FULL DRAFT HERE]

Run a full on-page SEO QA. For each item, return: ✅ pass | ⚠️ needs fix | ❌ fail — and if
not passing, give the specific fix required (not just "add the keyword").

METADATA
- [ ] H1 contains the target keyword and is under 60 characters
- [ ] Title tag is unique, under 60 chars, keyword near the front
- [ ] Meta description is 120–155 chars, includes keyword, has a click hook
- [ ] URL slug is short (≤6 words), lowercase, hyphenated, includes keyword

CONTENT
- [ ] Target keyword appears in first 100 words naturally
- [ ] Secondary keywords used naturally throughout (not stuffed)
- [ ] No keyword stuffing or unnatural repetition
- [ ] Word count is appropriate for page type
      (pillar: 2,000–3,500 | supporting: 800–1,500 | money: 1,500–2,500 | troubleshooting: 600–1,200)
- [ ] Intro hooks immediately — no "In this article..." filler
- [ ] Paragraphs are short (≤4 lines); good use of bullet lists and subheadings
- [ ] At least one H2 or H3 contains the target keyword or a close variant
- [ ] All [EXPERIENCE] placeholders have been filled in by the operator
- [ ] No [AFFILIATE], [INTERNAL LINK], or [PHOTO] placeholders remain unfilled

INTERNAL LINKING
- [ ] 3–5 internal links to relevant site pages
- [ ] Anchor text is descriptive (not "click here")
- [ ] Links to at least one pillar page (if not itself a pillar)
- [ ] If a money page: links from at least one informational article back to it

E-E-A-T & TRUST
- [ ] Author/site expertise is evident (first-hand experience present)
- [ ] Any factual claims are accurate and could be verified
- [ ] Affiliate links are disclosed (disclosure component present on money pages)
- [ ] No YMYL health claims made without appropriate caveats

SCHEMA
- [ ] Correct schema type recommended for this page (Article / HowTo / FAQPage / ItemList)
- [ ] If FAQPage: at least 3 Q&A pairs are present and could be marked up
- [ ] If HowTo: steps are clearly numbered

TECHNICAL (check after publishing)
- [ ] Page loads in under 3 seconds on mobile
- [ ] All images have descriptive alt text with keyword where natural
- [ ] No broken links

FINAL VERDICT
Give an overall readiness score out of 10 and a one-line publish/hold recommendation.
List any ❌ items as blockers; ⚠️ items as nice-to-fix before or shortly after publish.
```

---

## After running this prompt

- Fix all ❌ blockers before publishing.
- Fix ⚠️ items within 48 hours of publishing if you skip them.
- Once published, paste the live URL into Search Console → URL Inspection → Request Indexing.
