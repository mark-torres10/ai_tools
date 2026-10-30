# Five Principles for Generating Readable AI Text in Bulk

**Author:** Shreya Shankar  
**Published:** Oct 29, 2026  
**Source:** https://fsdatalab.github.io/blog/agent-text-at-scale/

Reference summary for the Full Stack Data Lab checklist on making large feeds of AI-generated text easy to read (dashboards, sidebars, notification stacks, generated web pages, and similar list-like UI copy).

## The problem

Modern products expose humans to AI-generated text at unprecedented scale: agent session sidebars (Claude Code, Codex), grouped notification summaries (Apple Intelligence), temporary dashboards and web pages, and other feeds.

Those feeds are hard to read because items must be **predictable** and **consistent** for people to scan many of them quickly.

## Checklist overview

Five principles:

1. Match how human readers parse sentences (NVN).
2. Put the most important words first (F-shaped scanning).
3. Use the same structure and the same vocabulary in every item.
4. Use variation only to show a meaningful difference (expressiveness).
5. Align the connotation of verbs with the purpose of the dashboard.

---

## 1. Match how human readers parse sentences

English readers often use the **NVN strategy** (Thomas Bever, 1970): first noun = subject, next verb = action, next noun = object. Example: in “The agent fixed the login bug,” readers take “agent” as subject, “fixed” as action, “bug” as object.

Non-NVN order forces **re-parsing**. Example: in “Login bug fixed by the agent,” readers first read “bug” as subject and “fixed” as its action (as if the bug fixed something). Only at “by the agent” do they find the real subject and parse again.

**Procedure for a list of items:**

1. Start each item with its subject or its verb. If the subject is the same in all items, drop it and start with the verb.
2. Put the first verb of each item in the tense that matches reader expectations: past, continuous, or future.

### Example: agent session sidebar titles (Figure 1)

Context: Claude sidebar session titles mix noun phrases, gerunds, and imperatives. All sessions share the same subject (the agent), so each title should start with a verb. Because sessions are active, use **continuous** form (e.g., “Measuring vLLM performance”).

**Before (as written):**

| Group | Title |
| --- | --- |
| Pinned | KV persistence across queries |
| Today | vLLM performance on eviction queries |
| Today | Nemotron-3.5-Parse on OfficeQA benchmark |
| Yesterday | Liquid 1.7B model integration |
| Yesterday | Quail grant application strategy |
| Yesterday | Fine-tune model on personal writing |
| Oct 26 | Switching to main and fast-forwarding |

**After (rewritten):**

| Group | Title |
| --- | --- |
| Pinned | Persisting KV across queries |
| Today | Measuring vLLM performance on eviction queries |
| Today | Running Nemotron-3.5-Parse on OfficeQA |
| Yesterday | Integrating Liquid 1.7B model |
| Yesterday | Planning Quail grant application |
| Yesterday | Fine-tuning model on personal writing |
| Oct 26 | Switching to main and fast-forwarding |

---

## 2. Put the most important words first

Jakob Nielsen’s eye-tracking work: readers scan web pages in an **F shape** (start of each line, skip the rest). List readers often see only the **first two words** of each item.

**Procedure:**

1. Find the words that make each item different from the other items.
2. Move those words as close to the start of the item as possible.

### Example: order email subjects (Figure 2)

**Before (status last — every subject starts the same):**

- Your order #1001 has been delivered — Oct 27
- Your order #1001 has shipped — Oct 25
- Your order #1002 has shipped — Oct 24
- Your order #1001 is confirmed — Oct 23

**After (status first, as in Amazon order emails — first word distinguishes emails):**

- Delivered: "Bounty Essentials..." — Oct 27
- Shipped: "Bounty Essentials..." — Oct 25
- Shipped: "Desk lamp..." — Oct 24
- Ordered: "Bounty Essentials..." — Oct 23

