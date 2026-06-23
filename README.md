# Clipy

A powerful AI video repurposing engine that turns long videos into social-ready viral clips. It merges the multi-pass detection workflow of OpusClip with the fast local rendering pipeline of Clipify.

Point it at any video file or URL and it will:

1. **Find clip-worthy segments** — transcribes the video with [Whisper](https://github.com/openai/whisper) and scans the transcript across 9 different detection passes (funny moments, soundbites, hot-takes, tutorials, etc) and assigns a **Virality Score**.
2. **Create customized clips** — trims your chosen moments and reframes 16:9 → 9:16 with hard-cut pans that follow whoever is speaking (or split-screen if you'd rather see both faces).
3. **Add subtitles** — burns word-by-word captions in multiple selectable styles (opus, karaoke, minimal, none) or lets you match your own reference styles.

### 🌟 Ultimate Features (Phase 2)
The AI agent using this skill can explicitly ask you if you want to deploy the following heavy-hitter editing techniques locally:
- 🖼️ **Thumbnail Maker**: Automatically extracts the peak emotional frame, boosts contrast, and applies catchy Youtube/Reels overlaid text.
- 🎵 **Auto-BGM & Ducking**: Downloads and overlays trending/lo-fi tracks and applies `ffmpeg` audio ducking to lower the beat automatically when the subject speaks.
- 🎥 **AI Cameraman**: Detects punchlines and applies aggressive `zoompan` or Ken-Burns effects dynamically.
- 🔕 **Smart Auto-Censorship**: Maps profanity via Whisper, bleeps it out, and applies a localized face blur for brand safety.
- 📌 **Social Retention**: Add exact-duration TikTok progress bars, custom logo watermarks, and B-Roll overlays implicitly tied to keywords.
- 📝 **Metadata Extractions**: Spits out `metadata.txt` with SEO hashtags and TikTok clickbait captions.

No cloud APIs. Runs entirely on your machine. No OpenCV. 

## Requirements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (for downloading from URLs)
- `ffmpeg` with `libx264`
- [`whisper`](https://github.com/openai/whisper) (`pip install openai-whisper`)
- Python 3 with `numpy` (`pip install numpy`)

## Usage

When using an AI agent equipped with this skill, just provide a video URL or a local file:

1. The agent will transcribe and propose a scored list of viral candidates
2. You confirm which ones to cut
3. The agent will ask you a series of deep customization questions (Frame size, Caption Style, Font, Colors, Branding, etc.)
4. The agent renders the result locally to `<source-video-dir>/clipify_out/`

## How the face-pan works

No face detection model. Camera is static within a single clip, so:
1. Eyeball each face's mouth+chin area as a rectangle on one sample frame.
2. `ffmpeg` computes per-frame motion energy in each rectangle using frame differencing.
3. Whichever rectangle has more motion at a given moment = that's the speaker.
4. Build a hard-cut x-coordinate expression from the speaker timeline.
5. Crop a vertical strip from the source that follows whoever's talking.

## Repo structure

```
clipy/
├── .agents/skills/clipy/
│   ├── SKILL.md           # the skill prompt 
│   ├── scripts/
│   │   ├── analyze.py     # speaker timeline from two ROI motion files
│   │   ├── build_pan.py   # ffmpeg crop x-expression with hard cuts
│   │   ├── build_ass.py   # opus/karaoke/minimal ASS captions from whisper JSON
│   │   └── audio_align.py # find offset of a sub-clip in a longer source
├── .gitignore
├── LICENSE
└── README.md
```

## License

MIT — see [LICENSE](LICENSE).

Built by Abderrazzak Karoui.
