def format_time(seconds):
    """Format seconds into a string of the form HH:MM:SS."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"
