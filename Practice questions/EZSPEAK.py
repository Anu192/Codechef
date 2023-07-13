def is_easy(s):
  const = 0
  for c in s:
    if c not in "aeiou":
      const += 1
    else:
      const = 0
    if const >= 4:
      return False
  return True

def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    s = input()
    print("YES" if is_easy(s) else "NO")

if __name__ == "__main__":
  main()
