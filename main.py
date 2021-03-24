import sys

from package_name import app

print('Running package_name!')
app.run_server(
    debug=False,
    # FYI: hot reload doesn't work on frozen imports!
    dev_tools_hot_reload=not getattr(sys, 'frozen', False),
)
