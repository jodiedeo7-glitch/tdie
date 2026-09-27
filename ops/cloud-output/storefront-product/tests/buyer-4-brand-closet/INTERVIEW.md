# Setup interview, buyer 4 (Jess, Brand Closet member)

Simulated run of `02_SETUP_PROMPT.txt` in the Claude desktop app, Monday 28 September 2026, about 10:15 am Eastern. The kit folder is attached. Jess's answers are natural and sometimes vague on purpose. Lines marked **[TEST NOTE]** are the tester's, not Claude's; they are not part of the chat.

---

**Claude:** Hi Jess. I've read the recipes, the task prompts and the persona and storefront paths, and there's no MY_RECIPE.txt in your folder yet, so we're starting fresh. Six questions, one at a time.

First: what's your look? Describe it the way you'd describe your Pinterest to a friend. For example: "cozy neutral mom style" or "coastal grandmother home decor".

**Jess:** pink girly outfits, a bit extra. like barbie vibes but I'm 38 and do school pickup lol

**Claude:** Love it. I'll write it as "pink girly outfits, a bit extra", with the summary "pink on pink, soft and feminine with one fun statement piece per look, easy enough for a busy mom's real day." I'm leaving the doll brand out on purpose: brand and character names can't go on pins or list titles, so your calendar describes the vibe instead.

Clothing, home, or both?

**Jess:** clothes. well accessories too I guess? bags and stuff

**Claude:** Got it: clothing, and I'm counting bags, shoes, jewelry and hair pieces as part of clothing.

> **[TEST NOTE]** The setup prompt never tells Claude to keep brand, character or film names out of the theme summary or the THEME CALENDAR. Claude did it here from R5/R6 in the recipe, but a less careful run could write "Barbiecore" into 100 look names. See FINDINGS F-07.
> **[TEST NOTE]** "Clothing only" collides with 03 line 38 ("Two clothing looks never sit back to back"). Claude tagged every calendar idea as [outfit], [theme list] or [roundup] so the weekly task can alternate kinds. See F-06.

**Claude:** Second: which Pinterest boards should the pins go on? Give me their exact names. If you don't have them yet, tell me and I'll suggest names people actually search for.

**Jess:** I have Pink Outfit Ideas and Pink Outfit of the Day. I think thats what theyre called

**Claude:** Could you open Pinterest and read me the names exactly as they appear, capitals included? The tasks match them letter for letter.

**Jess:** yep exactly "Pink Outfit Ideas" and "Pink Outfit of the Day"

**Claude:** Perfect. I'll put themed looks on Pink Outfit Ideas and Outfit of the Day pins on Pink Outfit of the Day. Please open each board and check it says Public, not Secret. Secret boards reach nobody.

**Jess:** ok the ideas one is public. the OOTD one I made last week... hang on. it was secret! fixed it, it's public now

**Claude:** Thank you, that's exactly the one that would have caught you out. Both confirmed public today.

> **[TEST NOTE]** "confirmed public" is recorded on her word only. The FINISH check ("boards all confirmed public") only re-reads the file Claude itself wrote, so it can never fail. The weekly and nightly tasks re-check with R11, so the risk is limited to setup day. See F-24.

**Claude:** Third: are you an approved Amazon Influencer with a storefront? If yes, paste your storefront address (it looks like amazon.com/shop/yourname). If you're Associates only, say "Associates only".

**Jess:** yes amazon.com/shop/jesspinkcloset

**Claude:** Great, you're on the Influencer path: every look gets its own Idea List in your storefront, and both pins link to it.

**Claude:** Fourth: do you have an AI persona, a consistent AI model who wears the looks? If yes, put her reference image in this folder and tell me the file name. (With a persona, pin 2 is her wearing the look. Without one, both pins are flat lays or collages.)

**Jess:** yes! jess-persona.png, it's in there

**Claude:** Found it. Name three or four real-feeling places she lives her life. For example: her kitchen island, her front porch, the hallway mirror, a farmers market.

**Jess:** my closet obviously, my bathroom mirror, the car at pickup, and like target runs and my starbucks drive thru haha

