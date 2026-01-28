from collections import Counter

import moving_bug


def run(bug: moving_bug.Bug, nb_trials: int = 1000000):
    """Runs the simulation over multiple trials."""
    final_positions = []

    for _ in range(nb_trials):
        bug.position = 12
        final_position = loop(bug)
        final_positions.append(final_position)

    show_percentages(final_positions, nb_trials)


def loop(bug: moving_bug.Bug) -> int:
    """Simulates one complete trial until the bug visits 12 positions."""
    stepped_positions = [12]

    while len(stepped_positions) < 12:
        new_position = bug.move()
        if new_position not in stepped_positions:
            stepped_positions.append(new_position)

    return stepped_positions[11]


def show_percentages(final_positions: list, nb_trials: int):
    """Displays the statistics of final positions."""
    positions_counter = Counter(final_positions)

    print(f"\n=== Results after {nb_trials} trials ===")
    for i in range(1, 12):
        percentage = positions_counter.get(i, 0) / nb_trials * 100
        print(f"Position {i:2d}: {percentage:6.2f}%")
