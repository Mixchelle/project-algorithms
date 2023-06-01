def count_study(persistence_period, target_time):
    count = 0
    for period in persistence_period:
        start_time, end_time = period
        if start_time <= target_time <= end_time:
            count += 1
    return count


def is_valid_entry(entry):
    if len(entry) != 2:
        return False
    start_time, end_time = entry
    if not isinstance(start_time, int) or not isinstance(end_time, int):
        return False
    if start_time > end_time:
        return False
    return True


def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if not isinstance(target_time, int):
        return None

    if not all(is_valid_entry(entry) for entry in permanence_period):
        return None
    return count_study(permanence_period, target_time)
