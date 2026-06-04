# Workflow 7 — Pinterest

Two parts: **one-time setup** (do today) and the **per-article pin process** (weekly).

---

## Part A — One-time setup

### 1. Create a Pinterest Business account
Go to **pinterest.com/business/create**. Use a new account (don't convert a personal one if you use it privately).

Profile settings:
- **Name:** Mossy Tank
- **Username:** mossytank (or mossytankcom)
- **Bio:** Beginner-friendly planted aquariums & aquascaping. Low-tech, no CO2. Betta tanks, shrimp, nano setups. mossytank.com
- **Profile photo:** the Mossy Tank logo (or a clean cropped tank photo if no logo yet)
- **Website:** https://mossytank.com

### 2. Claim your website
Settings → Claimed accounts → Claim website → enter `mossytank.com`.
Pinterest will give you an HTML tag or meta tag. Add it to BaseLayout.astro inside `<head>`:
```html
<meta name="p:domain_verify" content="PINTEREST_VERIFICATION_CODE" />
```
Then redeploy. Go back to Pinterest and click "Claim." This unlocks analytics and Rich Pins.

### 3. Create boards (do all 6 now)

| Board name | Description (for Pinterest SEO) |
|---|---|
| Low-Tech Planted Tanks | No-CO2 planted aquariums for beginners. Setup guides, plant tips, and gear for easy planted tanks. |
| Planted Betta Tanks | Planted aquarium ideas for betta fish. Best plants, setups, and care tips for betta tanks. |
| Aquarium Plants & Care | Easy aquarium plants that thrive without CO2. Care guides for java fern, anubias, moss, and more. |
| Shrimp & Nano Tanks | Cherry shrimp and nano planted aquarium setups. Water parameters, plants, and beginner care guides. |
| Aquarium Troubleshooting | Fix cloudy water, algae, ammonia spikes, and dying plants. Aquarium problem-solving for beginners. |
| Beginner Aquarium Setup | How to set up your first freshwater aquarium. Tank cycling, equipment picks, and starter guides. |

Set each board to **Public**. Add a keyword-rich description to each — Pinterest uses these for search.

### 4. Create your Canva pin template

Open Canva → Create design → Custom size → **1000 × 1500 px** (2:3, the Pinterest standard).

Design two template variants — save both as templates you can duplicate:

**Template A — Text-heavy (for troubleshooting/how-to articles):**
- Dark or muted background (deep green, navy, or a blurred tank photo)
- Large bold headline at top (e.g. "5 Reasons Your Aquarium Plants Are Turning Yellow")
- Small Mossy Tank logo + "mossytank.com" at the bottom
- Simple, clean — no clutter

**Template B — Aesthetic/list (for gear guides and plant articles):**
- Beautiful tank/plant photo fills ~60% of the image
- Semi-transparent dark overlay on the bottom third
- Headline text in the overlay
- Mossy Tank branding at the bottom

Fonts that work: Playfair Display (headings) + Lato or Montserrat (body). Stick to 2 fonts max.
Colour palette: deep green (#2D5016), white (#FFFFFF), warm cream (#F5F0E8).

### 5. Enable Rich Pins (recommended)
Rich Pins pull your article title/description automatically from your site's meta tags.
Go to **developers.pinterest.com/tools/url-debugger** → paste a mossytank.com article URL → click "Validate."
Then apply for Rich Pins at the same page. Takes 24–48 hrs to activate.

---

## Part B — Per-article pin process

**Time per article: ~20–30 min.** Do this the same day you publish.

### Step 1 — Generate pin concepts (AI)
Use the Pinterest section of Workflow 6. Paste the article → get 5 pin concepts with:
- Pin title
- Pin description + hashtags
- Image concept
- Board assignment

Pick the **3 best** concepts (skip any that feel too similar to each other).

### Step 2 — Create pins in Canva
1. Open your saved Canva template → duplicate it 3 times
2. For each pin: swap the headline text + adjust the background/image based on the image concept
3. Use free Pexels/Unsplash images inside Canva for tank/plant photos if you don't have originals
4. Download each as **PNG** (File → Download → PNG)

Good image search terms for free photos: "planted aquarium", "aquascape", "betta fish tank",
"aquarium plants", "shrimp aquarium", "nano tank".

### Step 3 — Schedule on Pinterest
1. Go to pinterest.com/pin-builder → upload image
2. Paste the pin title + description from the AI output
3. Add your mossytank.com article URL as the destination link
4. Select the correct board
5. Click **Publish later** → schedule (see timing below)

**Don't post all 3 at once.** Space them out:
- Pin 1: day of publish
- Pin 2: 2 days later
- Pin 3: 4–5 days later

**Best posting windows (AEDT):** 9–11am or 8–11pm. Pinterest's US audience is largest, so
late afternoon US Eastern = morning or evening AEDT.

### Step 4 — Repurpose to group boards (later, Phase 2)
Once you have 20+ pins and traction, join aquascaping group boards on Pinterest and re-pin
your top performers there for extra reach.

---

## Hashtag strategy

Use **5–8 hashtags max** per pin. Mix:
- Broad: #plantedaquarium #aquascape #aquariumplants
- Mid: #lowtechplantedtank #bettafish #nanoaquarium
- Specific: #javafern #cherryshrimpcare #bettatank

Pinterest is more keyword/image-search driven than hashtag driven — don't over-index on hashtags.

---

## Weekly Pinterest cadence

| When | Task |
|---|---|
| Day you publish an article | Create + schedule 3 pins from that article |
| Each week | Check Pinterest Analytics — which pins got saves/clicks |
| Monthly | Create 2–3 "evergreen aesthetic" pins with no article (just beautiful tank photos pointing to homepage) |

**Volume:** 3–5 pins/day is the Pinterest algorithm sweet spot for a new account.
With 2–3 articles/week that gives you 6–9 new pins. Supplement with re-pins of your own
older content to hit the daily target.

---

## What success looks like on Pinterest

- Month 1: 0–50 monthly views (normal — account is new, trust is low)
- Month 3: 1,000–5,000 monthly views
- Month 6: 10,000–50,000 monthly views (if consistent)
- Month 12: 50,000–200,000+ monthly views → meaningful referral traffic

Pinterest traffic compounds differently from Google — one viral pin can send thousands of
visits in a day, often months after it was posted. Be consistent and patient.
