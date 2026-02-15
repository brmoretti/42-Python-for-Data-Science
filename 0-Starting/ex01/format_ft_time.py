from datetime import datetime

dt_init = datetime(1970, 1, 1)
dt_end = datetime.now()
time_elapsed = (dt_end - dt_init).total_seconds()

print(
    f"Seconds since {datetime.strftime(dt_init, '%B %-d, %Y')}: "
    f"{time_elapsed:,.4f} or {time_elapsed:.2e} in scientific notation"
    "\n"
    f"{datetime.strftime(dt_end, '%b %-d %Y')}"
)
