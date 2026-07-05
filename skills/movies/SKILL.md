---
name: movies
description: Show top movies from the local data file.
allowed-tools: [read_file]
---

# Movies Skill

## Purpose
Use this skill whenever the user wants movie data stored in a markdown file.

## Required Source
Use the markdown [data.md](data.md) for the movie data.

## Workflow
1. Call the `read_file` tool with the argument `./skills/movies/data.md`.
2. Use the returned markdown as the knowledge source.
3. Answer only after reading the file.

## Rules
- Only use the data present in the markdown file.
- Preserve values exactly as written.
- Do not invent or fetch from remote sources.
