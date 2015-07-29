
def generate_messages_html(messages):

    html = ""

    for i in messages:
        html += '<p>' + i + '</p>'

    return html
