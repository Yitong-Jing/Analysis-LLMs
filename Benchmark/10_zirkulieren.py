# LLM antwortet zehnmal in einer Schleife und führt jedes Mal ein Benchmarking durch
import subprocess

for i in range(10):
    subprocess.call(["python", "rechnen_Benchmarks.py"])
