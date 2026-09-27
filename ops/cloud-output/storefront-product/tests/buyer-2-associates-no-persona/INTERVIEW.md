# Simulated setup interview: Dana (Associates only, no persona, Squarespace)

Setting: Claude desktop app, new chat, While-You-Sleep Storefront folder attached. Dana pasted 02_SETUP_PROMPT.txt. Today is Sunday 27 September 2026.
Simulated folder path used below: `~/Documents/While-You-Sleep Storefront`

Tester notes in [square brackets] mark every place where Claude had to improvise because the prompt did not cover the situation. These feed FINDINGS.md.

---

**Claude:** Hi Dana. I've read the recipe files (03, 04, 06, 07 and 08). There's no MY_RECIPE.txt in your folder yet, so we're starting fresh. Six questions, one at a time.

**1. Your theme.** What's your look? Describe it the way you'd describe your Pinterest to a friend. For example: "cozy neutral mom style", "pink everything, girly and a bit extra", or "coastal grandmother home decor".

**Dana:** ha literally coastal grandmother home decor. and a few linen outfits. nancy meyers kitchen vibes basically

**Claude:** Love it. Quick note: I'll keep film and real-person names out of every pin, image and hashtag, so "Nancy Meyers" stays our shorthand and never appears on a pin. Clothing, home, or both?

[Tester: R5 bans film stills and likenesses in images, and R6 bans brand names in copy, but nothing bans naming a real person or a film in pin titles, descriptions or hashtags (#nancymeyers). Claude added this on its own.]

**Dana:** both but mostly home. like 1 outfit for every 3 home ones maybe

**Claude:** Got it: mostly home, with roughly one linen outfit for every three home looks. I'll write that into your recipe so the weekly task keeps the mix.

[Tester: MY_RECIPE.txt has no field for the mix. Claude put it in the theme summary line.]

**2. Your boards.** Which Pinterest boards should the pins go on? Give me their exact names. If you don't have them yet, tell me and I'll suggest names people actually search for.

**Dana:** Coastal Grandmother Decor and Linen Outfits Over 40

**Claude:** Perfect, those are already search-friendly. Please open each board and check it says Public, not Secret. Secret boards reach nobody. (On the Pinterest app: tap the board, then the three dots, then Edit board, and look at "Keep this board secret". It should be off.)

**Dana:** pretty sure they're public

**Claude:** Could you take ten seconds and check each one? The weekly task stops cold if a board is secret, so it's worth knowing now.

**Dana:** ok checked. both public, secret toggle is off on both

**Claude:** Thank you. Both confirmed public today.

**3. Your storefront.** Are you an approved Amazon Influencer with a storefront? If yes, paste your storefront address (it looks like amazon.com/shop/yourname). If you're Associates only, say "Associates only".

**Dana:** associates only. i tried influencer once and they wanted instagram or youtube or something, i don't really do those

**Claude:** No problem. Do you have your own website where a shop-the-look page can live? Paste the address, or say no.

**Dana:** danashoreandhome.com

**Claude:** Great. One thing I can't work out myself: what is the site built on? For example Squarespace, Wix, WordPress, Shopify, or a Weekend Ecosystem site.

[Tester: 02 question 3 never asks the site platform, yet 08 line 29 says the whole path changes on it (Weekend Ecosystem publishes itself, anything else is hand-work). Claude had to add a question. The "one short follow-up" rule is already used up by the website question, so this is a second follow-up the prompt did not plan for.]

**Dana:** squarespace

**Claude:** Thanks. Here's the honest part, so you hear it now and not on day three:

- Your pins will link to a shop-the-look page on danashoreandhome.com, one page per look.
- The weekly task can't publish to Squarespace for you. It will write each look's page into your folder, ready to paste, and you paste it into Squarespace yourself. With 3 looks a week that's roughly 30 to 45 minutes of your time each week (about 10 to 15 minutes a page, including adding the two pin images).
- A pin never links to a page that doesn't load, so each look's pins wait until you've pasted its page. Paste late and the pins go out late.

Two quick checks before we go on, because the Associates path depends on them:

a) Amazon needs every place your links appear listed in your Associates account. Is danashoreandhome.com listed there? (Associates Central, your account name at top right, Account Settings, then the websites and mobile apps list.)
b) Pinterest has to accept your site as a link. On pinterest.com, start a new pin, paste https://danashoreandhome.com into the link field and tell me if it's accepted. You can close the pin without saving.

[Tester: neither check is in 02. Check (b) is required by 08 line 31 ("Tell your setup chat and it'll switch you to the fallback"), but the setup prompt never asks for it and has no fallback to switch to. Check (a) is required by 08 line 22 and never asked.]

**Dana:** oh. ok that's more than i thought, the sales page said no building no posting?? but fine, i can do sunday mornings with coffee. i think the site is listed, i used it when i signed up for associates. pinterest took the link, no error

