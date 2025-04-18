from youtube_transcript_api import YouTubeTranscriptApi

video_id = "1zJ7PQ6Nv38"          # 예: https://youtu.be/AbCdEf → "AbCdEf"
txt = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko', 'en'])

with open(f"{video_id}.txt", "w", encoding="utf-8") as f:
    for line in txt:
        f.write(line['text'] + '\n')
