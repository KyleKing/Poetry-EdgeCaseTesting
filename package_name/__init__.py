import importlib.metadata
import flask_compress
import pkg_resources
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

print(importlib.metadata.version('flask-compress'))
print(pkg_resources.get_distribution('flask-compress').version)

app = dash.Dash(__name__)

ALLOWED_TYPES = (
    "text", "number", "password", "email", "search",
    "tel", "url", "range", "hidden",
)


app.layout = html.Div(
    [
        dcc.Input(
            id="input_{}".format(_),
            type=_,
            placeholder="input type {}".format(_),
        )
        for _ in ALLOWED_TYPES
    ]
    + [html.Div(id="out-all-types")]
)


@app.callback(
    Output("out-all-types", "children"),
    [Input("input_{}".format(_), "value") for _ in ALLOWED_TYPES],
)
def cb_render(*vals):
    return " | ".join((str(val) for val in vals if val))


if __name__ == "__main__":
    app.run_server(debug=True)
