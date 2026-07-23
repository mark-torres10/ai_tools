# Correct timezone handling in scheduled reports

## Summary

Scheduled report jobs computed day windows in UTC but labeled and cut those windows using the workspace timezone, so “yesterday” reports near DST transitions included the wrong hours.

Window start/end are now computed and labeled with one timezone contract: the workspace timezone end-to-end.

## Purpose

Workspaces outside UTC (especially those that observe DST) get reports whose coverage does not match the labeled date—missing late-evening rows or including early-morning hours from the adjacent day.

This fix aligns schedule window computation with workspace timezone for daily and weekly report jobs. Changing how historical reports already delivered are re-labeled is out of scope.

## Reproduction

Setup: workspace timezone `America/Los_Angeles`; a daily report scheduled for “yesterday”; run on a date immediately after a spring-forward or fall-back transition (e.g. the Monday after US DST change).

1. Ensure the report source has events in the disputed boundary hours (local midnight ± 2h around the transition).
2. Trigger or wait for the scheduled “yesterday” report job.
3. Open the delivered report and note the labeled date range and included event timestamps.

Expected: Window is yesterday 00:00–24:00 in `America/Los_Angeles`; only events in that local day appear.

Actual: Labeled as yesterday local, but the included hours follow UTC day boundaries (or the reverse mix), so boundary events are missing or from the wrong calendar day.

## Root cause

The scheduler built the time window with UTC day boundaries, then formatted the report label (and sometimes filtered display) with the workspace timezone. Those two clocks disagreed across DST offsets, so the cut and the label described different intervals.

## Fix

Report window computation now resolves the workspace timezone first, then derives start/end instants from that local calendar day (or week). Labels use the same timezone. UTC is used only for storage/serialization of the resulting instants, not for choosing which local day to cover.

## How to verify

```bash
docker compose up api worker
```

1. Set a workspace to `America/Los_Angeles` (or another DST-observing zone).
2. Seed events around a known DST transition night.
3. Run the daily “yesterday” report for the day after the transition.
4. Confirm included timestamps fall strictly within yesterday 00:00–24:00 local, and the label matches that window.
5. Repeat for a UTC workspace: window and label remain UTC calendar days with no shift.
