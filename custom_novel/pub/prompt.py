from jinja2 import Environment, FileSystemLoader


class PromptTemplate:
    env = Environment(
        loader=FileSystemLoader('templates'),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True
    )

    def get_prompt(
            self,
            template: str,
            **kwargs: dict
    ) -> str:
        return self.env.get_template(template).render(**kwargs)


prompt_template = PromptTemplate()