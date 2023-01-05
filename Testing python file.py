import datetime as dt
here_now = dt.datetime.now()
utc_now = dt.datetime.utcnow()
time_difference = (utc_now - here_now)

print(f"My time : {here_now:%I:%M%p}")
print(f"Utc time : {utc_now:%I:%M%p}")
print(f"Difference  : {time_difference}")