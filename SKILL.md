---
name: genpark-content-factory
description: High-volume bulk social media graphic and post generator.
version: 1.0.0
---

# genpark-content-factory

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
