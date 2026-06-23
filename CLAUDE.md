# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 🔧 Common Commands
1. **Download videos**: Use `yt-dlp` to fetch content (e.g., `yt-dlp -f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]/best" -o "./episode/source.%(ext)s" <URL>`)
2. **Extract audio**: `ffmpeg -i "source.mp4" -vn -ac 1 -ar 16000 audio.wav`
3. **Transcribe audio**: `whisper audio.wav --model tiny.en --word_timestamps True --output_format json`
4. **Clip processing**: Use scripts in `.agents/skills/clipy/scripts/`:
   - `analyze.py`: Build speaker timelines
   - `build_pan.py`: Generate pan expressions for reframing
   - `build_ass.py`: Create subtitles
   - `audio_align.py`: Align clipped audio to source
5. **Render clips**: General workflow requires:
   - Trimming with `ffmpeg -ss START -t DURATION`
   - Reframing with `crop`/`scale` filters
   - Captions via ASS files
   - Final output to `./clipy_out/`

## 🧠 Architecture Overview
1. **Input Processing**:
   - Accepts URLs (via yt-dlp) or local files/transcripts
   - Generates timestamped transcripts using Whisper

2. **Clip Detection**:
   - Multi-pass analysis for 9 clip types (hooks, soundbites, tutorials, etc.)
   - Virality scoring algorithm (0-100) with 4 metrics: Hook, Flow, Value, Trend

3. **Customization**:
   - User selects output format (9:16/16:9/1:1)
   - Chooses caption styles (opus/karaoke/minimal)
   - Applies advanced features (music ducking, smart zooms)

4. **Output Generation**:
   - Trims clips with frame-accurate cuts
   - Adds subtitles or overrides burned-in ones
   - Generates metadata/thumbnails
   - Delivers final clips in `./clipy_out/`

## 📏 Key Rules
1. **Clip Length**: 15-60s minimum (180s max for tutorials)
2. **Boundary Rules**:
   - Never cut mid-thought
   - Add 1-3s breathing room around cuts
   - Always extend to complete sentence
3. **Reframing**:
   - Center-crop for single speaker
   -speaker
   - Pan-between-faces for multiple speakers
   - Strict vertical centering in 9:16 output
4. **Quality Checks**:
   - Re-run transcription on trimmed clips
   - Verify all output files exist before delivery

## 📄 Licensing
MIT License - see [LICENSE](LICENSE) file

Built by Abderrazzak Karoui.