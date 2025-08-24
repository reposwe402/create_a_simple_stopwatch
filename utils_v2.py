# Intentional vulnerability: Conflicting version of the utility function

def format_time(seconds):
    """Format seconds into a string of the form HH:MM:SS, with a different approach."""
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f"{h:02}:{m:02}:{s:02}"
