import octoprint.plugin

class EXOSkinPlugin(octoprint.plugin.UiPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.AssetPlugin):

	def get_assets(self):
		return dict(
			js=["js/viewmodel.js"]
		)

	def will_handle_ui(self, request):
		from octoprint.server.util.flask import passive_login

		result = passive_login()
		if hasattr(result, "status_code") and result.status_code == 200:
			# passive login successful, no need to handle that
			return False
		else:
			return True

	def on_ui_render(self, now, request, render_kwargs):
		from flask import render_template, make_response
		return make_response(render_template("EXOSkin_index.jinja2", **render_kwargs))

	def get_ui_custom_tracked_files(self):
		from os.path import join as opj

		paths = [opj("static", "css", "EXOSkin.css"),
		         opj("static", "js", "main.js"),
		         opj("static", "js", "viewmodel.js"),
		         opj("static", "less", "EXOSkin.less"),
		         opj("templates", "parts", "EXOSkin_css.jinja2"),
		         opj("templates", "parts", "EXOSkin_javascripts.jinja2"),
		         opj("templates", "EXOSkin_index.jinja2")]

		return [opj(self._basefolder, path) for path in paths]

	def get_ui_preemptive_caching_enabled(self):
		return False

__plugin_name__ = "EXOSkin"
__plugin_implementation__ = EXOSkinPlugin()
