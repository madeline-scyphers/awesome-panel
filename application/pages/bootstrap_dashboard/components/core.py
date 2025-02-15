# """Core Components for the Bootstrap Dashboard App"""
# import inspect

# import holoviews as hv
# import hvplot.pandas  # pylint: disable=unused-import
# import plotly.express as px  # pylint: disable=wrong-import-order

# import awesome_panel.express as pnx
# import panel as pn
# pn.extension()

# # See also
# # https://holoext.readthedocs.io/en/latest/examples/modifying_toolbar_tools.html#Hide-toolbar
# def disable_logo(plot, element):  # pylint: disable=unused-argument
#     """Hides holoviews logo"""
#     plot.state.toolbar.logo = None


# hv.plotting.bokeh.ElementPlot.finalize_hooks.append(disable_logo)  # pylint: disable=no-member


# def holoviews_chart():
#     """## Dashboard Orders Chart generated by HoloViews"""
#     data = services.get_chart_data()
#     line_plot = data.hvplot.line(
#         x="Day", y="Orders", width=None, height=500, line_color="#007BFF", line_width=6,
#     )
#     scatter_plot = data.hvplot.scatter(x="Day", y="Orders", height=300).opts(
#         marker="o", size=10, color="#007BFF"
#     )
#     fig = line_plot * scatter_plot
#     gridstyle = {"grid_line_color": "black", "grid_line_width": 0.1}
#     fig = fig.opts(
#         responsive=True,
#         toolbar=None,
#         yticks=list(range(12000, 26000, 2000)),
#         ylim=(12000, 26000),
#         gridstyle=gridstyle,
#         show_grid=True,
#     )
#     return fig


# def holoviews_view() -> pn.Column:
#     """## Dashboard Orders Chart View based on HoloViews"""
#     fig = holoviews_chart()
#     text = """
# The [HoloViews](http://holoviews.org/) and [hvplot](https://hvplot.pyviz.org/) I had not used
# before. Their APIs are different than what I'm used to be also seems powerful.

# I'm used to Plotly but it does not work well in Panel yet.
# """
#     return pn.Column(
#         pnx.Header("Holoviews"),
#         fig,
#         pn.pane.Markdown(text),
#         pnx.Code(inspect.getsource(holoviews_chart)),
#         name="Holoviews",
#         sizing_mode="stretch_both",
#     )


# def plotly_chart():
#     """## Dashboard Orders Chart generated by Plotly"""
#     fig = px.line(services.get_chart_data(), x="Day", y="Orders")
#     fig.update_traces(mode="lines+markers", marker=dict(size=10), line=dict(width=4))
#     fig.layout.paper_bgcolor = "rgba(0,0,0,0)"
#     fig.layout.plot_bgcolor = "rgba(0,0,0,0)"
#     fig.layout.width = 1000
#     # fig.layout.autosize = True
#     return fig


# def plotly_view(*args, **kwargs) -> pn.Column:
#     """## Dashboard Orders Chart View based on Plotly"""
#     fig = plotly_chart()
#     return pn.Column(
#         pnx.Header("Plotly"),
#         pn.Row(pn.layout.HSpacer(), pn.pane.Plotly(fig), pn.layout.HSpacer(),),
#         pnx.InfoAlert("Plotly cannot currently auto size to full width and be responsive"),
#         pnx.Code(code=inspect.getsource(plotly_chart)),
#         sizing_mode="stretch_width",
#         name="Plotly",
#         *args,
#         **kwargs,
#     )


# def dataframe_view(*args, **kwargs) -> pn.Column:
#     """## Dashboard Orders Table View"""
#     table = pn.widgets.DataFrame(services.get_table_data(), sizing_mode="stretch_width")
#     text = """I did not use the
#     [DataFrame widget](https://panel.pyviz.org/reference/widgets/DataFrame.html#gallery-dataframe)
#     in the dashboard because it would not look like the GetBootstrap example.
#     But I would always use this power full DataFrame widget in practice
#     because it's so powerful and nice. It's based on [SlickGrid](https://slickgrid.net/).
#     """
#     return pn.Column(
#         pnx.InfoAlert(text),
#         pn.layout.HSpacer(height=20),  # Hack
#         table,
#         sizing_mode="stretch_width",
#         name="DataFrame",
#         *args,
#         **kwargs,
#     )


# if __name__.startswith("bokeh"):
#     # holoviews_view().servable()
#     plotly_view().servable()