Contrast called out in the post: bad pattern `Your order #1001 has shipped.` vs Amazon pattern `Ordered: "Bounty Essentials..."`.

---

## 3. Use the same structure and the same vocabulary

Parallel structure speeds reading (Frazier et al., 1980s): the second clause in “X and Y” is read faster when it matches the first (both active or both passive). Same idea for list items: each item reads faster when it shares structure with prior items.

One concept → one word (ASD Simplified Technical English: “one word, one meaning”; Nielsen consistency heuristic).

**Procedure:**

1. Use one structure in every item.
2. Use one word for each concept.

### Example A: Notion AI summaries of GitHub issues (Figure 3 — bad)

Notion AI autofill on 10 public `ollama/ollama` issues. Summaries are hard to skim: inconsistent openings (“The issue reports that,” “The page reports,” or an action like “Pressing Ctrl+C”) and mixed terms (“issue” vs “page”) for the same kind of row.

**Row 1**

- Issue title (abbreviated): Claude Desktop Conversation: ~17K initial prefill, HTTP 500 retries, MLX cache loss (0.40.11–0.40.12)
- Summary start: **The issue reports that** Claude Desktop Conversation experiences a long (~70–90 s) initial prefill of ~17 K tokens, frequent HTTP 500 errors, and cache loss on MLX versions 0.40.11–0.40.12, despite later messages being faster.

**Row 2**

- Issue title: `ollama show --modelfile` writes a Modelfile that `ollama create` rejects when a SYSTEM/TEMPLATE/LICENSE/MESSAGE value contains `"""` followed by whitespace
- Summary start: **The issue reports that** `ollama show --modelfile` incorrectly wraps values containing triple quotes followed by whitespace, causing unparseable Modelfiles that fail to recreate the model.

**Row 3**

- Issue title: Error reading GGUF metadata on large MoE model with MXFP4 format
- Summary start: **The page reports** an error reading GGUF metadata for a large MoE model in MXFP4 format due to an oversized unsupported tensor, references a similar bug, and includes a link to the related GitHub issue.

**Row 4**

- Issue title: `ollama run`: Ctrl+C during `"""` multiline input leaves session in multiline mode, so later input is swallowed or saved as the system message
- Summary start: **Pressing Ctrl+C** while entering a `"""` multiline message in `ollama run` clears the buffer but leaves the REPL in multiline mode, so the following input is mistakenly treated as a continuation or system message.

### Example B: Perplexity Discover headlines (Figure 4 — good)

Same structure in every headline: **subject + present-tense verb + object**. Examples from Oct 28, 2026:

- Bank of Canada hikes rate to 2.5%, first since July 2023
- Brewers beat Rays in Game 5 for first World Series title
- Weil Gotshal to wind down after partner exodus
- HHS lets pharmacies make six unapproved peptides

(Also satisfies principle 1.)

---

## 4. Use variation only to show a meaningful difference

From Jock Mackinlay (1986): **expressiveness** — a chart should show all facts in the data and only those facts. If one bar is red, readers assume color means something; variation should encode a meaningful variable.

Apply to text lists: if one item differs in length, structure, or wording, readers assume that difference **means something**.

### Example: Duolingo App Store theme dashboard (Figure 5)

Claude `data:analyze` on 100 recent US App Store reviews (Oct 26–27, 2026). Left: Claude’s version (5 of 11 themes). Right: rewritten with one template plus a bar chart for review counts.

**Problem (Claude’s version):** Each card adds a different kind of detail. Only the bugs card names app version **7.146.0**; only the energy card notes reviews in **Russian and Turkish**. Readers cannot tell if those details are significant (e.g., is 7.146.0 the only buggy version? do other themes come only from English reviews?).

**Fix (authors’ version):** Same components on every card — what users say, then one example. Encode “how many reviews” in a bar chart instead of uneven inline detail.

#### Theme: Fun, easy, and effective learning (74 reviews)

**Before (Claude):**

