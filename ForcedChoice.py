print((lambda p,s: "\n".join(("KEEP" if any(p==x for x in map(int,input().split()[1:]))else "REMOVE" for _ in range(s))))(*map(int,input().split()[1:])))
