I'll compile everything into one clean deliverable. Since this is a pure synthesis task from the inputs provided (no new file investigation needed — the critics already verified against the live repo), I'll produce the master markdown directly.

# Camelot Flows — "Found & Converting" Homepage Relaunch: Master Deliverable

This document compiles the positioning rewrite, tri-lingual copy, SEO, structured data, blog posts, and an exact apply-map. Critics' fixes are applied inline. Real open decisions are surfaced as flags — nothing was silently dropped.

---

## ⚠️ Decisions needed

These require a human call before anything ships. They are ordered highest-leverage first.

### 1. Pricing — tier names, prices, and the 4→3 collapse `[FLAGGED — CLIENT CONFIRMATION]`

The new frame collapses **4 public tiers → 3 "Found" tiers + 1 optional care line**. Confirm the names and the numbers below. **No new price may propagate to live JSON-LD or meta until locked** — keep the old confirmed numbers live until then.

| Tier (new) | Replaces (old) | Proposed price | Status |
|---|---|---|---|
| **Found Core** | €690 Merlin Automation | **from €690** | `NEEDS CONFIRMATION` |
| **Found Standard** ⭐ | €990 Ecommerce/Advanced WP | **from €990** | `NEEDS CONFIRMATION` |
| **Found Premium** | €1,200+ Custom Premium (nudged up) | **from €1,400+** | `NEEDS CONFIRMATION` |
| **Visibility Care** (optional, not a tier) | net-new | **from €90–150/mo** | `NEEDS CONFIRMATION` |
| ~~€390 Launch + chatbot~~ | retired from homepage | private "single landing page" only | DECISION: confirm retirement |

**Rationale (for the call):** Dropping €390 as a public anchor is the single highest-leverage move — a low anchor + chronic undercharging is what drags the premium frame down. Leading with €690 makes "Found Core" the floor. Merlin/automation folds *into every tier* as the convert/follow-up layer (no longer a standalone priced product). The standalone Merlin page survives as an upsell, not a homepage tier.

### 2. hreflang reality — RO/RU multilingual SEO has no URLs to live at `[FLAGGED — BLOCKER]`

The site is **client-side JS i18n at a single URL**. Homepage hreflang currently points `en`/`ro`/`ru` all at the identical `https://camelotflows.dev/` — which is invalid; Google sees only the EN DOM. **Every RO/RU `<title>`/`<description>` in this deliverable is unshippable as meta until this is resolved.** Pick one:

- **(A) Cheap & honest (recommended now):** Drop the `ro`/`ru` hreflang lines. Keep only `hreflang="en"` + `x-default` → `/`. The RO/RU keyword packs and metas become **body-copy + future-roadmap assets**, not shipped `<head>` meta.
- **(B) Correct & expensive (separate project):** Pre-render `/ro/` and `/ru/` paths (or server-rendered `?lang=` meta) and point hreflang there. This is real engineering work — scope it separately; do not pretend the copy deliverable solves it.

### 3. Fate of the 4 standalone tier landing pages `[FLAGGED]`

`launch-site.html`, `merlin-automation.html`, `ecommerce-wp.html`, `custom-premium.html` all exist and are each linked from the old pricing cards (plus nav/footer/sitemap). Collapsing to 3 cards requires deciding, per page: **keep / merge / 301 / noindex.** Note likely **cannibalization between `launch-site.html` and `service-creation.html`** on the core keyword (`creare site web` / "website that converts") — pick a canonical winner and 301/noindex the loser.

### 4. Live-site boundary violations that must change with this copy `[FLAGGED]`

Two existing strings contradict the new no-results boundary and sit on the homepage:

- **Footer tagline** `common.footer.location_line_3` = "Mission: Premium builds. **Measurable results.**" (`index.html:1484`) — "Measurable results" is exactly the outcome-promise the boundary disavows. **Must change** (proposed: "Premium builds. You own the asset.").
- **Testimonial** "**Lead volume is noticeably up**" (`index.html:1398`) — a third-party quote, defensible as *evidence* not *claim*, but it sits in tension with "I don't promise traffic." **Conscious keep/cut decision needed** (lower severity).

### 5. Hero word-split for RO/RU `[FLAGGED — minor]`

`wrapLetters()` must handle the RO `&`/space (`Găsit &`) and Cyrillic. Fallback if the splitter chokes: RO → `Găsit` / `Convertește`; RU → `Находят` / `Продаёт`. Confirm at build.

### 6. Schema location signal `[FLAGGED]`

Decide: keep locality-only `address` (Chișinău, MD — true, recommended) and **drop `geo` GeoCoordinates** (a remote atelier has no walk-in office; city-center coords imply a visitable place). Also confirm real `sameAs` LinkedIn/Facebook URLs, logo/og-cover paths, and `priceRange`.

---

## Homepage copy rewrite

Every changed i18n key, all three languages. `html:` prefix means the value is an HTML string (renders as innerHTML). Prices remain `[NEEDS CLIENT CONFIRMATION]`.

> **Key-schema warning (from i18n-sync + critic):** The deliverable below uses `sw_c*_name` / `sw_c*_badge` / `sw_c*_li` for readability, but the **live codebase uses a different schema**: `sw_c1_title`, `sw_c1_sub`, `sw_c1_desc`, `sw_c1_li1`…`sw_c1_li4`, `sw_c1_delivery`, `sw_c1_kicker`, `sw_c1_cta`. There is **no `_name`, no `_badge`, and no single `_li` blob**. The implementer must remap (see Apply-map). `sw_c2_badge` is a genuinely **new** key to add.