> Most reviews praise Duolingo as fun, easy, and helpful for learning, often in short 5-star notes. Users cite new vocabulary, pronunciation help, self-paced lessons, and being able to talk with family or friends. Spanish is the most named language, followed by Japanese, Italian, Korean, German, and others. Several of these reviewers still raise a complaint, such as energy limits or cost.

**After (authors):**

> Users love that the app is fun and helps them learn, e.g., new vocabulary and pronunciation.

#### Theme: Chess, music, and math courses (12 reviews)

**Before (Claude):**

> Chess is a popular new draw, and some users mention music, piano, and math too. Feedback is mostly positive, but there are specific complaints: a checkmate rule that seems wrong, no way for skilled players to skip ahead, a distracting new owl voice and hard-to-see pieces in the chess puzzle, and many clicks between games.

**After (authors):**

> Users enjoy the new courses but complain about problems, e.g., a checkmate rule that seems wrong.

#### Theme: Bugs and technical problems (9 reviews)

**Before (Claude):**

> Reports include voice answers not registering, the app freezing (one user lost a streak), the app crashing on launch, finished lessons not counting, leaderboard members disappearing, a new event missing for one family-plan member, and a shared iPad starting a new learner at the wrong level. Most come from the current version, 7.146.0.

**After (authors):**

> Users complain about bugs that cost them progress, e.g., a freeze that lost a daily streak.

#### Theme: Energy and battery limits on lessons (8 reviews)

**Before (Claude):**

> The energy (battery) system, and the older hearts system, limits how much users can practice. Users say they run out fast, must wait or watch ads, and see it as a push to buy Super. Some reviews are in Russian and Turkish, so the complaint shows up across markets. One user suggests earning energy by doing chess, music, or math.

**After (authors):**

> Users complain that they run out of energy fast and must wait to keep practicing.

#### Theme: New language requests (3 reviews)

**Before (Claude):**

> Users ask for new courses. Two ask for Icelandic, noting that Duolingo already offers other Nordic languages, and one asks for Elvish from The Lord of the Rings.

**After (authors):**

> Users request new courses, e.g., Icelandic.

**Bar chart (authors’ version — reviews per theme):**

| Theme | Count |
| --- | ---: |
| Fun, easy, and effective learning | 74 |
| Chess, music, and math courses | 12 |
| Bugs and technical problems | 9 |
| Energy and battery limits on lessons | 8 |
| New language requests | 3 |

---

## 5. Align the connotation of verbs with the purpose of the dashboard

Dashboards often surface one kind of information (complaints, praise, what is going well). Verbs should make that purpose obvious: negative verbs like “complain” on complaint dashboards; positive verbs like “love” on praise dashboards. Strong connotation helps skimming readers grasp each item quickly.

### Example (Figure 5, chess theme)

**Before (Claude):** Opens with “Chess is a popular new draw,” while most of the card lists complaints — readers cannot tell at a glance if the theme is good or bad news.

**After (authors):** Each card starts with a verb of obvious sentiment, e.g. **“Users love”** for praise and **“Users complain”** for problems, so readers can tell praise vs complaint from the verb alone.

---

## Takeaways

These five principles make bulk AI-generated text easier to read. The post uses dashboard-like examples but applies the checklist to **any** AI-generated artifact or product (including websites). Use the checklist when editing list-like prose, sidebar titles, notification summaries, card feeds, and similar repeated UI copy.

---

## When to apply in a writing cleanup pass

Use this reference when the target text is or contains:

- Lists, feeds, cards, or repeated rows meant to be scanned quickly
- Session titles, email subjects, table autofill summaries, or headline-style items
- Mixed sentence openings, mixed vocabulary for the same concept, or uneven detail across parallel items

For continuous prose (essays, README sections, PR descriptions), still apply principles 1–3 where list fragments appear, but prioritize the other cleanup passes for flow and anti-slop patterns.
