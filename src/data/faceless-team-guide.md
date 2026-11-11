# Build & Sell Your Own Bot

## What a bot actually is

A bot is written instructions that make an AI do one job the way you do it. That is all. In Claude it is called a skill: a small folder with one instructions file inside. You do not code anything. If you can explain a task to a new assistant, you can build a bot.

Why it is worth more than a list of prompts: a prompt is something a person has to find, paste and adjust every time. A bot is installed once and then works whenever the task comes up. It asks the right questions, follows your steps, checks its own work and hands over a finished result.

## Step 1 · Pick the right task

Do not invent a product. Look at what you already do.

A task makes a good first bot when all three are true:
1. **You do it often.** You have a routine for it, maybe a checklist or a template.
2. **You do it better than a generic answer.** You know the mistakes, the order, the things nobody tells beginners.
3. **The result can be judged.** A pin is the right length or it is not. A listing has every part or it does not.

One bot, one job. "Writes my Etsy listings" is a bot. "Runs my Etsy shop" is five bots.

Ideas to get you started: writing a listing for one kind of product, turning a blog post into a week of posts, replying to a kind of customer message, planning a kind of week, checking a draft against your own rules, building a kind of document from a few answers.

## Step 2 · Get what you know out of your head

This is the part that makes your bot yours. Answer these, with real examples wherever you can:

1. What does someone give the bot to start?
2. What does a finished, good result look like? Paste one you are proud of.
3. What are your steps, in order?
4. What do beginners get wrong?
5. What are your rules, and **why** does each one exist?
6. What must it never do?
7. How should it talk to the person using it?

The "why" matters most. "Keep titles under 100 characters" makes a bot that obeys. "Keep titles under 100 characters because longer ones get cut off in search" makes a bot that understands, and it will handle the cases you did not think of.

The Bot Builder Bot asks you all of this in small rounds, so you never face a blank page.

## Step 3 · Write the instructions

Your bot's folder holds one required file, called SKILL.md. It has two parts.

**The top:** the bot's name and a description. The description is how the AI decides when to use your bot, so say what it does and include the things a person would actually type.

**The body:** the brief. Who the user is, the job, the steps, what a good result looks like, your rules with their reasons, and the rules that protect the user.

Three things that separate a good bot from an average one:
- **It asks before it guesses.** And it asks with numbered choices, not open questions.
- **It checks its own work.** If anything can be counted or ticked off, add a small checking script. The Bot Builder Bot writes these for you.
- **It refuses to make things up.** No invented facts, numbers, reviews or results. Say so in the instructions.

## Step 4 · Test it properly

1. Write down three things a real user would type. Make one of them awkward: missing information, a strange request, a beginner who does not know the words.
2. Install the bot and open a **brand-new chat**. Try all three.
3. Read the results as a buyer would. Would you pay for that?
4. Hand it to one other person and watch without helping. Every place they get stuck is a fix.
5. Fix the instructions, not the single answer. Then test again.

Your first version will not be good enough to sell. The second or third usually is.

## Step 5 · Package it

The Bot Builder Bot does this for you and hands you one file ending in `.skill`. To do it by hand: put SKILL.md (and any references or scripts folders) inside a folder named exactly the same as the bot's name, zip the folder, and rename the zip so it ends in `.skill`.

**To install a bot in Claude:**
1. Go to Settings, then Capabilities, and turn on Code execution and file creation.
2. Go to Customize, then Skills.
3. Click the plus button, then Create skill, then Upload a skill.
4. Choose the file and make sure its switch is on.

Write a one-page Start Here for your buyers with those four steps and the first five things to ask your bot.

## Step 6 · Sell it

**What you are selling** is the finished result your buyer gets, not "a bot". Lead with that. "Etsy listings written and checked in two minutes" is an offer. "An AI skill file" is a container.

**Your listing needs:**
- one sentence on what the buyer walks away with
- who it is for, and who it is not for
- what they need: a Claude account, and the one setting to turn on
- what they receive: the file, the Start Here page, any examples
- a real example of the bot's output from your own testing. This is your proof. Do not invent reviews.
- what the bot cannot do, said plainly
- your refund policy and whether updates are included

**Pricing** is your decision. Look at three comparable listings where you plan to sell and price in that range. A bundle of several bots that work together is worth more than the same bots sold apart, and it gives people a reason to buy all of them.

**Where to sell:** anywhere you already sell digital downloads. The buyer receives a file.

**Keep it honest.** Do not promise income, sales or results. Do not sell a bot that pretends to be a professional (doctor, lawyer, accountant). Do not put anyone else's paid material inside your bot. Tell buyers it is AI and that they should check its work.

## Step 7 · Keep it alive

- Keep a list of every question a buyer asks. Each one is a line to add to the instructions or the Start Here.
- When the platform or your own method changes, update the bot and send buyers the new file.
- Put a date in your Start Here so buyers know which version they have.
- Your second bot should work with your first. That is how a single product becomes a team.

## A one-page checklist

1. One task I already do often and well
2. My steps, my rules and the reason for each rule
3. One real example of a great result
4. SKILL.md written, with a clear description
5. A self-check for anything countable
6. Tested on three inputs in a brand-new chat
7. Tested by one other person
8. Packaged as a `.skill` file
9. Start Here page written
10. Listing written, with a real example and honest limits