| KEY | EN | RO | RU |
|---|---|---|---|
| `meta_title` | Get Found, Get Chosen, Own It \| Camelot Flows | Ești găsit, ești ales, e al tău \| Camelot Flows | Вас находят, вас выбирают, сайт ваш \| Camelot Flows |
| `meta_description` | A premium website set up to be found on Google and built to convert — for the searches that pay. One fixed price, then it's yours. No retainer. | Un site premium, pus la punct ca să fie găsit pe Google și construit ca să convertească — pentru căutările care aduc bani. Un preț fix, apoi e al tău. Fără abonament. | Премиальный сайт, настроенный так, чтобы вас находили в Google, и собранный, чтобы продавать — по тем запросам, которые приносят деньги. Одна фиксированная цена — и сайт ваш. Без абонентской платы. |
| `hero_badge` | Solo atelier · Chișinău → worldwide | Atelier solo · Chișinău → în toată lumea | Авторская студия одного мастера · Кишинёв → по всему миру |
| `hero_word_1` | Found & | Găsit & | Находят |
| `hero_word_2` | Converting | Convertește | Продаёт |
| `hero_p` | I build you a website that's set up to be found on Google for the searches that actually make you money — and built to turn those visitors into bookings. Then it's yours. No retainer, no middleman. | Îți construiesc un site pus la punct ca să fie găsit pe Google la căutările care chiar îți aduc bani — și gândit ca să transforme acei vizitatori în rezervări. Apoi e al tău. Fără abonament, fără intermediar. | Я делаю вам сайт, настроенный так, чтобы вас находили в Google по запросам, которые реально приносят деньги, — и собранный так, чтобы превращать этих посетителей в заявки. А дальше сайт ваш. Без абонентской платы, без посредников. |
| `hero_btn_start` | START A PROJECT | ÎNCEPE UN PROIECT | НАЧАТЬ ПРОЕКТ |
| `hero_btn_view` | SEE WHAT'S INCLUDED | VEZI CE INCLUDE | ЧТО ВХОДИТ |
| `hero_stat_1_value` | Found | Găsit | Находят |
| `hero_stat_1_label` | on Google | pe Google | в Google |
| `hero_stat_2_value` | Built to convert | Construit să convertească | Создан, чтобы продавать |
| `hero_stat_2_label` | not just pretty | nu doar frumos | а не просто красивый |
| `hero_stat_3_value` | You own it | E al tău | Сайт ваш |
| `hero_stat_3_label` | no retainer | fără abonament | без абонплаты |
| `rt_card_1_meta` | LOCAL_DISCOVERY | DESCOPERIRE_LOCALĂ | LOCAL_DISCOVERY |
| `rt_card_1_h` | Found on Google | Găsit pe Google | Вас находят в Google |
| `rt_card_1_p` | I set the foundation so the people already searching for what you do can actually find you — Google Business Profile dialed in, on-page local SEO aimed at the searches that bring paying customers, and the schema Google needs to trust you. | Pun fundația ca oamenii care deja caută ce faci tu să te poată găsi cu adevărat — profil Google Business pus la punct, SEO local pe pagină țintit pe căutările care aduc clienți plătitori și schema de care Google are nevoie ca să aibă încredere în tine. | Я выстраиваю фундамент, чтобы люди, которые уже ищут то, чем вы занимаетесь, действительно вас находили: настроенный профиль Google Business, локальное SEO, нацеленное на запросы, приводящие платёжеспособных клиентов, и разметка schema, которой Google доверяет. |
| `rt_card_1_li` | html:\<li>Google Business Profile\</li>\<li>Local SEO · profitable-intent keywords\</li>\<li>LocalBusiness schema\</li> | html:\<li>Profil Google Business\</li>\<li>SEO local · cuvinte-cheie cu intenție profitabilă\</li>\<li>Schema LocalBusiness\</li> | html:\<li>Профиль Google Business\</li>\<li>Локальное SEO · прибыльные запросы\</li>\<li>Разметка LocalBusiness\</li> |
| `rt_card_2_meta` | SITE_THAT_SELLS | SITE_CARE_VINDE | SITE_THAT_SELLS |
| `rt_card_2_h` | Built to Convert | Construit să convertească | Создан, чтобы продавать |
| `rt_card_2_p` | A premium, fast, mobile-first site built around one job: turning a visitor who found you into a booking, a call, or a sale. Clear service pages for the work that actually pays, designed so the next step is obvious. | Un site premium, rapid, gândit întâi pentru mobil, construit pentru un singur rol: să transforme vizitatorul care te-a găsit într-o rezervare, un apel sau o vânzare. Pagini de servicii clare pentru lucrul care chiar aduce bani, gândite ca pasul următor să fie evident. | Премиальный, быстрый сайт с упором на мобильные — с одной задачей: превратить нашедшего вас посетителя в заявку, звонок или продажу. Понятные страницы под услуги, которые реально приносят деньги, спроектированные так, чтобы следующий шаг был очевиден. |
| `rt_card_2_li` | html:\<li>Premium custom design\</li>\<li>Service pages for your money services\</li>\<li>Mobile-first · fast · clear CTAs\</li> | html:\<li>Design custom premium\</li>\<li>Pagini de servicii pentru serviciile care aduc bani\</li>\<li>Întâi pentru mobil · rapid · CTA-uri clare\</li> | html:\<li>Премиальный индивидуальный дизайн\</li>\<li>Страницы под ваши прибыльные услуги\</li>\<li>Сначала мобильные · быстро · понятные призывы к действию\</li> |
| `rt_card_3_meta` | OWNERSHIP + FOLLOW-UP | PROPRIETATE + URMĂRIRE | OWNERSHIP + FOLLOW-UP |
| `rt_card_3_h` | Yours to Keep | Al tău, definitiv | Сайт остаётся вашим |
| `rt_card_3_p` | You own the asset outright — no rental, no retainer trap. And it keeps working after launch: an automated review-collection system that turns happy customers into the reviews that win you the next one, plus simple lead follow-up so nothing slips. | Deții activul în întregime — fără chirie, fără capcana abonamentului. Și continuă să lucreze după lansare: un sistem automat de colectare a recenziilor care transformă clienții mulțumiți în recenziile care îți aduc următorul client, plus o urmărire simplă a lead-urilor, ca nimic să nu-ți scape. | Актив полностью ваш — никакой аренды, никакой ловушки абонентской платы. И он продолжает работать после запуска: автоматическая система сбора отзывов превращает довольных клиентов в те отзывы, что приводят следующего, плюс простое дожатие заявок, чтобы ничего не терялось. |
| `rt_card_3_li` | html:\<li>Full ownership · handover guide\</li>\<li>Automated review collection\</li>\<li>Lead follow-up that doesn't drop\</li> | html:\<li>Proprietate completă · ghid de predare\</li>\<li>Colectare automată de recenzii\</li>\<li>Urmărire a lead-urilor care nu lasă nimic să cadă\</li> | html:\<li>Полное право собственности · инструкция по передаче\</li>\<li>Автоматический сбор отзывов\</li>\<li>Дожатие заявок без потерь\</li> |
| `pricing_kicker` | What you get · what it costs | Ce primești · cât costă | Что вы получаете · сколько это стоит |
| `pricing_h2` | Found. Converting. Yours. | Găsit. Convertește. Al tău. | Находят. Продаёт. Ваш. |
| `pricing_lead` | One fixed price for a website that's set up to be found and built to convert — then handed over to you. Pick the depth that fits. No retainers, no surprises. | Un preț fix pentru un site pus la punct ca să fie găsit și construit ca să convertească — apoi predat ție. Alegi nivelul care ți se potrivește. Fără abonamente, fără surprize. | Одна фиксированная цена за сайт, который настроен, чтобы вас находили, и собран, чтобы продавать, — а потом передан вам. Выберите подходящую глубину. Без абонентской платы, без сюрпризов. |
| `sw_c1_name` (→ `sw_c1_title`) | Found Core | Found Core | Found Core |
| `sw_c1_price` | from €690 | de la €690 | от €690 |
| `sw_c1_desc` | The complete get-found-and-convert foundation, owned by you. | Fundația completă „te găsesc și convertești", a ta cu totul. | Полный фундамент «находят и продаёт» — и он ваш. |
| `sw_c1_li` (→ `sw_c1_li1`–`li4`+) | html:\<li>Premium single-purpose site (up to 3 money pages)\</li>\<li>Google Business Profile optimized\</li>\<li>On-page local SEO for profitable-intent keywords\</li>\<li>LocalBusiness schema\</li>\<li>Automated review-collection setup\</li>\<li>Handover guide\</li> | html:\<li>Site premium cu un singur scop (până la 3 pagini care aduc bani)\</li>\<li>Profil Google Business optimizat\</li>\<li>SEO local pe pagină pentru cuvinte-cheie cu intenție profitabilă\</li>\<li>Schema LocalBusiness\</li>\<li>Configurare colectare automată de recenzii\</li>\<li>Ghid de predare\</li> | html:\<li>Премиальный сайт под одну задачу (до 3 продающих страниц)\</li>\<li>Оптимизированный профиль Google Business\</li>\<li>Локальное SEO под прибыльные запросы\</li>\<li>Разметка LocalBusiness\</li>\<li>Настройка автоматического сбора отзывов\</li>\<li>Инструкция по передаче\</li> |
| `sw_c2_name` (→ `sw_c2_title`) | Found Standard | Found Standard | Found Standard |
| `sw_c2_badge` *(NEW KEY)* | Most popular | Cel mai ales | Самый популярный |
| `sw_c2_price` | from €990 | de la €990 | от €990 |
| `sw_c2_desc` | For businesses with a few services to rank and sell. | Pentru afaceri cu câteva servicii de poziționat și vândut. | Для бизнеса с несколькими услугами, которые нужно вывести в топ и продавать. |
| `sw_c2_li` | html:\<li>Everything in Found Core\</li>\<li>5–8 page build with dedicated service pages\</li>\<li>Richer conversion design\</li>\<li>Lead follow-up automation\</li>\<li>GA4 + Search Console wired\</li>\<li>30-day post-launch support\</li> | html:\<li>Tot ce e în Found Core\</li>\<li>Construcție de 5–8 pagini, cu pagini dedicate de servicii\</li>\<li>Design de conversie mai bogat\</li>\<li>Automatizare urmărire lead-uri\</li>\<li>GA4 + Search Console conectate\</li>\<li>30 de zile de suport după lansare\</li> | html:\<li>Всё из Found Core\</li>\<li>Сайт на 5–8 страниц с отдельными страницами услуг\</li>\<li>Более глубокий продающий дизайн\</li>\<li>Автоматизация дожатия заявок\</li>\<li>Подключённые GA4 + Search Console\</li>\<li>30 дней поддержки после запуска\</li> |
| `sw_c3_name` (→ `sw_c3_title`) | Found Premium | Found Premium | Found Premium |
| `sw_c3_price` | from €1,400+ | de la €1.400+ | от €1 400+ |
| `sw_c3_desc` | The flagship asset for a reputation that deserves it. | Activul de top pentru o reputație care îl merită. | Флагманский актив для репутации, которая этого заслуживает. |
| `sw_c3_li` | html:\<li>Everything in Found Standard\</li>\<li>Fully bespoke design (no templates)\</li>\<li>Advanced motion & interactions\</li>\<li>Deeper Merlin follow-up + review workflows\</li>\<li>Priority build access\</li>\<li>60-day support window\</li> | html:\<li>Tot ce e în Found Standard\</li>\<li>Design complet personalizat (fără șabloane)\</li>\<li>Animații și interacțiuni avansate\</li>\<li>Fluxuri Merlin de urmărire și recenzii mai aprofundate\</li>\<li>Acces prioritar la construcție\</li>\<li>Fereastră de suport de 60 de zile\</li> | html:\<li>Всё из Found Standard\</li>\<li>Полностью индивидуальный дизайн (без шаблонов)\</li>\<li>Продвинутая анимация и интерактив\</li>\<li>Углублённое дожатие через Merlin + сценарии работы с отзывами\</li>\<li>Приоритетный доступ к разработке\</li>\<li>60 дней поддержки\</li> |
| `sw_c4_name` (→ `sw_c4_title`) | Visibility Care | Visibility Care | Visibility Care |
| `sw_c4_price` | from €90–150/mo | de la €90–150/lună | от €90–150/мес |
| `sw_c4_desc` | Optional, cancel anytime. A monthly block of work — review monitoring, Google Business Profile updates, listing checks, and a content refresh. Ongoing maintenance, not a traffic or ranking guarantee. | Opțional, anulezi oricând. Un bloc lunar de lucru — monitorizarea recenziilor, actualizări la profilul Google Business, verificarea listărilor și o reîmprospătare de conținut. Mentenanță continuă, nu o garanție de trafic sau de poziționare. | Опционально, можно отменить в любой момент. Ежемесячный объём работ — мониторинг отзывов, обновления профиля Google Business, проверка карточек в каталогах и обновление контента. Текущее обслуживание, а не гарантия трафика или позиций. |
| `boundary_h` *(NEW SECTION)* | I build the asset. You own the outcome. | Eu construiesc activul. Tu deții rezultatul. | Я создаю актив. Результат — ваш. |
| `boundary_p` *(NEW SECTION)* | I set you up to be found and built to convert — Google profile, local SEO, a site that sells, and a system that gathers your reviews. What I don't do is run your ads or promise you traffic. The demand is yours; my job is to make sure it finally lands somewhere worthy of it. | Te pun la punct ca să fii găsit și construit ca să convertești — profil Google, SEO local, un site care vinde și un sistem care îți adună recenziile. Ce nu fac: nu îți administrez reclamele și nu îți promit trafic. Cererea e a ta; treaba mea e să mă asigur că, în sfârșit, ajunge undeva care o merită. | Я настраиваю так, чтобы вас находили, и собираю так, чтобы продавать: профиль Google, локальное SEO, продающий сайт и система, собирающая ваши отзывы. Чего я не делаю — не веду вашу рекламу и не обещаю трафик. Спрос — ваш; моя задача — сделать так, чтобы он наконец приходил туда, что его достойно. |
| `common.footer.location_line_3` *(FIX — violates boundary)* | Premium builds. You own the asset. | Construcții premium. Activul e al tău. | Премиальные сайты. Актив — ваш. |

