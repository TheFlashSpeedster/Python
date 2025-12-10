with open('file.txt', 'r') as f:
  text = f.read().split()

print('#'.join(text))
