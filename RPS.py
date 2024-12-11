def player(prev_play, opponent_history=[]):
    # Counter move mapping
    counter_moves = {"R": "P", "P": "S", "S": "R"}

    # Track opponent's history
    if prev_play != "":
        opponent_history.append(prev_play)

    # If no history, play "R" as a default starting move
    if not opponent_history:
        return "R"

    # Strategy 1: Counter the most frequent move
    from collections import Counter

    move_counts = Counter(opponent_history)
    most_common_move = max(move_counts, key=move_counts.get)
    return counter_moves[most_common_move]