**Copy notes applied from critics:**
- **RO `meta_title` fixed** from the ambiguous first-person "Te găsesc, te aleg, e al tău" (read as *the atelier* being found) to second-person **"Ești găsit, ești ales, e al tău"** ("you are found, you are chosen, it's yours"), mirroring the RU framing.
- **RU `pricing_h2` shortened** from "Вас находят. Сайт продаёт. И он ваш." to **"Находят. Продаёт. Ваш."** to match the staccato cadence of EN "Found. Converting. Yours." in a large display H2.
- **`sw_c4` (Visibility Care)** renders as a small optional line below the three tiers — **net-new element**, not a demotion of the existing 4th card (which is the real "Custom Premium" build tier). See Apply-map.

---

## SEO

### Per-language target keywords

#### EN — buyer-intent, local, vanity/DIY excluded
**Group A — "hire a builder" (primary, money queries):** small business website that converts · website that ranks on Google for local business · local business web design [city] · website design for salons/dentists/restaurants · one-time website cost (no monthly fee) · fixed price website design
**Group B — "make me findable" (primary):** how to get my business found on Google · Google Business Profile setup for small business · local SEO for [salon/clinic/trades] · get more bookings from my website
**Group C — replace a bad site (secondary):** website redesign for small business · my website doesn't show up on Google · professional website for [local service business] · website that I own (not Wix / not subscription)
**Group D — vertical long-tail:** dentist/salon/restaurant website with online booking
**EXCLUDE:** how to build a website · best website builder · free website · what is local SEO · how to get more clients · digital marketing agency

#### RO — RO/MD market
**Group A (build):** `creare site web` · `creare site web Chișinău` · `creare site web București` · `site web pentru salon` · `site web pentru cabinet stomatologic` / `clinică` · `site web pentru restaurant` · `site de prezentare pentru firmă` · `creare site care apare pe Google` · `preț creare site web`
**Group B (found locally):** `optimizare Google Business Profile` · `cum să apar pe Google Maps` / `promovare pe Google Maps` · `SEO local Chișinău` / `SEO local București` · `site web optimizat pentru Google`
**Group C (convert/ownership):** `site web care aduce clienți` / `site care convertește` · `site web modern pentru afaceri mici` · `magazin online WooCommerce` / `creare magazin online` · `site web preț fix` / `pachet creare site`
**EXCLUDE:** `ce este SEO` · `cum funcționează un site` · `tutorial WordPress` · `cele mai bune teme WordPress` · `marketing online` · `cum să devii viral` · `clienți premium garantați`

#### RU — RU/MD market
**Group A (hire to build):** `создание сайта для бизнеса Кишинёв` · `заказать сайт под ключ` · `создание сайта для салона красоты` · `сайт для стоматологии под ключ` · `разработка сайта для ресторана` · `сделать сайт для малого бизнеса` · `создание сайта цена Кишинёв` · `веб разработчик Кишинёв`
**Group B (found on Google):** `сайт который виден в Google` · `сайт чтобы находили в Гугл` · `местное SEO для малого бизнеса` · `настройка Google Бизнес профиля`
**Group C (converts/sells):** `продающий сайт под ключ` · `сайт для записи клиентов` · `сайт визитка для услуг`
**EXCLUDE:** `как создать сайт самому` · `что такое SEO` · `бесплатный конструктор сайтов` · `сайт бесплатно`

### Meta titles & descriptions

> **SHIP GATE:** EN metas are shippable now. **RO/RU metas are blocked on Decision #2 (hreflang).** Until per-language URLs exist, RO/RU metas are roadmap assets only — do not place them in any `<head>`. No prices in any meta (keeps them evergreen and price-confirmation-safe).

#### EN

