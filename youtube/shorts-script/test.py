from youtube_transcript_api import YouTubeTranscriptApi

video_id = "jxo8cEcYa7o"            # 예: https://youtu.be/AbCdE → "AbCdE"
korean_txt = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko'])
with open("transcript.txt", "w", encoding="utf-8") as f:
    for line in korean_txt:
        f.write(f"{line['text']}\n")