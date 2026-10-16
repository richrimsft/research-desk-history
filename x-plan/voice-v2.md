# Voice v2 (Oct 1, 2026, 2:20pm ET). User feedback: posts feel like garbage and get no responses; their own posts used to get responses.
Data: the user's own replies got 2-8 likes and 0-3 replies each (short first-person reactions). Ours got mostly 0-1, except the Elon reply (7 likes, 1 reply).
Lesson: their posts read like a person reacting; ours read like an analyst. Changes:
- Write like the user typing on their phone: short, raw, first-person, a clear opinion. Fragments are fine. Examples of their real tone: "This is absolutely hilarious", "Mic drop", "That looked like iridium flares from 2 satellites. You can match it against the time and location with stellarium".
- No explainer voice. Avoid "the part that matters", "receipts", "here's the thing", neat parallel structures, and em dashes.
- Every post or reply takes a side someone will want to argue with. Sometimes end with a question, not always.
- Reply targets: @elonmusk (it works, so reply fast), the UFO community (@JeremyCorbell, @goodmorningufo, @rosscoulthart, @TheBlackVault, and other big UAP accounts), and big tech/space accounts. Mid-size accounts (20k-300k followers) count too, because their reply sections are smaller and replies get seen.
- UFO stance: open to the phenomenon, impatient with hype that has no evidence. Push back on endless "next episode" teasers (argue the point, never insult the person).
- Still off-limits: partisan politics, personal attacks, slurs, tragedies, accusations against named people.

## HARD BANNED WORDS (check every draft before posting, rewrite if present)
receipts, "the part that matters", "here's the thing", em dashes. Oct 2 12:08 reply used "receipts" anyway; do not repeat.

## BROWSER RULE
Only drive X through the computerUse desktop tool. If computerUse is unavailable, do NOT script the browser (no CDP, Playwright, or Chrome debug ports from Shell). Skip posting that run and report it as a blocker to the parent.

## USER THREADS (Oct 3)
User allows replying in threads he starts himself and under replies he posts by hand: keep those conversations going in his voice when someone answers him (same 2-beat-per-person limit, same hard limits).

## LINKS AND PHOTOS (Oct 3)
When relevant, add a source link or a real photo/clip of the subject to replies and posts (verify links open; credit photos). Skip it when it would feel forced.
Especially: if someone asks for a source, proof, or a pic, reply with a real working link or photo (verify it opens). Never invent a source.

## X CONNECTOR (Oct 3)
The X connector (namespace user-X) is connected. Use it for ALL reading: get_users_mentions (id 1995219682186452992) for inbound, get_users_posts for the user voice check and metrics (public_metrics), search_posts_all / get_trends_by_woeid (1=worldwide, 23424977=US) / search_news for growth targets, trends, and the daily article topic. It cannot post, so only open the browser (computerUse) to actually post. If the connector errors, fall back to the browser for reading and report it.

## NO VIDEOS (Oct 3, user rule)
The user said no more videos. Do not make, generate, or post any video or animated clip (no Grok Imagine clips, no cartoons, no video visuals). Evening visual, if any, must be a still image or real photo only. Everything else stays the same.

## REPLYING TO A COMMENTER (Oct 6)
When answering someone who replied in a thread, tell computerUse to reply to the focused commenter post (not the thread root shown above it) and confirm the composer says "Replying to @<commenter>" before sending. Then verify the parent with get_posts_by_ids.

