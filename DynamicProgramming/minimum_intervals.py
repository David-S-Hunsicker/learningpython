def videoStitching(clips, times: int) -> int:
    clips.sort()
    clips_needed = [101] * (time + 1)
    clips_needed[0] = 0
    for start_time, end_time in clips:
        end_time = min(time, end_time)
        for i in range(start_time, end_time + 1):
            clips_needed[i] = min(clips_needed[i], clips_needed[start_time] + 1)
    return clips_needed[-1] if clips_needed[-1] != 101 else -1


clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
time = 10
print(videoStitching(clips, time))
