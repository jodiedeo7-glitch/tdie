# Simulated setup interview: buyer 1 (Kayla, Influencer, persona)

Simulation date: Sunday 27 September 2026. Claude desktop app, new chat, While-You-Sleep Storefront folder attached, 02_SETUP_PROMPT.txt pasted verbatim.
Everything under "Claude" is what Claude said. Everything under "Kayla" is the simulated buyer. Notes in [square brackets] are tester notes, not part of the chat.

---

[Claude reads 03, 04, 06, 07 and 08 first, as instructed. Claude lists the folder: 00 to 11 are present, maddie-ref.png is present, MY_RECIPE.txt is NOT present, so the "recipe already exists" branch is skipped. The Setup Guide PDF named in 00_START_HERE.txt is not in the folder. Claude does not mention it, because the prompt gives no instruction for a missing PDF.]

**Claude:** Hi Kayla! I've read the kit, so I'll only ask what I can't work out myself. Six topics, one question at a time.

First: what's your look? Describe it the way you'd describe your Pinterest to a friend. For example: "cozy neutral mom style" or "coastal grandmother home decor".

[Tester note: the prompt never tells Claude the buyer's name. Claude only knows "Kayla" because the storefront address arrives later. In a real run Claude would say "Hi!" here.]

**Kayla:** omg ok so like cozy neutral mom style?? sweaters, leggings, cute but practical bc I'm literally chasing a toddler all day lol

**Claude:** Love it. Clothing, home, or both? For example: "clothing only", "home only", or "both".

**Kayla:** both! my storefront is like half house stuff honestly

**Claude:** Got it: cozy neutral mom style, clothing and home.

Next, boards. Which Pinterest boards should the pins go on? Give me their exact names. For example: "Cozy Mom Outfits | Amazon Finds". If you don't have them yet, tell me and I'll suggest names people actually search for.

**Kayla:** I have Cozy Mom Outfits and then one for home stuff, I think it's Neutral Home Decor Finds? something like that

[Vague answer. One follow-up allowed.]

**Claude:** Could you open Pinterest and copy the home board's name exactly as it shows at the top of the board? One letter off and the task won't find it. For example: "Neutral Home Decor Finds".

**Kayla:** ok yes it's Neutral Home Decor Finds

**Claude:** Perfect. Please open each board and check it says Public, not Secret. Secret boards reach nobody. For example, you're looking for a small lock icon next to the board name: a lock means Secret.

[Tester note: the prompt only says "check it says Public, not Secret". Pinterest does not print the word "Public" on a board. Claude improvised the lock-icon hint.]

**Kayla:** cozy mom outfits is fine. wait the home one has a little lock on it?? it says secret. whoops I don't even remember doing that

**Claude:** Good catch, that would have hidden every home pin. Open Neutral Home Decor Finds, tap the three dots, choose Edit board, turn off "Keep this board secret", and save. Then reload the board and tell me when the lock is gone.

**Kayla:** ok done, no lock now

**Claude:** Thank you. Both boards confirmed public today.

[Tester note: the prompt says nothing about whether to suggest search-first names for boards she already has. Claude did not suggest renaming. "Cozy Mom Outfits" is searchable; "Neutral Home Decor Finds" is fine. Claude also did not ask about board sections, although 03 Part 5 uses sections.]

Next, your storefront. Are you an approved Amazon Influencer with a storefront? If yes, paste your storefront address. For example: amazon.com/shop/yourname. If you're Associates only, say "Associates only".

**Kayla:** yes! amazon.com/shop/kaylacozyhome

**Claude:** Great, that puts you on the Influencer path: every look gets its own Idea List in your storefront, and both pins link to it.

Next: do you have an AI persona, a consistent AI model who wears the looks? If yes, put her reference image in this folder and tell me the file name. For example: "yes, it's maddie.png".

- Persona path: pin 1 is a flat lay or collage, and pin 2 is your persona wearing the whole look, made in Gemini from her reference image.
- No-persona path: both pins are flat lays or collages, no people at all.

**Kayla:** yes!! her name is Maddie, she's blonde with long wavy hair and like 30ish, the file is called maddie ref I think

[Claude lists the folder instead of asking: the file is maddie-ref.png. Claude does not write down hair, hair length or age, per the prompt.]

**Claude:** Found her: maddie-ref.png is in the folder, so that's the one every task will attach. I'll keep her looks coming from the image only, so I won't write down anything about her hair or age. That keeps her consistent.

One more on Maddie: name three or four real-feeling places she lives her life. For example: her kitchen island, her front porch, the hallway mirror, a farmers market.

**Kayla:** her kitchen, the couch, her front porch, and like target runs lol

[Tester note: "target runs" names a real store. The setup prompt has no rule about brand or store names in PERSONA WORLD; 07 rule P3 and the no-brand rules (R5, R6, B4) imply it cannot stay. Claude decides and tells her.]

**Claude:** Lovely. One small change: I can't name a real store in her scenes (no logos or store names in any image), so I've written that one as "a big grocery store aisle with her cart, no signs". Her world is: her kitchen island, her living room couch, her front porch, and a grocery store aisle with her cart.

Next, times. What time zone are you in, and when is your computer usually on? For example: "Eastern, on from 9 am to 11 pm".

**Kayla:** central. it's on most of the day, like 8 till 10 at night-ish. sometimes I shut it when I go to bed

**Claude:** Here's what I'd suggest, all in Central time:

- Weekly build: Saturday at 1:05 pm. This is the big one: it picks the week's looks, finds the pieces, makes the images and schedules the pins.
- Pins: first pin of each look at 1:30 pm, second pin at 8:30 pm (3 days later).
- Pull sweep: daily at 12:00 pm and 6:00 pm. It removes any pin you mark PULL.

All of these sit inside your 8 am to 10 pm window. Does that work? And how many looks a week? 3 is light, 5 is steady, 7 is one a day. More looks means a longer weekly run and more of your Claude usage. For example: "5".

**Kayla:** yeah that's fine. 5 I guess? whatever's normal

**Claude:** 5 it is, that's the steady pace.

[Tester note: Kayla says she "sometimes shuts it when she goes to bed". The 8:30 pm pin slot does not need the computer (Pinterest posts it), but the prompt never explains to the buyer which times need the computer on and which don't. Claude did not explain either, because the prompt doesn't ask for it. The Saturday build at 1:05 pm has no stated duration, so Kayla has no idea she must leave the computer on all Saturday afternoon.]

Last one: are you a member of The Brand Closet™ at the $9/month tier or above? That tier carries the Outfit of the Day, which automation 2 needs. For example: "yes, $9 tier" or "no".

**Kayla:** no?? what is that

**Claude:** It's Rose's styling community, and it's optional: automation 2 uses its Outfit of the Day, and 04_OUTFIT_OF_THE_DAY_RECIPE.txt starts with how to join if you ever want it. You're all set without it.

[Claude writes the five files. Decisions Claude made that the prompt did not cover, and told Kayla about:
1. Which board gets which kind of look (outfits to Cozy Mom Outfits, home to Neutral Home Decor Finds).
2. Pin 2 for HOME looks on the persona path: the kit's persona prompt dresses her in "every item", which cannot work for a throw blanket or a lamp. Claude decided home looks use the no-persona pin 2 (the other collage format).
3. Store name removed from PERSONA WORLD.
4. Folder name: read from the attached folder as "While-You-Sleep Storefront".
Claude reads every file back and checks: boards confirmed public (yes), no two pin slots within an hour (1:30 pm and 8:30 pm, 7 hours apart), no shared slot between automations (automation 2 not set up), every run at or after 7:00 am (12:00 pm, 1:05 pm, 6:00 pm), disclosure matches Influencer path (yes).]

**Claude:** All done. I've written MY_RECIPE.txt, storefront-log.md, pin-tab.md, browser-lock.txt and MY_SCHEDULED_TASKS.txt into your folder.
Your setup: cozy neutral mom style, clothing and home, 5 looks a week, Maddie on pin 2 for outfits, both boards public, Idea Lists as the pin link.
Two calls I made: home looks use a second collage instead of Maddie (she can't wear a lamp), and her "target runs" became a grocery aisle with no store names.
First run: Saturday 3 October 2026 at 1:05 pm Central. Your first pins go out Sunday 4 October at 1:30 pm.
Next step: open the Setup Guide PDF at step 6 and create the two scheduled tasks from MY_SCHEDULED_TASKS.txt.

[Tester note: that is five lines, but only because two decisions were squeezed into one line. The prompt's five-line limit leaves no room to report improvised decisions. Also the "first pins go out Sunday 4 October" line is a promise the setup chat cannot verify: the weekly task decides the dates.]

**Kayla:** yay ok!! wait where's the pdf

[Tester note: the PDF is not in the kit folder (00_START_HERE.txt lists it; kit/ and pdf/ do not contain it). Claude has no instruction for this. Simulated answer below.]

**Claude:** I can't see the Setup Guide PDF in the folder you attached, only the text files. It should have come with your download, so check the email or page you bought from. In the meantime, MY_SCHEDULED_TASKS.txt has the exact name, schedule and folder to type for each task.

---

Interview length: 13 Claude turns, 12 Kayla answers (00_START_HERE.txt says "answer six questions" and "about 5 minutes"). Realistic time including finding and fixing the secret board: 10 to 15 minutes.
