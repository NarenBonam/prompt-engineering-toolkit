class PromptTemplate:
    def __init__(self, template: str):
        self.template = template

    def render(self, **kwargs) -> str:
        return self.template.format(**kwargs)

class PromptTemplateLibrary:
    def __init__(self):
        self.templates = {
            'summarize': PromptTemplate('Summarize the following text: {text}'),
            'translate': PromptTemplate('Translate the following text to {language}: {text}'),
            'code_review': PromptTemplate('Review the following code: {code}'),
            'extraction': PromptTemplate('Extract relevant information from the following text: {text}'),
            'qa': PromptTemplate('Answer the question: {question} based on the following context: {context}'),
        }

    def get_template(self, task: str) -> PromptTemplate:
        return self.templates.get(task, None)