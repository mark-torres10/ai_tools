## Problem

<What was wrong, missing, painful, or unclear? Who or what is affected?>

## Solution

<What changed from a caller or operator perspective? New or restored behavior.>

```diff
 <existing shape>
-  <removed>
+  <added>
```

Use a `diff` fence when the view is a change, so GitHub colors `+` and `-`. Use `text` for a new tree. See ../../shared/summary-view.md.

## Purpose

<Why this approach and scope now? Tradeoffs and what is in / out of scope.>

## How to run

```bash
<command or check that exercises the change>
```

Expected: <observable success condition>.

## Merge Danger

**Door:** one-way | two-way

<optional: why revert is expensive or incomplete, or why it is cheap>

**Blast radius:** <short phrase>

<optional: who or what breaks if this is wrong>