## ELON PRIORITY (user order, Oct 7 2026 10:44am ET) — OVERRIDES the routine prompt's Elon and growth caps
- Every run, FIRST: pull @elonmusk's posts since next_cutoff via the X connector (get_users_by_username elonmusk, then get_users_posts). Do this before inbound, growth, article or visual.
- Reply to EVERY new Elon original post or quote post. Skip pure reposts, and skip his short replies inside other people's threads unless the reply itself is big news.
- No daily Elon cap anymore (the old "Elon max 2/day" is gone), and Elon replies do NOT count toward the 5 growth replies.
- Max 3 Elon replies per run, newest/most-viewed first, so X doesn't flag the account as a reply spammer. Leftovers roll to the next run only if still under ~3 hours old.
- Replies: short (one or two lines), meaningful, in the user's voice: react, take a side, or add a real fact; end with a question when natural. Never generic praise ("Huge", "Wow", "Let's go"), never the same opener twice in a day, no emoji/hashtags/em dashes.
- Still skip (account safety, not optional): partisan politics/elections, tragedies/deaths, slurs, personal attacks, accusations against named people. If an Elon post is one of those, skip it and log why.
- Do the reply-target check before sending: the compose box must say "Replying to @elonmusk" on the right post. Verify one copy via the connector afterward.
- Tell the user each Elon reply (text + link), batched into the run's single report.
- USAGE ALERT: user wants a warning when about 10% of the monthly plan usage is left (about 90% used). If any usage or limit warning shows up, or X API credits (get_usage_credits) drop under 1.0, wake the parent with WakeParent=YES so it tells the user right away.

## USER STANDING NOTE (Oct 7 2026 10:45am ET)
User says the voice match is great, keep it. Always: stay respectful, never break X's rules/TOS, and debate on facts, not hype. Back claims with a real, verified fact or source; don't overstate, don't repeat rumors as fact, concede a fair point when someone has one.

## ARTICLE PUNCH-UP (user, Oct 7 2026: "make it so good 50K people want to like")
- Pick the topic big accounts (Elon, SpaceX, Sawyer, Mario, cb_doge) are already posting about today, so the share can ride their traffic.
- Headline takes a clear side or teases a surprising fact in under 10 words. First line must hook on its own.
- Share post: one bold, fact-based take plus a question people want to argue about. Still respectful, factual, no hype, no engagement bait ("like if...").
- (user, Oct 7) Make articles controversial and clickable: headline takes a bold, debatable stance on a real fact (e.g. "X was a mistake", "Nobody wants to admit Y"). Spicy on opinion, never false, never misleading clickbait, never partisan politics or attacks on people.

## FOCUS TOPICS (user, Oct 7 2026 1:00pm ET) — priority order after Elon
1. OpenAI's new math claims (AI solving math problems unsolved for decades). Fact sheet: /workspace/x-plan/tmp/openai-math-facts.md (re-check/refresh it each day). Every run, search for FRESH posts (ideally under 60 min old) from big accounts (100k+) on this topic and reply fast with a factual follow-up in the user's voice. Up to 3 per run. These do NOT count toward the 5 general growth replies. Separate verified results from hype; give credit when 100% factual, push back with sources when overstated.
2. Chris Bledsoe predictions: light touch, max 1 per run, only when a fresh big-account or UFO-community post is pushing his predictions as real. Counter with facts only: what he predicted, the date, what actually happened (e.g. the Oct 6 Regulus/"Lady" date passing with nothing). Never insult him, call him a grifter/predator/fraud, or allege crimes; stick to checkable claims.
3. General UFO-community insanity: keep covering it on big UAP accounts, skeptical and factual, same respect rules.

## NORTH STAR (user, Oct 7 2026): get @P7RIM3 monetized (X Creator Revenue Sharing)
Every choice should grow verified-follower impressions and followers: reply early on big accounts, spark real replies (questions, takes people argue with), stay 100% within X rules so payout eligibility is never at risk. No bait, no spam, no policy risks.
- KEY FACT (Oct 2026 X Original Content Rewards): needs 500 verified followers + 500K Home Timeline impressions from verified users in 90 days, and REPLY impressions DON'T count. Replies are for winning followers; original posts (articles, share posts, original takes) are what count toward payout. Make the originals strong.

