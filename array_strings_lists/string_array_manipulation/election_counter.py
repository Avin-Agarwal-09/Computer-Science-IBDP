def election_counter(votes):
    counts = {}
    for name in votes:
        name_lower = name.lower()
        counts[name_lower] = counts.get(name_lower,0) + 1
    max_votes = max(counts.values())
    for name, count in counts.items():
        if count == max_votes:
            winner = name
    return counts, winner

votes = ["alice","Alice","ALICE","alice", "bob", "BOB" , "Charlie", "duck", "DUCK","duck"]
print(election_counter(votes))