from datetime import datetime
from typing import Callable, Any
from flask import url_for
from ... import app


def site_map():
    def has_no_empty_params(rule):
        defaults = rule.defaults if rule.defaults is not None else ()
        arguments = rule.arguments if rule.arguments is not None else ()
        return len(defaults) >= len(arguments)

    links = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))

    return links


@app.template_filter()
def site_map_sort(links: list[tuple[str, Callable]]) -> list[tuple[str, Callable]]:
    return sorted(links, key=lambda x: len(x[0]))


@app.template_filter()
def current_hour(data:Any=None):
    return datetime.now().hour