| Page | Title | Description |
|---|---|---|
| Homepage (`index.html`) | Get Found, Get Chosen, Own It \| Camelot Flows | A premium website set up to be found on Google and built to convert — for the searches that pay. One fixed price, then it's yours. No retainer. |
| Launch / Found Core (`service-creation.html` — see cannibalization flag) | Local Business Website That Converts \| Found Core | A premium one-page site that gets your business found on Google and turns visitors into bookings. Fixed price, fully yours — no monthly fees. |
| Ecommerce (`ecommerce-wp.html`) | Ecommerce Website Built to Sell \| Camelot | A fast WordPress store, set up to be found and built to convert browsers into buyers. One fixed price, owned by you — no subscription lock-in. |
| Custom Premium (`custom-premium.html`) | Bespoke Premium Website, Built to Convert | A fully custom site for a reputation that deserves it — found on Google, built to book clients, yours to keep. Direct from the builder, fixed price. |
| Merlin (`merlin-automation.html`) | Automated Reviews & Lead Follow-Up \| Merlin | Turn happy customers into the reviews that win the next one — automated review collection and lead follow-up that helps your site convert. Yours. |

For geo-targeted builds, inject the city (`Chișinău` / `București`) into the homepage and launch-site titles — highest-impact local move once per-language URLs ship.

#### RO `[BLOCKED on Decision #2]`

| Page | Title | Description |
|---|---|---|
| Homepage | Creare site web care apare pe Google \| Camelot Flows | Site premium pentru afacerea ta locală: găsit pe Google, construit să aducă programări — apoi e al tău. Preț fix, fără abonament, direct de la creator. |
| Launch (`launch-site.html` / `service-creation.html`) | Creare site de prezentare, preț fix \| Camelot Flows | Un site rapid și modern care îți arată afacerea exact când clienții te caută pe Google. Optimizat local, ușor de găsit, al tău din prima zi. Fără abonament. |
| Ecommerce (`ecommerce-wp.html`) | Creare magazin online WooCommerce \| Camelot Flows | Magazin online pe WordPress, construit să vândă și să apară pe Google. Pagini de produs clare, plăți sigure, mobil-first. Îl deții complet, fără retainer. |
| Custom Premium (`custom-premium.html`) | Site web premium, design la comandă \| Camelot Flows | Design bespoke pentru o reputație care merită. Găsit pe Google, construit să convertească, cu animații fine — și complet al tău. Preț fix, acces direct. |
| Merlin (`merlin-automation.html`) | Merlin: colectare recenzii automat \| Camelot Flows | Sistemul care transformă clienții mulțumiți în recenzii Google și nu pierde niciun lead. Follow-up automat care îți face site-ul să convertească după lansare. |

#### RU `[BLOCKED on Decision #2]`

| Page | Title | Description |
|---|---|---|
| Homepage | Сайт, который находят в Google и который продаёт | Премиум-сайт для локального бизнеса: видимость в Google, продающий дизайн, система отзывов. Под ключ — и сайт ваш. Без абонплаты и посредников. |
| Launch / Found Core (`launch-site.html` / `service-creation.html`) | Создание сайта под ключ — Found Core | Премиум-сайт для бизнеса: настройка Google Бизнес, локальное SEO, схема LocalBusiness и сбор отзывов. Фикс-цена, сайт переходит вам. |
| Ecommerce (`ecommerce-wp.html`) | Сайт интернет-магазина под ключ — WordPress | Магазин на WordPress: страницы товаров, которые видны в Google и продают. Локальное SEO, автоматизация отзывов, поддержка. Под ключ — и магазин ваш. |
| Custom Premium (`custom-premium.html`) | Премиум-сайт под заказ — Found Premium | Полностью индивидуальный дизайн без шаблонов: видимость в Google, продающая структура, авто-отзывы и follow-up. Флагманский сайт — и он ваш. |
| Merlin (`merlin-automation.html`) | Merlin — автоматизация отзывов и заявок | Система, которая превращает довольных клиентов в отзывы и не теряет заявки. Автоматизация для сайта — работа, а не обещание трафика. |

> **Page-inventory correction (critic):** `launch-site.html`, `ecommerce-wp.html`, `custom-premium.html`, `merlin-automation.html` **all exist** — the earlier RO note claiming they don't was wrong. Map metas to the real files. Resolve the `launch-site.html` vs `service-creation.html` cannibalization (Decision #3) before assigning the Found Core meta. Recount Cyrillic char limits in code, not by eye — but moot until RO/RU have URLs.

---

## Structured data (JSON-LD)

Critics' fixes applied: `geo` dropped (locality `address` only), `acceptedText:null` removed, all blocks reference one canonical org node by `@id`, prices flagged. **Ship Offers + FAQ together on confirmed prices only — never in separate passes** (prevents the recurring "two contradictory price sets on one page" bug).

### Block A — `ProfessionalService` (canonical org node) → `index.html` `<head>`

This is the canonical node every other block references via `@id`. Confirm `sameAs`, `logo`/`image` paths, `priceRange` before ship.

```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "https://camelotflows.dev/#organization",
  "name": "Camelot Flows",
  "alternateName": "Camelot Flows Atelier",
  "description": "Solo web atelier building local-business websites that are set up to be found on Google and built to convert — owned outright by the client. Premium, fixed-price, direct builder access. No agency, no middlemen.",
  "url": "https://camelotflows.dev/",
  "logo": "https://camelotflows.dev/assets/images/logo.png",
  "image": "https://camelotflows.dev/assets/images/og-cover.jpg",
  "founder": { "@type": "Person", "name": "Alex Buzi" },
  "priceRange": "€€",
  "knowsLanguage": ["en", "ro", "ru"],
  "slogan": "Get found. Get chosen. Own it.",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Chișinău",
    "addressCountry": "MD"
  },
  "areaServed": [
    { "@type": "Country", "name": "Moldova" },
    { "@type": "Country", "name": "Romania" },
    { "@type": "AdministrativeArea", "name": "European Union" },
    { "@type": "Country", "name": "United States" }
  ],
  "sameAs": [
    "https://www.linkedin.com/company/camelot-flows",
    "https://www.facebook.com/camelotflows"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "sales",
    "email": "alex@camelotflows.dev",
    "availableLanguage": ["en", "ro", "ru"]
  }
}
```

> **Applied fix:** `geo` GeoCoordinates **removed** (remote atelier, no walk-in office — locality-only address is true and sufficient). See Decision #6.