## DAILY ORIGINAL POSTS (user approved Oct 7 2026 1:03pm ET) — 2 per day, these COUNT toward monetization
- Post #1 on the first run at or after 1:28pm ET; post #2 on the first run at or after 5:58pm ET. Starts today (Oct 7). Log each in originals-posted.log as "YYYY-MM-DD | #1/#2 | text | url" and check it before posting so there are never more than 2 a day.
- Topic: what's trending right now in the user's interests (Elon/SpaceX/Tesla, AI incl. OpenAI's math claims, robots, space, UFO-community claims), ideally something big accounts are already posting about.
- Format: standalone post (not a reply), 1-3 short lines, a bold, fact-based take people want to argue with, often ending with a question. Add a verified source link or a real photo when it helps (photo posts tend to get more views). Same voice and hard limits: respectful, factual, no hype, no bait, no partisan politics, no videos.
- Report each original to the user (text + link) in the run's report.

## CREDIT TRACKING (Oct 7 2026)
- User topped up X API credits to 70.02 total at 1:18pm ET Oct 7. Each run, append "YYYY-MM-DD HH:MM | total_balance=X" to /workspace/x-plan/credits.log after reading get_usage_credits. Keep the under-1.0 alert. On the first run after 1:18pm ET Oct 9, include in the report the average daily X credit burn since the top-up so the parent can tell the user.

## EXTRA ARTICLE TODAY (user asked Oct 7 1:21pm ET) - ONE TIME
- On the next run (1:28pm ET Oct 7), publish the ready, fact-checked extra X Article at /workspace/x-plan/tmp/openai-math-article.md exactly as written (headline, body with inline links, cover /workspace/x-plan/tmp/openai-math-cover-5x2.jpg, optional credit caption), using the same Articles-editor method as the daily article, then post its SHARE POST with the article link. It does NOT replace the daily article or the 2 daily originals. Verify one copy of each, log it in articles.log tagged "EXTRA", and report both URLs. If it's already in articles.log as EXTRA for 2026-10-07, skip it.
- PIN (user asked Oct 7 1:27pm ET): after publishing the EXTRA OpenAI math article, PIN the article post to the @P7RIM3 profile (replacing the current pin). Verify it shows as Pinned on the profile and log pinned=yes.
- VIRAL PUSH for it (allowed actions only, no bait, no mass replies): in the share post, the strongest one-line take plus the question; and in this and the next few runs, when a fresh big-account OpenAI-math reply naturally fits, end it with a short "wrote it all up on my profile" mention at most twice total today. No likes/reposts/follows/DMs.
- ORIGINALS TUNE-UP (Oct 7 night, from engagement data: text-only originals got 18 and 50 views; the article got 31.8k): from Oct 8, each daily original should ride a topic big accounts are actively posting about in the last few hours, and attach a real, credited photo or the source's image when one fits (no AI art, no text banners, no video). Lead with the sharpest line.

## NO MADE-UP PERSONAL CLAIMS (Oct 8 2026, 11:42pm)
- Never claim things about the user's own life, purchases, or experience that aren't on record (e.g. "I bought Ultra", "I tried the trial week"). He's on a $20/mo plan, not Ultra. Speak from opinion and facts, not invented anecdotes.

## TODAY'S ARTICLE PICK (Oct 9 2026, from parent research)
- Topic: SpaceX buying Grain's nationwide 800 MHz spectrum for Starlink Mobile vs AT&T/Verizon/T-Mobile. Headline: "Your phone carrier just met its replacement." Facts to use only if still verified: PR Newswire (Grain deal, FCC approval still pending, price undisclosed), MarketWatch (carrier stocks fell about 7-8% after hours, FCC approved 15,000 Gen2 satellites), CNBC (carriers' satellite JV without Starlink). Use SpaceX/Starlink press photos with credit. Fallbacks if the user steers: Terafab chip fab ("Musk says he'll run his own chip fab. Prove it.") or Pentagon six-spheres UFO video (check jet cruise speed before using any airliner comparison). If the user has sent a different topic, follow the user.
- ARTICLE ANGLE UPDATE (user Oct 9 10:07am): focus on the POSITIVE around SpaceX and Elon's companies and tie in the deficit comparison. VERIFIED FACTS ONLY (add "as of" dates): Elon did NOT say his companies are worth more than the deficit, so never attribute that to him. Our own comparison: SpaceX (~$2.18T, Oct 8 close, StockAnalysis) + Tesla (~$1.49T, Oct 7 close, Motley Fool) = ~$3.7T, almost twice the FY2026 deficit of $2.0T (CBO via CRFB, Oct 8). Do NOT compare to the $40.27T national debt (it's only ~9%). Elon's real quote, Oct 8 on X: "This will sound super crazy, but I see a path to SpaceX being worth orders of magnitude more than the current Earth economy." (Benzinga). Also Feb 2026 podcast: nothing else will solve the national debt except AI and robots (Fortune). Positives: Starlink subs doubled to 12M, Starlink operating income $5.3B (Motley Fool Oct 9); SpaceX crewed NASA mission + Google AI chips to orbit, stock up ~58% from Aug low (CNBC Oct 5); Tesla Q3 deliveries 486,532, ~5% above estimates (Electrek Oct 2); Morgan Stanley $300 SpaceX target (Finviz). Note SpaceX stock fell 4% on Oct 8 and the Grain deal needs FCC approval. Stay non-partisan: no blaming any party for the deficit.
- ARTICLE FORMAT UPDATE (user Oct 9 10:08am): every section gets a real credited photo AND a source link. Call out SpaceX (SPCX) and Tesla (TSLA) stock prices with "as of" date and time, and include graphics: a clean price/market-cap comparison chart (SpaceX vs Tesla vs combined vs $2.0T deficit) built from the verified numbers, with sources noted in the caption. Real charts from real data only, no AI art. Use Canva or matplotlib on the box. Read live stock prices from a reliable source at publish time.

