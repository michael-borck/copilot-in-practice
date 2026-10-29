---
pagetitle: What Copilot can see
description: "Where Copilot has context, what the licence changes, and how to carry work between apps."
nav-context: true
---

::: kicker
Session 3 · 10:00
:::

# What Copilot can see

Copilot answers from what it can see. What it can see depends on three things:

1. The app you are in.
2. The licence you have.
3. How Curtin has configured the tenant.

Two people can be on the same licence and still get different buttons, because the tenant settings decide which features are switched on. So the useful skill is not memorising the product. It is checking your own setup, and checking again after an update.

## The wall between apps

```{=html}
<div class="flow">
  <div class="step"><b>Outlook</b><span>The selected email, and with a licence, the mailbox and calendar.</span></div>
  <div class="step"><b>Word</b><span>The open document, and files you point it to.</span></div>
  <div class="step"><b>Excel</b><span>The open workbook, and the range you select.</span></div>
  <div class="step"><b>Chat</b><span>The web, the page you are on, and what you paste or upload.</span></div>
  <div class="step"><b>You</b><span>The doorway. You carry the work across on purpose.</span></div>
</div>
```

There is a wall between each box. Copilot does not pass work from Outlook to Word for you. That is not a bug to wait out. It is where judgement enters.

## What each place can see

| Where you are | What Copilot usually sees |
|---|---|
| Copilot in Outlook, with an email selected | The open email, and with an add-on licence, your mailbox, calendar and related files |
| Copilot in Outlook, nothing selected | The mailbox and calendar, to the extent your licence and tenant allow |
| Copilot in Word | The open document, and files you point it to with a licence |
| Copilot in Excel | The open workbook, and the range or table you select |
| Copilot in PowerPoint | The open deck |
| Copilot Chat in the browser or Edge | The web, the page you are on, and anything you paste or upload. Work data only with an add-on licence and a tenant that allows it |
| Copilot Chat in Teams | The open chat or meeting, and with a licence, work data |

The middle column is a guide, not a promise. Microsoft changes it. Verify on your own screen.

## Check what you have

1. Sign in at `copilot.cloud.microsoft` with your Curtin account.
2. Look under your name. You will see Copilot Chat (Basic), M365 Copilot (Basic) or M365 Copilot (Premium).
3. Basic means web reasoning plus the content you open or upload. Premium adds work data through Work IQ, Microsoft's work-data layer, which builds on Microsoft Graph.
4. Open the same chat inside Outlook and ask the same question. Note the difference.

Ask this question of your own setup: **"What can you see about my work right now?"** The answer tells you what to trust it with.

::: note
Microsoft is actively changing this. A 2026 roadmap item extends Copilot Chat in Outlook to reason over the whole inbox and calendar for people without an add-on licence, due around October 2026. By the time you read this, your screen may differ from the person next to you. Check, do not assume.
:::

## The carry pattern

Copilot does not move work between apps for you. You do. That is fine once it becomes a habit.

1. **Gather** in the app that holds the context. In Outlook, select the email. In Word, open the document. In Edge, open the page.
2. **Extract** what matters. Ask for the decisions, dates, asks and numbers. Keep it short.
3. **Carry** it. Copy the result and paste it into the next app. Say where it came from.
4. **Refine** in the destination. Ask for the shape you need.
5. **Check** before it moves on. Names, figures, commitments.

Every arrow is a copy and paste by a person. That is why the output is still yours.

## When carrying is not practical

Sometimes you want the whole job in one place. You can batch several steps into a single prompt, as long as you accept that it is still one context and one output.

```
We will do [task] in steps.
1. Summarise the brief.
2. Identify the decisions the client needs to make.
3. Draft an outline.
4. List the gaps.
Do step 1 only, then wait for me to say continue.
```

This does not join the apps. It just stops you making five separate prompts in one chat. Use it for work that fits inside one document.

## Agents

An agent is a brief that remembers. There are three tiers, and only the first is something you use without setting anything up.

| Tier | What it is | What you do |
|---|---|---|
| Built-in | Analyst, Researcher, Facilitator, Writing Coach, Idea Coach | Use it. You do not build or maintain it. |
| Custom | Instructions plus files, built inside Copilot | Build it from your best RTCF prompt. The Custom GPT equivalent. |
| Copilot Studio | Actions, connectors, systems | A project with an owner, a knowledge source and governance. |

Custom agents do not talk to each other, do not run on their own, and do not hand work to the next app. They are a saved prompt with a name and some files attached. Useful when you do the same task often. Not automation.

Before you build one, do the workflow manually twice. If the prompt and the check work, the agent is just packaging.

## Personalisation and memory

Copilot remembers context to be useful. That is helpful and also something to manage.

- Look for personalisation or memory settings in Copilot settings. The exact menu name moves, so use the search box.
- Review what it has remembered. Delete anything wrong, stale or about a client.
- If you share a machine or demo account, check what is remembered before you present.
- Turning memory off is reasonable for sensitive work. You will need to supply context each time.

## Edge

- Sign in with the Curtin account, not a personal one, or you get the consumer experience.
- Work mode and web mode are different. Check which one you are in.
- Uploading a file is a deliberate act. Confirm the file, the permissions and the audience before you attach it.
- The page you have open is context. Close anything you would not want summarised if you are sharing your screen.