### Block B — `Service` + reconciled 3-tier `offers` → `index.html` `<head>` (replace existing Offers/Service block)

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://camelotflows.dev/#found-and-converting-build",
  "name": "Found & Converting — Local Business Website Build",
  "serviceType": "Website design + local discovery foundation",
  "description": "A one-time premium website build that is set up to be found on Google for the searches that make a local business money, and built to convert those visitors into bookings, calls, and sales. Includes Google Business Profile optimization, on-page local SEO targeting profitable-intent keywords, LocalBusiness schema, service pages for the money services, an automated review-collection system, and a full handover guide. The client owns the asset outright — no retainer, no middleman. Does not include ongoing ad management or traffic/lead guarantees.",
  "category": "Web design",
  "provider": { "@id": "https://camelotflows.dev/#organization" },
  "areaServed": [
    { "@type": "Country", "name": "Moldova" },
    { "@type": "Country", "name": "Romania" },
    { "@type": "AdministrativeArea", "name": "European Union" },
    { "@type": "Country", "name": "United States" }
  ],
  "audience": {
    "@type": "BusinessAudience",
    "name": "Local service SMBs with existing demand losing it to a weak or unfindable website"
  },
  "termsOfService": "One-time build, full client ownership on handover. Excludes ad management and traffic/lead guarantees.",
  "offers": [
    {
      "@type": "Offer",
      "name": "Found Core",
      "description": "Premium single-purpose site (up to 3 money pages), Google Business Profile optimization, on-page local SEO for profitable-intent keywords, LocalBusiness schema, automated review-collection setup, and a handover guide. The complete get-found-and-convert foundation, owned outright.",
      "price": "690",
      "priceCurrency": "EUR",
      "priceSpecification": {
        "@type": "PriceSpecification",
        "price": "690",
        "priceCurrency": "EUR",
        "valueAddedTaxIncluded": false,
        "minPrice": "690"
      },
      "category": "Website build (one-time)",
      "availability": "https://schema.org/InStock",
      "url": "https://camelotflows.dev/#pricing"
    },
    {
      "@type": "Offer",
      "name": "Found Standard",
      "description": "Everything in Found Core, plus a 5–8 page build with dedicated service pages for each money service, richer conversion design, lead follow-up automation, GA4 + Search Console wired, and 30-day post-launch support.",
      "price": "990",
      "priceCurrency": "EUR",
      "priceSpecification": {
        "@type": "PriceSpecification",
        "price": "990",
        "priceCurrency": "EUR",
        "valueAddedTaxIncluded": false,
        "minPrice": "990"
      },
      "category": "Website build (one-time)",
      "availability": "https://schema.org/InStock",
      "url": "https://camelotflows.dev/#pricing"
    },
    {
      "@type": "Offer",
      "name": "Found Premium",
      "description": "Everything in Found Standard, plus fully bespoke design (no templates), advanced motion and interactions, deeper Merlin follow-up and review workflows, priority build access, and a 60-day support window. The flagship owned asset.",
      "price": "1400",
      "priceCurrency": "EUR",
      "priceSpecification": {
        "@type": "PriceSpecification",
        "price": "1400",
        "priceCurrency": "EUR",
        "valueAddedTaxIncluded": false,
        "minPrice": "1400"
      },
      "category": "Website build (one-time)",
      "availability": "https://schema.org/InStock",
      "url": "https://camelotflows.dev/#pricing"
    },
    {
      "@type": "Offer",
      "name": "Visibility Care (optional)",
      "description": "Optional monthly maintenance block, cancel anytime. Review monitoring, Google Business Profile updates, listing checks, and a content refresh. This is work performed, not a traffic or ranking guarantee.",
      "priceCurrency": "EUR",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "priceCurrency": "EUR",
        "minPrice": "90",
        "maxPrice": "150",
        "unitText": "MONTH",
        "billingDuration": "P1M"
      },
      "category": "Maintenance (recurring, optional)",
      "availability": "https://schema.org/InStock",
      "url": "https://camelotflows.dev/#pricing"
    }
  ]
}
```

> **All four prices `[NEEDS CLIENT CONFIRMATION]`** (690 / 990 / 1400 / 90–150). `valueAddedTaxIncluded: false` is correct for a non-VAT MD freelancer — confirm. `provider` now references `#organization` by `@id` instead of repeating the inline object.

### Block C — `FAQPage` → `index.html` `<head>` (replace the existing stale FAQ block, don't append)