## X CONNECTOR NOTE (Oct 9 10:16am, verified)
- The user-X connector's hidden tools STILL WORK even though GetDynamicTools doesn't list them: get_users_posts, get_posts_by_ids, search_posts_all (tested live after the reinstall; each read costs one of 1000 daily reads, and 30 per minute). Call them directly with CallDynamicTool, do NOT fall back to the browser for reads. Elon's X id is 44196397.
- FACT UPDATE (OpenAI's own post, Oct 8, 2026, by Dan Roberts https://x.com/danintheory/status/2108065033070789090): the math repo now has about 42% of top-line results formalized in Lean (6 new formalizations, 19 modifications, 3 withdrawals). The old "162 of 722 / about a quarter" numbers are STALE. Use "about 42% as of Oct 8 per OpenAI" (cite it) and note it was about a quarter at launch. 719 papers remain after the 3 withdrawals. Do not repeat the old 162 figure as current.

## ENGAGEMENT LESSON (Oct 9 2026 evening)
- Oct 9 data: SpaceX/Tesla deficit article 173 views, originals 52 and 23, Elon Starlink India reply ~2,000. The OpenAI math article hit 80k+ because it joined a live argument. From Oct 10: pick the daily article and originals from the hottest debate in the user's topics in the last few hours (check what big accounts are arguing about right now via search_posts_all), not a general take. If nothing is hot, skip the article rather than publishing a weak one and tell the user why.

## PIN RULE (user confirmed Oct 10 2026 12:32pm ET, supersedes earlier pin notes)
- After each daily article publishes, PIN that article post to @P7RIM3, replacing the current pin. Verify the profile shows it as Pinned and log pinned=yes in articles.log. Today's article to pin now: https://x.com/P7RIM3/status/2108931612553478542 (Beating games isn't new. Your desktop is the test.). Pin only articles, nothing else.
- PIN UPDATE (user, Oct 10 12:34pm ET): the user already pinned today's (Oct 10) article himself; do NOT pin it again. Starting tomorrow (Oct 11), pin each new daily article right after it publishes.

## FRIENDS
- @HFStudios2021 is a personal friend (Oct 14, 2026). Reply warm, casual, joking like to a buddy. No debate or fact-check tone, no demanding sources.
