# Visual Companion Guide

Browser-based visual brainstorming companion for showing mockups, diagrams, and options.

## When to Use

Decide per-question, not per-session. Would the user understand this better by seeing it than reading it?

**Use the browser** for visual content: UI mockups, architecture diagrams, side-by-side comparisons, design polish, spatial relationships.

**Use the terminal** for text content: requirements, conceptual choices, tradeoff lists, technical decisions, clarifying questions.

## How It Works

The server watches a directory for HTML files and serves the newest one to the browser. Write HTML content to `screen_dir`, the user sees it in their browser and can click to select options.

**Content fragments vs full documents:** If your HTML starts with `<!DOCTYPE` or `<html`, served as-is. Otherwise auto-wrapped in frame template.

## Starting a Session

```bash
scripts/start-server.sh --project-dir /path/to/project --open
```

Save `screen_dir` and `state_dir` from the response.

## The Loop

1. Check server is alive, write HTML to new file in `screen_dir`
2. Tell user what to expect, share URL
3. On next turn, read `$STATE_DIR/events` for browser interactions
4. Iterate or advance
5. Unload with waiting screen when switching to terminal

## CSS Classes Available

.options, .option, .cards, .card, .mockup, .split, .pros-cons, .placeholder, .mock-nav, .mock-sidebar, .mock-content, .mock-button, .mock-input

## Design Tips

- Scale fidelity to the question
- 2-4 options max per screen
- Use real content when it matters
- Keep mockups simple, focus on layout

## File Naming

Use semantic names, never reuse filenames. Server serves newest file by modification time.

## Cleaning Up

```bash
scripts/stop-server.sh $SESSION_DIR
```