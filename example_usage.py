# -*- coding: utf-8 -*-
from client import OpenClawGenParkContentFactory

factory = OpenClawGenParkContentFactory()

# 1. Headline Scoring
hl = "7 Breakthrough Secrets That Unlocked Autonomous Agent Workflows"
res_hl = factory.evaluate_headline_impact_score(hl)
print(f"Headline Impact: Score={res_hl['headline_score']} ({res_hl['classification']})")
print(f"  Power words: {res_hl['power_words_detected']}, Curiosity: {res_hl['curiosity_triggers_detected']}")

# 2. Prose Rhythm Cadence
article = """
Autonomous AI is here. It changes everything about software development.
Developers who adapt quickly will experience extraordinary productivity gains, while those who resist will inevitably fall behind.
Build fast. Deploy often.
"""
cadence = factory.analyze_prose_rhythm_cadence(article)
print()
print(f"Cadence Analysis: StdDev={cadence['sentence_length_std_dev']} words ({cadence['pacing_classification']})")
print(f"  Sentence lengths: {cadence['sentence_lengths']}")

# 3. Retention Modeling
ret = factory.predict_hook_retention_curve(video_length_seconds=45, hook_strength_score=88.0, topic_pacing_wpm=165.0)
print()
print(f"Retention Curve: 3s Hook={ret['initial_3s_hook_retention_pct']}%, Completion={ret['completion_rate_pct']}% (Avg: {ret['average_watch_time_pct']}%)")
