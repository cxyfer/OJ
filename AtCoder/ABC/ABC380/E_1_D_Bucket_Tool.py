import sys
import bisect

def main():
    import sys
    import threading

    def solve():
        import sys

        sys.setrecursionlimit(1 << 25)
        N, Q = map(int, sys.stdin.readline().split())
        queries = []
        for _ in range(Q):
            parts = sys.stdin.readline().split()
            if parts[0] == '1':
                queries.append(('1', int(parts[1]), int(parts[2])))
            else:
                queries.append(('2', int(parts[1])))

        # Initialize starts and colors
        starts = list(range(1, N + 1))
        colors = list(range(1, N + 1))

        # Initialize color_counts
        color_counts = [0] * (N + 2)
        for c in range(1, N + 1):
            color_counts[c] = 1

        for query in queries:
            if query[0] == '1':
                _, x, c = query
                # Find the interval containing x
                index = bisect.bisect_right(starts, x) - 1
                a = starts[index]
                if index + 1 < len(starts):
                    b = starts[index + 1] - 1
                else:
                    b = N
                old_color = colors[index]
                if old_color != c:
                    # Update color_counts
                    color_counts[old_color] -= (b - a + 1)
                    color_counts[c] += (b - a + 1)
                    # Update the color
                    colors[index] = c
                    # Merge with previous if needed
                    if index > 0 and colors[index -1] == c:
                        # Merge current interval into previous
                        # Remove current start and color
                        starts.pop(index)
                        colors.pop(index)
                        index -=1
                    # Merge with next if needed
                    if index +1 < len(starts) and colors[index +1] == c:
                        # Merge next interval into current
                        starts.pop(index +1)
                        colors.pop(index +1)
            else:
                _, c = query
                print(color_counts[c])

    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()