**Claude:** That's fair, and you're right that the "no building, no posting" line is written for the Idea List path. On yours, the pins, images, links and pin copy are all done for you; the one thing you do is paste each page. I'll plan around Sunday mornings: the weekly run builds on Saturday, you paste Sunday morning, and the first pin of each week goes out Monday. I've noted the Associates site listing as "she believes it's listed", and I'd suggest a quick look in Associates Central when you're next at the computer.

[Tester: the promise mismatch surfaced in the interview itself. The Monday start is Claude's own decision; nothing in the kit lets the setup chat move look days.]

**4. Your persona.** Do you have an AI persona, a consistent AI model who wears the looks? If yes, put her reference image in this folder and tell me the file name.

**Dana:** no. and i don't want one tbh, the AI people thing is a little creepy to me

**Claude:** Totally fine. Here's the difference in one line each:
- Persona path: pin 2 is your AI model wearing the look, made in Gemini from her reference image.
- No-persona path: both pins are person-free, a styled flat lay and a "that girl" collage, made in Seedream 4.5 on Higgsfield. No faces, no Gemini.

You're on the no-persona path. It suits home decor well.

**5. Your times.** What time zone are you in, and when is your computer usually on?

**Dana:** eastern. it's on like 9 to 6 and then i shut it off, i don't do computer at night

**Claude:** Is that every day, including Saturdays?

**Dana:** weekdays yes. weekends usually on during the day but sometimes i'm out

**Claude:** Thanks. Here's what I propose, all Eastern time (New York):

- Weekly themed-look build: Saturday at 1:05 pm. Inside your hours. If you're out and the computer is off, the run waits until you turn it back on.
- Pin posting slots: first pins at 1:30 pm, second pins at 8:30 pm. Your computer does NOT need to be on for these. The weekly run schedules the pins on Pinterest ahead of time, and Pinterest posts them itself. 8:30 pm is a good evening slot for home decor, so I've kept it.
- Pull sweep (removes any pin you mark PULL, and schedules pins whose pages you've pasted): daily at 12:00 pm and 5:00 pm. I moved the evening one from 6:00 pm to 5:00 pm so it doesn't start as you're shutting down.
- One thing to know: to pull an 8:30 pm pin through the sweep, mark it PULL before 5:00 pm that day. After that, delete it on Pinterest yourself.

[Tester: 02 line 28 says "Move any time she says her computer is off." Read literally, that moves the 8:30 pm posting slot too, which is wrong: posting slots run on Pinterest's servers. Claude kept 8:30 pm and explained. A less careful run would have crammed both pin slots into 9 to 6.]

How many looks a week? 3 is light, 5 is steady, 7 is one a day. More looks means a longer weekly run and more of your Claude usage.

**Dana:** 3 is plenty

**Claude:** 3 it is. With Sunday-morning pasting, your looks go out Monday, Wednesday and Friday at 1:30 pm, and each look's second pin 3 days later at 8:30 pm (Thursday, Saturday and Monday). No two pins within an hour, nothing before 7:00 am, nothing more than 14 days ahead.

**Dana:** sounds good

**6. The Brand Closet™.** Are you a member of The Brand Closet™ at the $9/month tier or above? That tier carries the Outfit of the Day, which automation 2 needs.

**Dana:** no whats that. no thanks

**Claude:** No problem. It's optional, and 04_OUTFIT_OF_THE_DAY_RECIPE.txt starts with how to join if you ever want it. Skipping automation 2.

Writing your files now.

[Files written: MY_RECIPE.txt, storefront-log.md, pin-tab.md, browser-lock.txt, MY_SCHEDULED_TASKS.txt. Read-back check run: boards confirmed public 2026-09-27; pin slots 1:30 pm and 8:30 pm are 7 hours apart; run times 12:00 pm, 1:05 pm, 5:00 pm all at or after 7:00 am; one automation only, so no shared slots; disclosure line is the Associates version. All passed.]

**Claude (finish, five lines):**
Set up: themed looks only, no-persona path, Associates-only with shop pages on danashoreandhome.com, 3 looks a week, Eastern time.
First run: Saturday 3 October 2026 at 1:05 pm. Its pages land in your folder; paste them Sunday morning and the pins go out from Monday 5 October at 1:30 pm.
Your weekly part: paste each look's page into Squarespace (about 10 to 15 minutes a page). Everything else runs itself.
Before Saturday: confirm danashoreandhome.com is listed in Associates Central.
Next step: open the Setup Guide PDF at step 6 and create the two scheduled tasks from MY_SCHEDULED_TASKS.txt.

[Tester: the prompt allows "the one next step" only. Dana has three real next steps (create tasks, confirm Associates site listing, set up a Squarespace page home for the looks). Claude squeezed two into five lines and still had no room to say where in Squarespace the pages go, because the kit never defines it.]
