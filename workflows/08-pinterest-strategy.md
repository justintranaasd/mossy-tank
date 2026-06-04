# Workflow 8 — Pinterest Growth Strategy

**When to use:** Review at Month 3–4 when you have 40+ articles and Pinterest is
starting to show impressions. The early-stage playbook is at the bottom — follow
that now, come back to the full strategy later.

---

## The foundational insight

**Pinterest is a visual search engine, not a social platform.**

People search "low tech planted tank" or "why are my aquarium plants turning yellow"
and look for answers. Follower count barely matters. Posting time barely matters.
Going viral on social has nothing to do with Pinterest success.

The game: show up in search results for the right keywords, with an image that stops
the scroll, and a headline that earns the click.

---

## Account setup (one-time)

**Profile name:** Include keywords, not just the brand name.
> Mossy Tank | Planted Aquarium Ideas & Care

**Bio:**
> Beginner guides for low-tech planted tanks, betta fish, and shrimp aquariums.
> No CO2 needed. mossytank.com

**Boards — keyword-rich names, all with 2–3 sentence descriptions:**

| Board | Purpose |
|---|---|
| Low Tech Planted Aquarium Ideas | Core keyword, high volume |
| Planted Betta Tank Ideas | #1 entry keyword in the niche |
| Aquarium Plants for Beginners | Beginner funnel |
| Shrimp Tank Ideas | Neocaridina audience is active on Pinterest |
| Aquarium Troubleshooting Tips | Problem-solvers click hard |
| Beginner Aquarium Setup | Gift buyers + total beginners |
| Aquascape Inspiration | Save-magnet for the aesthetic crowd |

Pinterest indexes board names and descriptions — treat them like meta descriptions.

---

## Two types of pins (run both simultaneously at scale)

**Type A — Save Magnet (builds reach)**
- Beautiful, aspirational image. Minimal text.
- People save it → algorithm treats it as quality → wider distribution.
- Goal: saves and impressions, not clicks.
- Use for: aesthetic tank shots, "inspiration" angles.

**Type B — Click Driver (sends traffic)**
- Educational, problem-solving, or curiosity-gap headline.
- Goal: link clicks back to the article.
- Use for: troubleshooting, how-tos, numbered lists, buyer guides.

**Ratio at scale:** 40% Save Magnets, 60% Click Drivers.
The Save Magnets feed the algorithm so Click Drivers get distribution.

**Early stage (now):** Run Click Drivers only. Every pin should earn a click.
Add Save Magnets once you have 40+ pins and are optimising for reach.

---

## Pin design rules

- **Vertical 2:3 (1000×1500px)** always
- **Bottom text** — let the image be the hero first, text anchors at the bottom
- **Left-aligned** headline feels editorial, not generic
- **DIN Condensed Bold** for the headline (clean, modern, readable small)
- **Category badge** ("BEGINNER GUIDE", "LOW-TECH TANKS") above headline
- **Dark gradient** from bottom, white text, high contrast
- **8 words max** in the headline
- **mossytank.com** bottom centre

**Headlines that convert:**
- Curiosity gap: "The #1 mistake beginners make with aquarium plants"
- Problem-solving: "Why your plants keep dying (and how to fix it)"
- Numbered lists: "5 plants that thrive with zero effort"
- Permission: "You don't need CO2 for a beautiful planted tank"

**Images that stop the scroll in this niche:**
- Single stunning plant or fish as a clear hero (not a wide busy tank shot)
- Before/after (algae tank → clear planted tank)
- Close-up plant textures (moss, java fern fronds)
- Betta fish swimming through plants (highest emotional pull)

---

## Keyword research

Do it inside Pinterest itself:
1. Type your seed keyword into the Pinterest search bar
2. Note the bubble suggestions that appear below — these are real, high-volume searches
3. Use these exact phrases in pin titles, descriptions, and board descriptions

Key seeds to research: "planted aquarium", "aquarium plants", "betta tank", "low tech aquarium",
"aquarium for beginners", "shrimp tank", "nano aquarium"

**Hashtags:** 3–5 specific ones only. #plantedaquarium #lowtechaquarium #beginnertank.
Never generic (#plants). Less weight than they used to have but still useful for initial
distribution.

---

## Posting cadence

**New account (now–Month 6):** 2 pins/day, every day. Consistency over volume.
**Month 6+ (scaling):** 3–5 pins/day once you have a production system.

- Use Pinterest's native scheduler — free, schedule 1–2 weeks ahead
- Pin each article to 2–3 relevant boards (not spam — correct categorisation)
- Space out pins to the same URL across different days
- Best window for US audience (biggest Pinterest market): schedule for 8–11pm US Eastern
  = 11am–2pm AEDT / 10am–1pm AEST

---

## The algorithm

1. Pinterest distributes new pins to a small test audience first
2. If they save or click → wider distribution
3. If not → pin dies quietly

Every pin gets **one real shot.** This is why quality beats quantity.

Keywords feed the algorithm from four places:
1. Pin title
2. Pin description (first 100 characters matter most)
3. Your article title/content (Pinterest reads the landing page)
4. Board name and description

---

## What to measure

**Ignore:** follower count, monthly views (vanity)

**Watch weekly:**
- Link clicks (the only number that pays you)
- Outbound click rate (link clicks ÷ impressions — above 0.5% good, 1%+ excellent)
- Top pins by clicks (double down on whatever format is winning)

**Monthly:**
- Which boards generate the most clicks → focus content there
- Which headline formats are winning → replicate the pattern

---

## Realistic timeline

| Month | Expectation |
|---|---|
| 1–2 | Near-zero traffic. Normal. Pinterest is learning the account. |
| 3–4 | First impressions spike. 5–20 site visitors/week from Pinterest. |
| 6 | If consistent: 50–200 visitors/week. Pins starting to compound. |
| 9–12 | If a pin goes semi-viral: 500–2,000+ visitors/week. |

The biggest risk is quitting in month 2. That's when the foundation is being laid.

---

## Current playbook (early stage — follow this now)

Given time constraints and site being brand new:

1. **2 pins per article** (1 problem/solution + 1 numbered list angle)
2. **2 pins/day** scheduled — sustainable, not burnout-inducing
3. **Click Drivers only** — every pin earns a click, no Save Magnets yet
4. **Max 1 hour/week** on Pinterest total
5. **Don't batch all pins upfront** — build 2 pins for each new article as you publish,
   then go back and do existing articles one batch at a time as Ideogram credits allow
6. **Skip for now:** group boards, Idea Pins, video pins, Save Magnets, hashtag optimisation

**The leverage point:** every new article feeds both Google and Pinterest simultaneously.
Writing is the highest-value activity — Pinterest is the distribution layer running in
the background.

---

## Pin production workflow (per article)

1. Run Workflow 6 Pinterest prompt → 2 pin concepts (problem/solution + list)
2. Generate clean aquarium background in Ideogram (background only, no text)
3. Run: `python3 /Users/justintran/side/mossy-tank/tools/make-pin.py <image> "Headline" "BADGE"`
4. Schedule on Pinterest with keyword-rich description + 3–5 hashtags
5. Pin to 2 relevant boards
6. Time per article: ~20 minutes
