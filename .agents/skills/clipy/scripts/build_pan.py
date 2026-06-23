#!/usr/bin/env python3
"""Build ffmpeg crop x-expression with face centering and smooth transitions.

Usage: build_pan.py SEGMENTS.json LEFT_CENTER_X RIGHT_CENTER_X
Stdout: ffmpeg expression suitable for crop=W:H:x='EXPR':y=0
"""
import json, sys, os

segs = json.load(open(sys.argv[1]))
LEFT_CENTER = float(sys.argv[2])  # Face center x-coordinate for left speaker
RIGHT_CENTER = float(sys.argv[3]) # Face center x-coordinate for right speaker

# For 9:16 output from 16:9 source (1920x1080), crop width = 608
# To center a face: x = face_center_x - 304
LEFT_X = LEFT_CENTER - 304
RIGHT_X = RIGHT_CENTER - 304

def x_for(s): return LEFT_X if s == "left" else RIGHT_X

# Add buffering: start 1-3 seconds before segment, end 1-3 seconds after
# This ensures smooth cuts around speech boundaries
buffered_segs = []
for seg in segs:
    start_buffer = max(0.0, seg["start"] - 2.0)  # 2s before (adjustable)
    end_buffer = seg["end"] + 2.0                # 2s after (adjustable)
    buffered_segs.append({
        "start": start_buffer,
        "end": end_buffer,
        "speaker": seg["speaker"]
    })

# Build expression with buffering
expr = str(x_for(buffered_segs[-1]["speaker"]))
for seg in reversed(buffered_segs[:-1]):
    expr = f"if(lt(t\\,{seg['end']:.4f})\\,{x_for(seg['speaker'])}\\,{expr})"
print(expr)
