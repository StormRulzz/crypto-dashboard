"""Generate a daily conspiracy-theory YouTube video script and email it as a draft-style message."""

import os
import smtplib
from datetime import date
from email.mime.text import MIMEText

import anthropic

PROMPT = """Write a YouTube video script meant for about 10 minutes of spoken delivery \
(roughly 1300-1500 words). The topic is a conspiracy theory, in the style of \
"Do we really live in the matrix?" Pick a single specific conspiracy theory angle \
(don't just write about "conspiracy theories" generally). Structure it with:
- A strong hook in the first few sentences
- Escalating points / "evidence" framed as food for thought, not as factual claims
- A thought-provoking close that invites the viewer to decide for themselves

Start your response with a single line "TOPIC: <short topic title>" followed by a blank line, \
then the full script."""


def generate_script() -> tuple[str, str]:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[{"role": "user", "content": PROMPT}],
    )
    text = response.content[0].text.strip()
    first_line, _, body = text.partition("\n\n")
    topic = first_line.removeprefix("TOPIC:").strip() if first_line.startswith("TOPIC:") else "Conspiracy Theory"
    return topic, body.strip() or text


def send_email(topic: str, script: str) -> None:
    gmail_address = os.environ["GMAIL_ADDRESS"]
    gmail_app_password = os.environ["GMAIL_APP_PASSWORD"]

    message = MIMEText(script)
    message["Subject"] = f"Daily Video Script - {topic} - {date.today().isoformat()}"
    message["From"] = gmail_address
    message["To"] = gmail_address

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_address, gmail_app_password)
        server.send_message(message)


def main() -> None:
    topic, script = generate_script()
    send_email(topic, script)
    print(f"Sent script for topic: {topic}")


if __name__ == "__main__":
    main()
