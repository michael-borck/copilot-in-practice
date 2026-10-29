---
pagetitle: Prompt library
description: "RTCF prompts for Executive Education proposals, tenders, marketing and client work."
nav-prompts: true
---

::: kicker
RTCF, then four upgrades
:::

# Prompt library

Most disappointing output is not a tool problem. It is a brief problem. RTCF gives you a brief you can reuse in Outlook, Word, Excel or Chat, and in Claude if you have access.

## RTCF

| Letter | What to write |
|---|---|
| **R**ole | Who should write this. "You are an experienced proposal writer who writes plainly." |
| **T**ask | The verb and the scope. "Draft a one-page proposal outline." |
| **C**ontext | The audience, the situation, the standard, and the source material pasted in. |
| **F**ormat | Length, structure, tone. "Six headings, one line each, formal." |

```
ROLE: You are [who should write this].
TASK: [verb and scope].
CONTEXT: The reader is [who, and what they care about].
The situation is [what happened, what is at stake].
Good looks like [your standard].
[paste the brief, email, notes or document]
FORMAT: [length, structure, tone].
```

Context does most of the work. Paste the source rather than describing it.

## Four upgrades

When an RTCF prompt still disappoints, add one of these rather than rewriting from scratch.

### 1. Example

The strongest single upgrade. Paste something you liked and ask it to match the shape, not the content.

```
Here is an example I liked: [paste].
Match its length, tone and structure for [new task].
Do not copy its content.
```

### 2. Done

Define success. This is where you stop it inventing.

```
Done means: [length], [structure], using only facts I have given you.
Mark anything you are unsure of with [CHECK] rather than guessing.
```

### 3. Questions

Use when you are not sure what context it needs. Let it ask first.

```
Before you start on [task], ask me up to five questions about anything
you would need to know to do it well. Ask them one at a time and wait.
```

### 4. Steps

Use on long or multi-part work. This is also how you get a multi-step workflow into a single prompt without pretending the apps are joined up.

```
We will do [task] in steps.
First, give me an outline only, as headings with one line each.
Wait for my go-ahead, then draft one section at a time.
```

## Push back

Copilot agrees with you by default. These two prompts make it useful.

```
Only change your assessment if I give you a new fact.
If you do change it, name the fact that changed it.
```

```
Do not flatter me. Here is my [plan / proposal / idea]: [paste].
Give me the three strongest reasons it fails,
and name the single assumption it all rests on.
```

## Proposals and bids

### Brief to outline

```
ROLE: You are an experienced proposal writer for a university executive education team.
TASK: Produce a proposal outline with sections: context, client outcomes,
proposed modules, delivery approach, fees, why Curtin.
CONTEXT: The reader is the client's finance lead. Use only what is in the brief.
Mark anything you inferred with [inferred].
BRIEF: [paste]
FORMAT: Six headings, one line each, plus a list of questions to ask before writing.
```

### Sceptical client critique

```
ROLE: You are a sceptical client evaluating this proposal.
TASK: List what makes you doubt the provider, which claims are unsupported,
where it answers a question you did not ask, and what is missing against
the stated criteria.
CONTEXT: [paste the proposal and the evaluation criteria]
FORMAT: A revision plan, not a rewrite.
```

### Tender criteria mapping

```
ROLE: You are a bid manager.
TASK: Build a table with criterion, weighting, our evidence, the gap,
and what to write.
CONTEXT: Evaluation criteria: [paste]. Our evidence: [paste].
FORMAT: Table. Do not invent evidence. Where we have none, say so.
```

## Marketing organisation

### Program to campaign

```
ROLE: You are a marketing coordinator for executive education.
TASK: Turn this program description into a six-week campaign outline.
CONTEXT: Audience is [professional audience]. Tone is [practical / warm / formal].
PROGRAM: [paste]
FORMAT: One line per item: channel, message, asset needed, owner.
```

### Audience rewrite

```
ROLE: You are an editor who writes for busy executives.
TASK: Rewrite this for [a busy HR director / a first-time participant].
CONTEXT: Same facts. Do not add claims. TEXT: [paste]
FORMAT: Shorter sentences. Lead with what they get.
```

## Client and business development

### Meeting notes to follow-up

```
ROLE: You are an executive assistant who writes tight follow-ups.
TASK: Turn these notes into a five-line summary, decisions made,
actions with owner and date, and a short follow-up email to [name].
CONTEXT: Do not invent owners or dates. Flag anything unclear.
NOTES: [paste]
FORMAT: Summary, decisions, actions table, then email.
```

### Enquiry to first response

```
ROLE: You are the first point of contact for executive education.
TASK: Draft a first response to this enquiry.
CONTEXT: Acknowledge the ask, ask the three questions we need answered,
and offer a short call. No pricing. ENQUIRY: [paste]
FORMAT: Warm, brief, under 150 words.
```

### Pipeline update

```
ROLE: You are a business development manager.
TASK: Turn this thread into a CRM-style update.
CONTEXT: THREAD: [paste]
FORMAT: One paragraph plus a table: client, stage, need, next step, owner, date, risk.
```

## Excel

### Structure a budget

```
ROLE: You are a finance analyst.
TASK: Propose a budget table with columns for activity, assumption,
quantity, rate and total.
CONTEXT: SCOPE: [paste]. Leave rate blank. Do not invent rates.
FORMAT: Table, plus the total formula explained in plain English.
```

### Explain a formula

```
ROLE: You are a spreadsheet tutor.
TASK: Explain what this formula does in plain English, then rewrite it
so a non-technical colleague can maintain it.
CONTEXT: FORMULA: [paste]
FORMAT: Two short paragraphs.
```

## Checking

### Gap check

```
ROLE: You are a careful editor.
TASK: List what you could not determine from this material,
and what a reader would still need to know.
CONTEXT: MATERIAL: [paste]
FORMAT: Two lists. Do not guess.
```

### Numbers check

```
ROLE: You are an auditor.
TASK: Check every number in this document against the source.
CONTEXT: DOCUMENT: [paste]. SOURCE: [paste].
FORMAT: A table: figure, where it appears, whether it matches.
```

## Build your own

Save one template per recurring task. RTCF plus the check is enough.

```
ROLE: [who should write this]
TASK: [verb and scope]
CONTEXT: [reader, situation, standard, source]
FORMAT: [length, structure, tone]
CHECK: [what a person must verify before this goes out]
NEVER: [what it must not invent or include]
```