Reconciled to the 3-tier story. The boundary is baked into the answers. **The price-bearing answer is generalized to "from around €690" — keep the *old confirmed numbers* live until prices lock, then update this in lockstep with Block B.**

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Will you get me more customers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Honestly: I build the asset, you own the outcome. My job is to make sure the people already searching for what you do can find you — Google Business Profile dialed in, local SEO aimed at profitable-intent searches, LocalBusiness schema — and that the site turns those visitors into bookings. What I don't do is run your ads or promise a number of leads. If you already have demand from referrals, foot traffic, or reputation, I make sure it finally lands on a site worthy of it. If you have no demand and need someone to make you famous, I'm not the right fit."
      }
    },
    {
      "@type": "Question",
      "name": "Do I own the website, or am I renting it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You own it outright. It's a one-time build handed over to you with a guide — no rental, no retainer trap, no being held hostage by your developer. The site, the content, and the accounts are yours to keep and control."
      }
    },
    {
      "@type": "Question",
      "name": "Will my business show up on Google?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "I set the foundation so you can be found: your Google Business Profile is optimized, the site has on-page local SEO targeting the searches that actually bring paying customers, and the LocalBusiness schema Google needs to trust and place you is built in. I can't guarantee a specific ranking position — nobody honest can — but I make sure everything within a builder's control is done right so you're set up to be found."
      }
    },
    {
      "@type": "Question",
      "name": "What does it cost, and are there hidden fees or monthly charges?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "One fixed price, agreed upfront, with three tiers from around €690. No surprises and no required monthly fee — you own the asset when it's done. There's an optional Visibility Care plan if you want me to keep handling reviews, listing updates, and content afterward, but it's opt-in and sold as work performed, never as a traffic or ranking promise."
      }
    },
    {
      "@type": "Question",
      "name": "Do you work with businesses outside Moldova?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. I'm a solo atelier based in Chișinău working with local service businesses across Moldova and Romania first, and the EU and US next. Everything is delivered remotely with direct builder access — no agency layers, no account managers, no middlemen between you and the person actually building your site."
      }
    },
    {
      "@type": "Question",
      "name": "What kind of businesses is this built for?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Local service businesses that already have demand — salons, clinics, dentists, restaurants, trades, fitness studios, and similar — who are losing customers to a weak, outdated, or unfindable website. If you have a reputation and repeat customers but your site doesn't reflect it, that's exactly what this is for. If you have no demand yet and need marketing to create it from scratch, this isn't the right offer."
      }
    }
  ]
}
```

> **Applied fix:** `acceptedText: null` **removed** (invalid no-op, validators flag it).

### Dedup / ship checklist
- Page must end with **exactly one** `FAQPage`, **one** canonical org node, **one** `Service`/`Offers` definition. Recent commits (`d8fa98f`, `28c6e55`, `c22def3`) already touched FAQ + Offers — **replace, don't append**.
- **Do NOT add `aggregateRating` / `Review` nodes** — there are no real reviews; a fake one is a manual-action risk and contradicts the honesty thesis. The "automated review collection" feature must not tempt anyone into this.
- Old live FAQ JSON-LD still enumerates €390/€650/€900/€1,200 and "Merlin … from €690." **Ship Offers + FAQ together**, on confirmed numbers only.
- Validate combined output with Google Rich Results Test + schema.org validator before `git push`.

---

## Blog post

One post, three languages, same shared slug `found-and-converting` (RO uses `gasit-si-convertit` per the original draft — **decide one slug convention** if all three live at distinct URLs). All four critic flags applied to the EN body and carried into RO/RU.

### EN

**Title:** I Build the Asset, Not the Outcome: How "Found & Converting" Became My Whole Philosophy
*(Promoted from alt title — critic noted it is the more confident option. Original primary "The Beautiful Site Nobody Could Find" retained as H1 of the body.)*
**Slug:** `/blog/found-and-converting`
**Meta description (148):** A maker's hard-won lesson: clients don't buy websites, they buy customers. Why I now build sites that get found on Google and convert — and you own it.
**Keywords:** website that gets found on google · local SEO website build · website that converts customers · Google Business Profile optimization · premium small business website

**Body:**

# The Beautiful Site Nobody Could Find

I have handed over websites that made clients genuinely happy. Fast, premium, beautiful — the kind of build where you both sit back at launch and feel the craft in it. That moment is real, and I am not going to pretend it isn't the best part of the job.

But here is what I learned watching those beautiful sites live in the world: a finished website, by itself, is a cabin built deep in a forest. Perfect woodwork. Stone fireplace. And not a single person walking past, because there's no path to the door.

So clients would come back. Not to ask for more design. They'd ask the real question underneath every web project: **"How do people actually find this?"**

## The role I didn't want

For a while, I answered that question by becoming a marketer.

If you're a freelancer who builds things, you know how this happens. The client is happy with the site, they trust you, and the next ask is traffic. You don't want to lose the relationship, so you say yes. Suddenly you're running ads, chasing rankings, and quietly becoming accountable for something with a dozen moving parts you don't control.

That role is structurally rigged against a solo builder. And I have the scar to prove it.

## The lawyer

A lawyer hired me, and I did genuinely good work. I'd spotted a real trend, so I wrote expert blog posts — the most useful "how to open a company in Moldova" content out there — and put Google Ads behind them. And the phone rang.

And here's where the model breaks: the wins were invisible. Call tracking barely works in this market, so the leads that *did* come from those posts couldn't be proven. My fee and his ad spend fused into one number with nothing measurable on the other side. So I raised my rate — and he left for someone cheaper. Fair enough. He was paying for an outcome neither of us could see, and I'd put myself on the hook for it.

I could be annoyed about that. I'm not. It taught me the single most useful thing I know about this work.

## Clients don't buy websites. They buy customers.

That's the truth nobody puts on a pricing page. Nobody wants a website. They want the thing a website is supposed to bring: more of the right customers walking through the door.

So for a while the logical conclusion seemed to be: *fine, I'll sell customers, then.* Sell the outcome.

But sit with that and it falls apart. **You cannot be accountable for an outcome you don't control.** I don't control the client's offer. I don't control their prices, their sales skills, whether they call the lead back in five minutes or five days, whether they close. I don't even control whether the market is measurable — see: call tracking in Moldova.

Selling outcomes means eating the blame for other people's businesses. You become the lightning rod for every variable that has nothing to do with the work you actually did. That's not a service. That's a hostage situation with an invoice attached.

## So I got sharper

So I sharpened. The lesson wasn't *marketing is too hard.* It was *I'd been selling the wrong half of the value.*

The web work I do — premium, fast, built right — is the most defensible, most controllable, most genuinely valuable thing on the table. The mistake was bolting an uncontrollable outcome onto a controllable asset and calling it one offer.

So I split them. I keep the part I'm world-class at and can stand behind completely. I hand the client the part only they can own.

I call it **Found & Converting.**

## What I actually build now

I build you a site that is set up to be *found* on Google and *convert* — for the searches that actually make you money — and then **you own it.** One build. One price. No meter running.

Concretely, that means the premium site, plus the discovery foundation that turns it from a cabin in the woods into a storefront on the main road:

- A **Google Business Profile** optimized properly, so you show up when someone nearby is searching with their wallet out.
- **On-page local SEO** aimed at profitable-intent keywords — not vanity traffic, the searches that end in a booking.
- **LocalBusiness schema** and real service pages for the services that actually pay your bills.
- A **review-collection system** that runs quietly in the background, because reviews are the modern word-of-mouth and they compound.
- A **handover guide**, because it's yours. I'm not holding your keys hostage.

And here's the boundary: **I build the asset. You run your sales.** No ad-budget babysitting, no traffic guarantees, no pretending I can manufacture premium clients out of thin air — because I'd rather own the part I'm world-class at than rent the blame for the part I'm not. What you do with the customer once they arrive is your craft, not mine.

## The philosophy

The best clients for this already have demand. They have referrals, foot traffic, a reputation, people who'd happily send business their way — and they're *losing* it to a weak or invisible website. They don't need to be made famous. They need the people already looking for them to actually find them, and to be impressed when they do.

That's the line I've drawn, and it's made the work better on both sides: **I build you an asset that gets found and converts. You own it. And nobody's accountable for a business except the person who runs it.**

That's not me doing less. That's me doing exactly the right thing — and standing fully behind it.

### RO

**Title:** Construiesc activul, nu rezultatul: cum „Găsit și convertit" a devenit întreaga mea filozofie
**Slug:** `/blog/gasit-si-convertit`
**Meta description (149):** Lecția grea a unui meșter: clienții nu cumpără site-uri, cumpără clienți. De ce construiesc acum site-uri care se găsesc pe Google și convertesc — și sunt ale tale.
**Keywords:** site care se găsește pe Google · construcție site cu SEO local · site care convertește clienți · optimizare Profil de Afaceri Google · site premium pentru afaceri mici

**Body:**

# Site-ul superb pe care nu-l găsea nimeni

Am predat site-uri care i-au făcut pe clienți cu adevărat fericiți. Rapide, premium, frumoase — genul de proiect în care, la lansare, vă lăsați amândoi pe spate și simțiți măiestria din el. Momentul acela e real și n-o să mă prefac că nu e cea mai bună parte a meseriei.

Dar iată ce am învățat privind cum trăiesc în lume site-urile acelea frumoase: un site terminat, în sine, e o cabană construită adânc în pădure. Lemnărie impecabilă. Șemineu de piatră. Și niciun om care să treacă pe lângă ea, fiindcă nu duce nicio potecă până la ușă.

Așa că clienții se întorceau. Nu ca să ceară mai mult design. Puneau întrebarea adevărată care stă sub orice proiect web: **„Cum mă găsesc oamenii, concret?"**

## Rolul pe care nu mi-l doream

O vreme, am răspuns la întrebarea aceea devenind marketer.

Dacă ești un freelancer care construiește lucruri, știi cum se întâmplă. Clientul e mulțumit de site, are încredere în tine, iar următoarea cerere e trafic. Nu vrei să pierzi relația, așa că spui da. Și dintr-odată te trezești că rulezi reclame, alergi după poziții în căutări și devii, pe tăcute, răspunzător pentru un lucru cu o duzină de piese în mișcare pe care nu le controlezi.

Rolul ăsta e structural măsluit împotriva unui constructor solo. Și am cicatricea care o dovedește.

## Avocatul

M-a angajat un avocat și am făcut o muncă bună, sinceră. Sesizasem un trend real, așa că am scris articole de blog de expert — cel mai util conținut de tip „cum deschizi o firmă în Moldova" care exista — și am pus reclame Google în spatele lor. Și telefonul a început să sune.

Și aici se rupe modelul: reușitele erau invizibile. Urmărirea apelurilor abia funcționează pe piața asta, așa că lead-urile care *chiar* veneau din acele articole nu puteau fi dovedite. Onorariul meu și bugetul lui de reclame s-au contopit într-un singur număr, fără nimic măsurabil de cealaltă parte. Așa că mi-am ridicat tariful — iar el a plecat la cineva mai ieftin. Corect. Plătea pentru un rezultat pe care niciunul dintre noi nu-l putea vedea, iar eu mă pusesem singur chezaș pentru el.

Aș putea fi supărat din cauza asta. Nu sunt. M-a învățat cel mai util lucru pe care îl știu despre meseria asta.

## Clienții nu cumpără site-uri. Cumpără clienți.

Acesta e adevărul pe care nimeni nu-l pune pe o pagină de prețuri. Nimeni nu vrea un site. Vor lucrul pe care un site se presupune că-l aduce: mai mulți clienți potriviți care intră pe ușă.

Așa că, o vreme, concluzia logică părea să fie: *bine, atunci vând clienți.* Vând rezultatul.

Dar dacă stai puțin cu gândul ăsta, se destramă. **Nu poți fi răspunzător pentru un rezultat pe care nu-l controlezi.** Nu controlez oferta clientului. Nu-i controlez prețurile, talentul de a vinde, dacă sună înapoi lead-ul în cinci minute sau în cinci zile, dacă închide vânzarea. Nu controlez nici măcar dacă piața e măsurabilă — vezi: urmărirea apelurilor în Moldova.

Să vinzi rezultate înseamnă să înghiți vina pentru afacerile altora. Devii paratrăsnetul pentru fiecare variabilă care n-are nicio legătură cu munca pe care chiar ai făcut-o. Asta nu e un serviciu. E o luare de ostatici cu o factură atașată.

## Așa că am devenit mai ascuțit

Așa că m-am ascuțit. Lecția nu era *marketingul e prea greu.* Era *vânduse jumătatea greșită a valorii.*

Munca web pe care o fac — premium, rapidă, făcută cum trebuie — e lucrul cel mai defensabil, cel mai controlabil, cel mai cu adevărat valoros de pe masă. Greșeala a fost să lipesc un rezultat necontrolabil de un activ controlabil și să numesc asta o singură ofertă.

Așa că le-am separat. Păstrez partea la care sunt de clasă mondială și în spatele căreia pot sta complet. Îi predau clientului partea pe care doar el o poate deține.

Îi spun **Găsit și convertit.**

## Ce construiesc de fapt acum

Îți construiesc un site pregătit să fie *găsit* pe Google și să *convertească* — pentru căutările care îți aduc bani cu adevărat — și apoi **e al tău.** O singură construcție. Un singur preț. Niciun contor care merge.

Concret, asta înseamnă site-ul premium, plus fundația de vizibilitate care îl transformă dintr-o cabană în pădure într-un magazin pe artera principală:

- Un **Profil de Afaceri Google** optimizat ca lumea, ca să apari când cineva din apropiere caută cu portofelul în mână.
- **SEO local on-page** țintit pe cuvinte-cheie cu intenție profitabilă — nu trafic de fală, ci căutările care se termină cu o programare.
- **Schema LocalBusiness** și pagini de servicii reale pentru serviciile care chiar îți plătesc facturile.
- Un **sistem de colectare a recenziilor** care rulează discret în fundal, fiindcă recenziile sunt vorba-în-vânt modernă și se acumulează în timp.
- Un **ghid de predare**, fiindcă e al tău. Nu-ți țin cheile ostatice.

Și iată limita: **eu construiesc activul. Tu îți conduci vânzările.** Niciun dădăcit de buget de reclame, nicio garanție de trafic, nicio prefăcătorie că pot fabrica clienți premium din nimic — fiindcă prefer să dețin partea la care sunt de clasă mondială decât să închiriez vina pentru partea la care nu sunt. Ce faci cu clientul odată ce ajunge la tine e meșteșugul tău, nu al meu.

## Filozofia

Cei mai buni clienți pentru asta au deja cerere. Au recomandări, au oameni care le intră pe ușă, au o reputație, au persoane care le-ar trimite bucuroase de lucru — și o *pierd* din cauza unui site slab sau invizibil. N-au nevoie să fie făcuți celebri. Au nevoie ca oamenii care deja îi caută chiar să-i găsească — și să rămână impresionați când o fac.

Asta e linia pe care am trasat-o și a făcut munca mai bună de ambele părți: **îți construiesc un activ care se găsește și convertește. E al tău. Și nimeni nu e răspunzător pentru o afacere în afară de omul care o conduce.**

Asta nu înseamnă că fac mai puțin. Înseamnă că fac, în sfârșit, exact lucrul potrivit — și că stau complet în spatele lui.

### RU

**Title:** Я строю актив, а не результат: как «Найден и продаёт» стало всей моей философией
**Slug:** `/blog/found-and-converting`
**Meta description (149):** Выстраданный урок мастера: клиенты покупают не сайты, а клиентов. Почему я делаю сайты, которые находят в Google и которые продают — и они ваши.
**Keywords:** сайт, который находят в Google · сайт с локальным SEO под ключ · сайт, который превращает посетителей в клиентов · оптимизация Google Business Profile · премиальный сайт для малого бизнеса

**Body:**

# Красивый сайт, который никто не мог найти

Я сдавал сайты, от которых клиенты были искренне счастливы. Быстрые, премиальные, красивые — те самые проекты, где на запуске вы оба откидываетесь на спинку кресла и буквально чувствуете в них мастерство. Этот момент настоящий, и я не собираюсь делать вид, что это не лучшая часть работы.

Но вот что я понял, наблюдая, как эти красивые сайты живут своей жизнью: готовый сайт сам по себе — это домик, построенный в глубине леса. Идеальная столярка. Каменный камин. И ни одного человека, проходящего мимо, потому что к двери не ведёт ни одной тропинки.

И клиенты возвращались. Не для того, чтобы просить ещё дизайна. Они задавали тот самый настоящий вопрос, который скрывается под любым веб-проектом: **«А как люди вообще это найдут?»**

## Роль, которой я не хотел

Какое-то время я отвечал на этот вопрос тем, что становился маркетологом.

Если вы фрилансер, который что-то создаёт, вы знаете, как это происходит. Клиент доволен сайтом, он вам доверяет, и следующая просьба — трафик. Вы не хотите терять отношения, поэтому говорите «да». И вот вы уже крутите рекламу, гоняетесь за позициями в выдаче и тихо становитесь ответственным за штуку с десятком движущихся частей, которые вам неподконтрольны.

Эта роль структурно настроена против соло-исполнителя. И у меня есть шрам в доказательство.

## Юрист

Меня нанял юрист, и я сделал по-настоящему хорошую работу. Я уловил реальный тренд, поэтому написал экспертные статьи в блог — самый полезный контент в духе «как открыть компанию в Молдове», какой только был на рынке — и пустил на них Google Ads. И телефон зазвонил.

И вот где модель ломается: победы были невидимы. Отслеживание звонков на этом рынке почти не работает, так что те заявки, что *всё-таки* приходили с этих статей, нельзя было доказать. Мой гонорар и его рекламный бюджет слились в одно число, а на другой стороне — ничего измеримого. Поэтому я поднял ставку — и он ушёл к тому, кто дешевле. Справедливо. Он платил за результат, которого ни один из нас не мог увидеть, а я сам подписался за него отвечать.

Я мог бы на это злиться. Но я не злюсь. Это научило меня самой полезной вещи, которую я знаю об этой работе.

## Клиенты покупают не сайты. Они покупают клиентов.

Вот правда, которую никто не пишет на странице с ценами. Никому не нужен сайт. Им нужно то, что сайт должен приносить: больше тех самых, правильных клиентов, заходящих в дверь.

И какое-то время логичным выводом казалось: *ладно, тогда я буду продавать клиентов.* Продавать результат.

Но если посидеть с этой мыслью, она разваливается. **Нельзя отвечать за результат, который ты не контролируешь.** Я не контролирую предложение клиента. Я не контролирую его цены, его навыки продаж, перезвонит ли он по заявке через пять минут или через пять дней, закроет ли сделку. Я даже не контролирую, измерим ли рынок вообще — см. отслеживание звонков в Молдове.

Продавать результат — значит брать на себя вину за чужой бизнес. Ты становишься громоотводом для каждой переменной, которая не имеет никакого отношения к работе, которую ты на самом деле сделал. Это не услуга. Это захват заложника со счётом-фактурой в придачу.

## Поэтому я стал острее

Поэтому я заточился. Урок был не *маркетинг слишком сложен.* Он был *я продавал не ту половину ценности.*

Веб-работа, которую я делаю — премиальная, быстрая, сделанная как надо — это самая защищённая, самая контролируемая, самая по-настоящему ценная вещь на столе. Ошибка была в том, чтобы прикрутить неконтролируемый результат к контролируемому активу и назвать это одним предложением.

Поэтому я их разделил. Я оставляю себе ту часть, в которой я мирового уровня и за которую могу полностью отвечать. А клиенту отдаю ту часть, которой можете владеть только вы.

Я называю это **«Найден и продаёт».**

## Что я на самом деле делаю теперь

Я делаю вам сайт, который настроен на то, чтобы его *находили* в Google и который *продаёт* — по тем запросам, которые реально приносят вам деньги — и дальше **он ваш.** Одна сборка. Одна цена. Никакого счётчика.

Конкретно это означает премиальный сайт плюс фундамент видимости, который превращает его из домика в лесу в витрину на главной улице:

- **Google Business Profile**, оптимизированный как положено, чтобы вы появлялись, когда кто-то рядом ищет с кошельком наготове.
- **Локальное SEO на страницах** под запросы с прибыльным намерением — не ради тщеславного трафика, а ради тех поисков, что заканчиваются заявкой.
- **Schema-разметка LocalBusiness** и настоящие страницы услуг под те услуги, что реально оплачивают ваши счета.
- **Система сбора отзывов**, которая тихо работает в фоне, потому что отзывы — это современное сарафанное радио, и они накапливаются.
- **Руководство по передаче**, потому что сайт ваш. Я не держу ваши ключи в заложниках.

И вот граница: **я строю актив. Вы ведёте свои продажи.** Никакого нянченья рекламного бюджета, никаких гарантий трафика, никакого притворства, будто я могу слепить премиальных клиентов из воздуха — потому что я лучше буду владеть той частью, в которой я мирового уровня, чем арендовать вину за ту, в которой нет. Что вы делаете с клиентом, когда он пришёл, — это ваше мастерство, а не моё.

## Философия

Лучшие клиенты для этого уже имеют спрос. У них есть рекомендации, проходящий поток, репутация, люди, которые с радостью отправили бы к ним дела — и они *теряют* всё это из-за слабого или невидимого сайта. Их не нужно делать знаменитыми. Им нужно, чтобы те, кто уже их ищет, действительно их находили — и были впечатлены, когда найдут.

Вот черта, которую я провёл, и она сделала работу лучше с обеих сторон: **я строю вам актив, который находят и который продаёт. Вы им владеете. И никто не отвечает за бизнес, кроме того, кто им управляет.**

Это не я делаю меньше. Это я наконец делаю ровно то, что нужно — и полностью за это отвечаю.

---

## Apply-map

Exact files and locations. **i18n source of truth is the JS files, NOT the JSON.** Application is mechanical if you follow the key remap and the sync warning.

### ⚠️ Critical sync warning — `locales.js` ↔ `locales.min.js`

These two files are **NOT auto-generated mirrors at runtime** — they are two hand-maintained copies, and the homepage loads the *minified* one while all other pages load the source one:

- `index.html` loads **`assets/js/locales.min.js?v=1`**
- All other 17 HTML pages load **`assets/js/locales.js`**

**If you edit only `locales.js`, the homepage will not change.** Every key edit must be applied to **both** files in lockstep (or regenerate `.min.js` from `.js`). After editing, **bump the `?v=` cache-buster** on the `index.html` include (e.g. `?v=2`) so the new minified file is fetched. Verify the homepage in a hard-refresh after deploy — this is the #1 trap.

### Files to edit

| File | Action |
|---|---|
| **`assets/js/locales.js`** | PRIMARY source of truth. Apply all EN/RO/RU key changes from the Homepage copy table under `pages.index` (and `common.footer`). |
| **`assets/js/locales.min.js`** | Apply the **identical** changes (or regenerate from `.js`). Loaded by the homepage — without this, homepage copy does not move. |
| `index.html` | Bump `locales.min.js?v=` cache-buster. Swap `<head>` JSON-LD: replace Offers/Service → Block B, replace FAQ → Block C, add/replace org node → Block A. Apply hreflang decision (#2). Fix footer key render. |
| ~~`assets/locales/en.json` / `ro.json` / `ru.json`~~ | **STALE — do not edit, not used by live site.** (They still say "Award-Winning"; ignore.) |
| `wp-theme/camelot-flows/assets/js/locales.js` | Only if WP theme homepage is in scope. Note: WP theme locales are a smaller subset and **RU is missing entirely** from the WP theme — RU copy there is a separate gap. |

### Key remap (deliverable label → real codebase key)

The pricing values in the copy table use convenience labels. The live schema differs — remap before pasting:

| Deliverable label | Real key(s) in `locales.js` |
|---|---|
| `sw_c1_name` | `sw_c1_title` |
| `sw_c1_desc` | `sw_c1_desc` (exists) |
| `sw_c1_li` (one blob) | split into `sw_c1_li1`, `sw_c1_li2`, `sw_c1_li3`, `sw_c1_li4` (+ `sw_c1_delivery`) — **the live markup uses 4 separate list keys, not one HTML blob.** Trim/merge the 6 bullets to fit the 4-key structure, or restructure the card markup. |
| `sw_c2_name` | `sw_c2_title` |
| `sw_c2_badge` | **NEW KEY** — does not exist; add it + matching markup for the featured badge. |
| `sw_c3_name` | `sw_c3_title` |
| `sw_c4_name` | `sw_c4_title` (currently the real "Custom Premium" card — repurpose to Visibility Care + visually demote, see #3) |
| `boundary_h` / `boundary_p` | **NEW KEYS + NEW SECTION** — confirm the honest-boundary block exists in the homepage template; if not, add markup near pricing. |
| `hero_word_1` / `hero_word_2` | exist (`locales.js` ~L69/775/1479) — feed `wrapLetters()`; confirm RO `&`/Cyrillic handling. |

### `<head>` block routing (per page)

| Page | Gets which meta | Gets which schema |
|---|---|---|
| `index.html` | EN homepage title/desc now; RO/RU blocked on #2 | Block A (org) + Block B (Service/Offers) + Block C (FAQ) — replace existing, one of each |
| `service-creation.html` | EN "Found Core" meta (pending #3 cannibalization decision) | Optional: Block B Service node referencing `#organization` |
| `ecommerce-wp.html` | EN "Ecommerce" meta | — |
| `custom-premium.html` | EN "Custom Premium" meta | — |
| `merlin-automation.html` | EN "Merlin" meta | — |

