from flask import Flask, jsonify, render_template


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',
        variable_end_string='%%',
    ))


app = CustomFlask(
    __name__,
    template_folder="../client",
    static_folder="../client")