**Claude:** Those are great, very real. Two of them name real stores, and store names, logos and signs can't appear in the photos, so here's what I decided: her walk-in closet by the mirror, her bathroom vanity mirror, the driver's seat of her car in the pickup line, and the window seat of a neighborhood coffee shop with no signs or writing. I dropped the big-box store aisle, because shelves full of labelled products make it almost impossible to keep text out of the photo.

> **[TEST NOTE]** 02 line 21 and line 36 never say PERSONA WORLD must be brand-free. Jess's natural answer contained two brands. See F-08.

**Claude:** Fifth: what time zone are you in, and when is your computer usually on?

**Jess:** eastern. I'm on it from like 7am till 11ish at night. sometimes I close it earlier if I crash lol

**Claude:** Here's what I propose, all Eastern:
- Themed looks: a weekly build on Saturday at 1:05 pm. Flat lay pins at 1:30 pm, second pins at 8:30 pm.
- Pull sweep: daily at 12:00 pm and 6:00 pm.
- If you're a Brand Closet™ member (that's my next question): a nightly Outfit of the Day run Sunday to Friday at 9:20 pm, flat lays at 4:30 pm, lifestyle pins at 9:30 am.

All of those are inside your 7 am to 11 pm window. How many looks a week? 3 is light, 5 is steady, 7 is one a day. More looks means a longer weekly run and more of your Claude usage.

**Jess:** 5 I guess? whatever's normal

**Claude:** 5 it is. That's the steady pace.

> **[TEST NOTE]** Question 5 has to propose Outfit of the Day times "if she's a member" before question 6 asks whether she is. Claude had to hedge in the chat. See F-05.
> **[TEST NOTE]** Jess said "11ish" and "sometimes earlier". The kit only moves times the computer is OFF, so 9:20 pm stays. A two-outfit night (the recipe allows up to 2) can easily run past 11 pm. See F-15.

**Claude:** Last one: are you a member of The Brand Closet™ at the $9/month tier or above? That tier carries the Outfit of the Day, which automation 2 needs.

**Jess:** yes I'm on the $9 one. oh and can I do that recommend-it card thing later? the brand closet one

**Claude:** Yes to both. Automation 2 is on. The recommend-it card lives on your own website's shop-the-look pages, so it needs the blog half first (09_THE_BLOG_HALF.txt). I've written "wanted later" in your recipe so it's not forgotten. Nothing about it goes on your pins for now.

> **[TEST NOTE]** 05_RECOMMEND_IT_TOO.txt still ships with a KIT BUILD NOTE and both VERSION A and VERSION B, so Claude cannot tell Jess whether she will get a referral link. See F-01. The setup prompt also has no field for "card wanted later"; Claude invented one. See F-26.

---

*(Claude writes MY_RECIPE.txt, storefront-log.md, pin-tab.md, browser-lock.txt and MY_SCHEDULED_TASKS.txt, then reads each back.)*

**FINISH check, as run by Claude:**
- Boards: both marked "confirmed public on 28 September 2026". Pass.
- Posting slots in one day: 9:30 am, 1:30 pm, 4:30 pm, 8:30 pm. Closest pair 3 hours apart. Pass. (Run times 12:00 pm, 1:05 pm, 6:00 pm, 9:20 pm are runs, not pin slots, so they are not in this check. The weekly run at 1:05 pm sits 25 minutes before the 1:30 pm pin slot, which would fail if "slots" meant run times too.)
- No slot shared between automations. Pass.
- Every run at or after 7:00 am. Pass.
- Disclosure line matches Influencer path. Pass.

**Claude (final, five lines):**
You're set up: pink girly outfits on the Influencer path with your persona, 5 themed looks a week plus the Outfit of the Day.
Your pins go to Pink Outfit Ideas (themed) and Pink Outfit of the Day (Outfit of the Day), all times US Eastern.
First run: tonight, Monday 28 September, 9:20 pm, the nightly Outfit of the Day (the first weekly build is Saturday 3 October at 1:05 pm).
Your recipe renews on 28 March 2027.
Next step: open the Setup Guide PDF at step 6 and create the three scheduled tasks from MY_SCHEDULED_TASKS.txt.

> **[TEST NOTE]** "First run" is ambiguous: the pull sweep at 12:00 pm today would technically run first, but it opens nothing on empty files. Claude named the first run that does work.
