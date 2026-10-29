# Prompt library

Starter prompts for Executive Education work. Build them with RTCF, then add an upgrade if the output misses.

## RTCF

- **Role:** who should write this.
- **Task:** the verb and the scope.
- **Context:** the reader, the situation, the standard, and the source pasted in.
- **Format:** length, structure, tone.

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

**Example.** Paste one you liked and ask it to match the shape, not the content.

```
Here is an example I liked: [paste].
Match its length, tone and structure for [new task].
Do not copy its content.
```

**Done.** Define success, and make it mark uncertainty.

```
Done means: [length], [structure], using only facts I have given you.
Mark anything you are unsure of with [CHECK] rather than guessing.
```

**Questions.** Let it ask first when you are not sure what it needs.

```
Before you start on [task], ask me up to five questions about anything
you would need to know to do it well. Ask them one at a time and wait.
```

**Steps.** Split a long job. This is also how you batch a workflow into one prompt.

```
We will do [task] in steps.
First, give me an outline only, as headings with one line each.
Wait for my go-ahead, then draft one section at a time.
```

## Push back

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

```
ROLE: You are an experienced proposal writer for a university executive education team.
TASK: Produce a proposal outline with sections: context, client outcomes,
proposed modules, delivery approach, fees, why Curtin.
CONTEXT: The reader is the client's finance lead. Use only what is in the brief.
Mark anything you inferred with [inferred].
BRIEF: [paste]
FORMAT: Six headings, one line each, plus a list of questions to ask before writing.
```

```
ROLE: You are a sceptical client evaluating this proposal.
TASK: List what makes you doubt the provider, which claims are unsupported,
where it answers a question you did not ask, and what is missing against
the stated criteria.
CONTEXT: [paste the proposal and the evaluation criteria]
FORMAT: A revision plan, not a rewrite.
```

```
ROLE: You are a bid manager.
TASK: Build a table with criterion, weighting, our evidence, the gap,
and what to write.
CONTEXT: Evaluation criteria: [paste]. Our evidence: [paste].
FORMAT: Table. Do not invent evidence. Where we have none, say so.
```

## Marketing organisation

```
ROLE: You are a marketing coordinator for executive education.
TASK: Turn this program description into a six-week campaign outline.
CONTEXT: Audience is [professional audience]. Tone is [practical / warm / formal].
PROGRAM: [paste]
FORMAT: One line per item: channel, message, asset needed, owner.
```

```
ROLE: You are an editor who writes for busy executives.
TASK: Rewrite this for [a busy HR director / a first-time participant].
CONTEXT: Same facts. Do not add claims. TEXT: [paste]
FORMAT: Shorter sentences. Lead with what they get.
```

## Client and business development

```
ROLE: You are an executive assistant who writes tight follow-ups.
TASK: Turn these notes into a five-line summary, decisions made,
actions with owner and date, and a short follow-up email to [name].
CONTEXT: Do not invent owners or dates. Flag anything unclear.
NOTES: [paste]
FORMAT: Summary, decisions, actions table, then email.
```

```
ROLE: You are the first point of contact for executive education.
TASK: Draft a first response to this enquiry.
CONTEXT: Acknowledge the ask, ask the three questions we need answered,
and offer a short call. No pricing. ENQUIRY: [paste]
FORMAT: Warm, brief, under 150 words.
```

```
ROLE: You are a business development manager.
TASK: Turn this thread into a CRM-style update.
CONTEXT: THREAD: [paste]
FORMAT: One paragraph plus a table: client, stage, need, next step, owner, date, risk.
```

## Excel

```
ROLE: You are a finance analyst.
TASK: Propose a budget table with columns for activity, assumption,
quantity, rate and total.
CONTEXT: SCOPE: [paste]. Leave rate blank. Do not invent rates.
FORMAT: Table, plus the total formula explained in plain English.
```

```
ROLE: You are a spreadsheet tutor.
TASK: Explain what this formula does in plain English, then rewrite it
so a non-technical colleague can maintain it.
CONTEXT: FORMULA: [paste]
FORMAT: Two short paragraphs.
```

## Checking

```
ROLE: You are a careful editor.
TASK: List what you could not determine from this material,
and what a reader would still need to know.
CONTEXT: MATERIAL: [paste]
FORMAT: Two lists. Do not guess.
```

```
ROLE: You are an auditor.
TASK: Check every number in this document against the source.
CONTEXT: DOCUMENT: [paste]. SOURCE: [paste].
FORMAT: A table: figure, where it appears, whether it matches.
```

## Build your own

```
ROLE: [who should write this]
TASK: [verb and scope]
CONTEXT: [reader, situation, standard, source]
FORMAT: [length, structure, tone]
CHECK: [what a person must verify before this goes out]
NEVER: [what it must not invent or include]
```