### Pre-existing `<head>` bug to fix on `service-creation.html` (critic Blocker 2)

- `service-creation.html:40` canonical → `/service-creation` (no `.html`) **conflicts with** `:41` hreflang-en → `/service-creation.html` (with `.html`). Make canonical + all hreflang use the **same** URL form (house style is extensionless — homepage uses bare `/`).
- `service-creation.html:44`: the `x-default` `<link>` and `og:type` `<meta>` are **concatenated on one line with no newline** — split onto two lines.

### Ship sequence (mechanical, safe)

1. Lock prices (Decision #1) → fill the four `price` values in Block B + the "from around €690" line in Block C.
2. Edit `locales.js` **and** `locales.min.js` together (remapped keys); fix footer key.
3. Apply hreflang decision (#2) to `index.html` (+ service pages if RO/RU URLs are built).
4. Swap the three JSON-LD blocks in `index.html` `<head>` (replace, not append).
5. Fix `service-creation.html` canonical/hreflang/run-on tag.
6. Bump `locales.min.js?v=`. Validate JSON-LD (Rich Results + schema.org). Hard-refresh homepage to confirm copy moved.
7. `git push origin master` → Cloudflare Pages auto-deploys. (WP theme is a separate manual `scp` deploy if in scope.)

---

## Open flags from review

Human calls the critics raised that this document did **not** silently resolve:

1. **hreflang reality (Blocker 1)** — ~60% of the deliverable (all RO/RU meta) rests on per-language URLs that don't exist. Decision #2 must be answered before any RO/RU meta ships. Strip ro/ru hreflang now, or scope a real `/ro/ /ru/` pre-render project. **Until answered, RO/RU stay as body-copy/roadmap, not `<head>` meta.**

2. **Prices not locked** — all of 690 / 990 / 1,400+ / 90–150 are `[NEEDS CLIENT CONFIRMATION]`. Keep old confirmed numbers live in JSON-LD until locked. Ship Offers + FAQ + the three "from €390" meta strings + FAQ price ladder **in one atomic pass** — never split (prior bug `d8fa98f`).

3. **Fate of 4 standalone landing pages + cannibalization** (Decision #3) — keep/merge/301/noindex per page, and resolve `launch-site.html` vs `service-creation.html` competing on the core keyword. Not decidable from copy alone.

4. **Footer "Measurable results." + testimonial "Lead volume is noticeably up"** (Decision #4) — footer fix is proposed and required; the testimonial is a conscious keep/cut call (evidence vs. claim).

5. **€390 retirement** — confirm it survives only as a private "single landing page" call option, not anywhere public.

6. **Schema verification before ship** (Decision #6) — real `sameAs` LinkedIn/Facebook URLs, `logo`/`og-cover` paths exist, `priceRange: "€€"` accuracy, `valueAddedTaxIncluded: false` correctness. `geo` already dropped per recommendation — confirm you also don't want street-level `address` (locality-only kept).

7. **RO/RU hero word-split + `wrapLetters()`** (Decision #5) — confirm the splitter handles `Găsit &` and Cyrillic; fallbacks specified.

8. **Blog slug convention** — EN/RU use `/blog/found-and-converting`; RO uses `/blog/gasit-si-convertit`. If all three live at distinct URLs, confirm this is intentional (localized RO slug) vs. a single shared slug.

9. **WP theme RU gap** — the WordPress theme's locale subset has **no RU at all** (only EN + RO). If the relaunch must reach the WP-served pages in Russian, that's a separate translation task not covered by editing the main-site locales.

10. **Cyrillic meta char-counts** — the RU deliverable's own count tables disagree with each other (e.g. homepage listed as both "48/139" and "54/148"). Recount in code before shipping any RU meta — moot until Flag 1 gives RU a URL.