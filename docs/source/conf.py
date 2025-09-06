project = "Docs for NYU CREO"
extensions = ["myst_parser"]
templates_path = ["_templates"]
exclude_patterns = ["_build"]
html_css_files = ['custom.css'] 
html_theme = "alabaster"
html_sidebars = {
    "**": ["searchbox.html", "globaltoc.html"],  # use global TOC, not per-page navigation
}
html_theme_options = {
    "fixed_sidebar": True,        # keep sidebar position fixed
    "globaltoc_collapse": False,  # show full tree, don’t collapse sections
    "globaltoc_maxdepth": 1,      # depth of the tree you want visible
}
myst_enable_extensions = ["attrs_inline"]
