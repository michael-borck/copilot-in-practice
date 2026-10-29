---
pagetitle: Exercises
description: "The four hands-on exercises: brief, outline, critique and budget table."
nav-exercises: true
---

::: kicker
Session 4 · 11:00 to 11:45
:::

# Exercises

Work in pairs or threes. Use one of the sanitised briefs:

- [Professional development proposal](downloads/brief-professional-development-proposal.docx) (Word)
- [International tender response](downloads/brief-international-tender-response.docx) (Word)

Both keep the structure of a real document with client names, staff names, rates and totals removed. The tender brief is harder. Use the proposal brief if you want a gentler start.

```{=html}
<div class="flow">
  <div class="step"><b>1 Find · Outlook</b><span>Select the brief. Extract the decisions and the asks.</span></div>
  <div class="step"><b>2 Draft · Word</b><span>Paste the brief. Ask for the house structure.</span></div>
  <div class="step"><b>3 Challenge · Chat</b><span>Red-team it as a sceptical client. Mark inferences.</span></div>
  <div class="step"><b>4 Quantify · Excel</b><span>Scope to a table. Trace every number.</span></div>
  <div class="step"><b>5 Send · Outlook</b><span>Check names, figures, commitments. A person sends.</span></div>
</div>
```

The four exercises are one chain, not four separate tasks. Each one picks up what the last one produced.

## Exercise 1 · Find the brief

::: {.pill}
10 min
:::

Open the brief in Word or paste it into Copilot Chat. Ask for:

- the client's stated outcomes
- what they actually need but did not say
- the three decisions the proposal must help them make
- the questions we should ask before writing

Compare answers across pairs. The differences show how much the prompt and the pasted context matter.

```
Read this brief. Give me:
1. the client's stated outcomes, in their words
2. what they need but did not say
3. the three decisions the proposal must help them make
4. the questions we should ask before writing
Mark anything you inferred rather than read.
BRIEF: [paste]
```

## Exercise 2 · Draft the outline

::: {.pill}
15 min
:::

Move to Word. Paste the brief and your Exercise 1 output. Ask for an outline that follows the house structure: context, client outcomes, proposed modules, delivery approach, fees, why Curtin.

Then tighten it with a second prompt. Cut anything generic. Keep only what is specific to this brief. Mark anything inferred.

```
Here is the brief and my notes. Produce a proposal outline with sections:
context, client outcomes, proposed modules, delivery approach, fees, why Curtin.
Use only what is in the material. Mark inferences with [inferred].
Then cut anything that would be true of any provider.
BRIEF: [paste]
NOTES: [paste]
```

## Exercise 3 · Challenge it

::: {.pill}
15 min
:::

Ask Copilot to act as a sceptical client. Then ask for a revision plan, not a rewrite. Revise one section by hand. The critique is useful. The rewrite is yours.

```
Act as a sceptical client reading this outline. Tell me:
- what makes you doubt this provider
- which claims are unsupported
- where it answers a question you did not ask
- what is missing against the evaluation criteria
Give me a revision plan, not a rewrite.
OUTLINE: [paste]
```

::: note
Watch for agreement. If you push back and Copilot immediately concedes, that is sycophancy, not a better answer. Ask it to give the strongest case against its own position before it responds.
:::

## Exercise 4 · Quantify it

::: {.pill}
5 min
:::

In Excel, paste the scope list and ask for a table with columns for activity, assumption, quantity, rate and total. Leave rates blank. Ask Copilot to explain any formula it writes.

```
Here is the scope. Propose an Excel table with columns:
activity, assumption, quantity, rate, total.
Leave rate blank. Give me the formula for total in plain English,
then the formula itself. Do not invent rates.
SCOPE: [paste]
```

## Debrief

Come back together for five minutes. Ask:

- What did Copilot get right that surprised you?
- Where did it invent something?
- Which prompt made the biggest difference?
- What would you check before this went to a client?

## If you finish early

Take the tender brief. Map its evaluation criteria to evidence you already have. The gap column is the useful part.
