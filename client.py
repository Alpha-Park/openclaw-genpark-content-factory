# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Content Factory Client
Pure Python Standard Library (Zero External Dependencies)
Implements headline emotional impact scoring, prose rhythm variance (syllable standard deviation),
and video engagement hook retention modeling.
"""

import math
import re
from typing import Dict, Any, List, Optional

class OpenClawGenParkContentFactory:
    """
    Automated editorial and virality mechanics engine for content generation agents.
    """

    def __init__(self):
        self.power_words = {
            "breakthrough", "secret", "proven", "exponential", "insane",
            "autonomous", "mastery", "unlocked", "revolution", "elite",
            "ultimate", "guaranteed", "flawless", "effortless", "critical"
        }
        self.curiosity_triggers = {
            "why", "how", "this", "stop", "never", "before", "truth", "revealed", "warning"
        }

    def evaluate_headline_impact_score(self, headline: str) -> Dict[str, Any]:
        """
        Evaluates headline virality posture based on word count balance, power word density,
        and curiosity trigger activation.
        
        Score components:
          - Optimal Length (6 to 12 words): up to 30 pts
          - Power Words: 15 pts each (up to 30 pts)
          - Curiosity Triggers: 15 pts each (up to 30 pts)
          - Numerical/Digit Hook: 10 pts bonus
        """
        clean_headline = headline.strip()
        words = [w.strip(" .,!?:;()[]{}") for w in clean_headline.lower().split() if w.strip(" .,!?:;()[]{}")]
        word_count = len(words)

        if word_count == 0:
            return {"headline": headline, "headline_score": 0.0, "classification": "EMPTY"}

        # 1. Length scoring
        if 6 <= word_count <= 12:
            length_score = 30.0
        elif 4 <= word_count <= 15:
            length_score = 20.0
        else:
            length_score = 10.0

        # 2. Power words
        found_power = [w for w in words if w in self.power_words]
        power_score = min(30.0, len(found_power) * 15.0)

        # 3. Curiosity triggers
        found_curiosity = [w for w in words if w in self.curiosity_triggers]
        curiosity_score = min(30.0, len(found_curiosity) * 15.0)

        # 4. Numerical Hook
        has_digit = any(char.isdigit() for char in clean_headline)
        digit_score = 10.0 if has_digit else 0.0

        total_score = min(100.0, length_score + power_score + curiosity_score + digit_score)

        if total_score >= 80:
            classification = "HIGH_CONVERTING_VIRAL"
        elif total_score >= 60:
            classification = "MODERATE_ENGAGEMENT"
        else:
            classification = "WEAK_LOW_CTR"

        return {
            "headline": headline,
            "word_count": word_count,
            "headline_score": round(total_score, 1),
            "classification": classification,
            "has_numerical_hook": has_digit,
            "power_words_detected": found_power,
            "curiosity_triggers_detected": found_curiosity
        }

    def analyze_prose_rhythm_cadence(self, text: str) -> Dict[str, Any]:
        """
        Analyzes prose cadence and dynamic pacing through sentence length standard deviation:
          sigma = sqrt( sum((len - mean)^2) / N )
        Higher variance prevents monotonous robotic cadence and enhances reader retention.
        """
        raw_sentences = text.replace("!", ".").replace("?", ".").split(".")
        sentences = [s.strip() for s in raw_sentences if s.strip()]
        if not sentences:
            return {"sentence_count": 0, "rhythm_classification": "EMPTY"}

        lengths = [len([w.strip(" .,!?:;()[]{}") for w in s.split() if w.strip(" .,!?:;()[]{}")]) for s in sentences]
        n = len(lengths)
        mean_len = sum(lengths) / n

        variance = sum((l - mean_len) ** 2 for l in lengths) / n
        std_dev = math.sqrt(variance)

        # Syllables estimation heuristic
        all_words = re.findall(r"[a-zA-Z]+", text.lower())
        vowel_count = sum(len(re.findall(r"[aeiouy]+", w)) for w in all_words)
        syllables_per_word = round(vowel_count / max(1, len(all_words)), 2)

        if std_dev >= 7.0:
            pacing = "EXCELLENT_DYNAMIC_CADENCE"
        elif std_dev >= 4.0:
            pacing = "MODERATE_NATURAL_RHYTHM"
        else:
            pacing = "MONOTONOUS_ROBOTIC_PACING"

        return {
            "sentence_count": n,
            "mean_sentence_length_words": round(mean_len, 2),
            "sentence_length_std_dev": round(std_dev, 2),
            "syllables_per_word": syllables_per_word,
            "pacing_classification": pacing,
            "sentence_lengths": lengths
        }

    def predict_hook_retention_curve(
        self,
        video_length_seconds: int = 60,
        hook_strength_score: float = 85.0,
        topic_pacing_wpm: float = 160.0
    ) -> Dict[str, Any]:
        """
        Forecasts viewer retention curve along short-form video timelines using an exponential decay model:
          R(t) = R_0 * exp(-lambda * t)
        """
        # Pacing multiplier (optimal between 150-180 wpm)
        pacing_penalty = max(0.0, abs(topic_pacing_wpm - 165.0) / 100.0)
        
        # Base retention at t=3s
        r_3s = min(95.0, max(40.0, hook_strength_score * 0.95 - (pacing_penalty * 10.0)))
        
        # Decay lambda
        decay_lambda = 0.025 + (100.0 - hook_strength_score) * 0.0004 + (pacing_penalty * 0.01)

        retention_timeline = []
        checkpoints = [1, 3, 5, 10, 15, 30, 45, video_length_seconds]
        checkpoints = sorted(list(set([t for t in checkpoints if t <= video_length_seconds])))

        for t in checkpoints:
            ret = r_3s * math.exp(-decay_lambda * max(0, t - 3))
            retention_timeline.append({
                "timestamp_seconds": t,
                "projected_retention_pct": round(min(100.0, max(5.0, ret)), 1)
            })

        avg_retention = round(sum(p["projected_retention_pct"] for p in retention_timeline) / len(retention_timeline), 1)

        return {
            "video_duration_seconds": video_length_seconds,
            "initial_3s_hook_retention_pct": round(r_3s, 1),
            "completion_rate_pct": retention_timeline[-1]["projected_retention_pct"],
            "average_watch_time_pct": avg_retention,
            "retention_curve": retention_timeline
        }
