with open("pipes.txt", "r", encoding="utf-8") as f:
    content = f.read()
parts = content.split("\n\n")
pipe_lines = parts[0].strip().splitlines()
sel = parts[1].strip().split() if len(parts) > 1 else []
times = [float(x.strip()) for x in pipe_lines if x.strip()]
indices = [int(x) for x in sel if x.strip()]
rate_sum = sum(1 / times[i - 1] for i in indices)
minutes = 60 / rate_sum
with open("time.txt", "w", encoding="utf-8") as f:
    f.write(str(minutes))