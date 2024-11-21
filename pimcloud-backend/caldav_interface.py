import sys
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
import os
import caldav

sys.path.insert(0, "..")
sys.path.insert(0, ".")

load_dotenv()

caldav_url = os.getenv("CALDAV_URL")
username = os.getenv("CALDAV_USERNAME")
password = os.getenv("CALDAV_PASSWORD")

def connect_caldav_server(caldev_url: str, username: str, password: str):
    try:
        with caldav.DAVClient(
            url=caldav_url,
            username=username,
            password=password,
        ) as client:
            return client
    except caldav.error.AuthorizationError as e:
        raise ValueError("Invalid credentials or unauthorized access.") from e
    except caldav.error.DAVError as e:
        raise RuntimeError("Failed to interact with the CalDAV server.") from e
    except Exception as e:
        raise RuntimeError("An unexpected error occurred.") from e

def fetch_calendar_list(client):
    principal = client.principal()
    return principal.calendars()

#fetches tasks from a certain [url] calendar
def fetch_calendar_tasks(client, url, inclCompleted):
    calendar = client.calendar(url=url)
    tasks = []
    if inclCompleted:
      tasks = calendar.todos(include_completed=True)
    else: 
      tasks = calendar.todos()
    return tasks

def mark_task_done(task):
    try:
        task.complete()
        task.save()
    except Exception as e:
        raise RuntimeError("Failed to mark the task as completed.") from e

def task_to_dict(task):
    summary = task.icalendar_component.get("SUMMARY")
    due = task.icalendar_component.get("DUE")
    uid = task.icalendar_component.get("UID")
    #status = "Completed" if task.is_completed else "Pending"
    task_status = task.icalendar_component.get("COMPLETED") 
    completed = False
    if(task_status is not None):
      completed = True

    return {
        "uid": uid,
        "summary": summary,
        "due": due and due.dt.isoformat() if due else None,
        "completed": completed 
    }

client = connect_caldav_server(caldav_url, username, password)

cals = fetch_calendar_list(client)

#for c in cals:
#  print(c.url)

tasks = fetch_calendar_tasks(client, cals[2].url, 0)

for t in tasks:
  print(task_to_dict(t))

uid = tasks[0].icalendar_component.get("UID")

#mark_task_done(tasks[0])

#mark task done from uid

t = cals[2].event_by_uid(uid)
print(t.data)