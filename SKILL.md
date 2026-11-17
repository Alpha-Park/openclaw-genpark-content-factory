---
name: genpark-content-factory
description: High-volume bulk social media graphic and post generator.
version: 1.0.0
---

# genpark-content-factory

## MCP runtime requirements

The standard-library-only policy applies to direct `client.py` use. Running `mcp_server.py` requires Python 3.10+ and the official `mcp` SDK (`mcp>=1.0.0,<2`) from `requirements.txt`. Install it into your chosen environment from the repository checkout:

```bash
python -m pip install -r requirements.txt
```

Configure the MCP client with that environment's absolute Python executable path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; a GitHub URL is not a remote MCP endpoint.

## Overview
This skill operates as an autonomous content agency. It monitors niche trends on platforms like X (Twitter) and Reddit, identifies high-engagement formats, and bulk-generates a full month's worth of multi-platform content (text, carousels, video scripts) scheduled for automatic posting. 

## Core Capabilities
- **Trend Ingestion**: Scrape niche-specific subreddits or trending hashtags to discover viral concepts.
- **Bulk Content Creation**: Convert one core idea into an X thread, a LinkedIn post, an Instagram Carousel outline, and a TikTok short script.
- **Scheduling**: Integrate with tools like Buffer or natively schedule via platform APIs to ensure a constant stream of posts.

## Usage Guide
When a user asks to generate a content strategy:
1. Ask for their specific niche (e.g., "AI SaaS", "Fitness Coaching").
2. Retrieve the top 5 trending discussions in that niche from the past week.
3. Automatically generate 30 unique, hook-driven social media posts designed for organic reach.
4. Output the results in a structured format (CSV or JSON) ready for bulk scheduling upload.
