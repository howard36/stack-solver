from stackapi import StackAPI
from stackapi import StackAPIError

SITE = StackAPI('stackoverflow')
SITE.page_size = 2
SITE.max_pages = 1

# fitler with question_id, title, body_markdown, and can_answer
filter = '!.yIW4AOgyCaf6v4N'

questions = SITE.fetch('questions/no-answers', tagged='python;django', sort='votes', filter=filter)

question_ids = []
for question in questions['items']:
    question_ids.append(question['question_id'])
    print(question['body'])

print(questions)

