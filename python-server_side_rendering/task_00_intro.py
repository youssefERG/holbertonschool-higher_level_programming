#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        content = template

        name = attendee.get("name") if attendee.get("name") else "N/A"
        event_title = attendee.get("event_title") if attendee.get("event_title") else "N/A"
        event_date = attendee.get("event_date") if attendee.get("event_date") else "N/A"
        event_location = attendee.get("event_location") if attendee.get("event_location") else "N/A"

        content = content.replace("{name}", str(name))
        content = content.replace("{event_title}", str(event_title))
        content = content.replace("{event_date}", str(event_date))
        content = content.replace("{event_location}", str(event_location))

        filename = "output_{}.txt".format(i)
        with open(filename, "w") as f:
            f.write(content)
