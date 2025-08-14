from __future__ import annotations

import os
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.resources import resource_add_path


def _load_kv_definitions() -> None:
	"""Load the KV definitions for the Body UI.

	Tries both 'body.kivy' and 'body.kv' in the same directory as this file,
	then falls back to the current working directory. This avoids black screens
	caused by filename mismatches or not actually adding the root widget to the Screen.
	"""
	kv_candidates = ("body.kivy", "body.kv")
	this_dir = os.path.abspath(os.path.dirname(__file__))

	# Ensure images/fonts in this folder are discoverable by Kivy
	resource_add_path(this_dir)

	for candidate in kv_candidates:
		candidate_abs = os.path.join(this_dir, candidate)
		if os.path.exists(candidate_abs):
			Builder.load_file(candidate_abs)
			return

	# Fallback: try CWD
	for candidate in kv_candidates:
		if os.path.exists(candidate):
			Builder.load_file(candidate)
			return

	# If nothing found, warn (Screen will appear empty)
	print("[body] Warning: Could not find 'body.kivy' or 'body.kv'.")


# Load KV once at import time
_load_kv_definitions()

# Optional: set a development window size (has no effect on mobile)
Window.size = (dp(300), dp(500))


class BodyScreen(Screen):
	"""Screen that hosts the 'Body' widget defined in body.kivy.

	Usage (in your ScreenManager setup):
		from body import BodyScreen
		sm.add_widget(BodyScreen())
		# On successful login:
		# self.manager.current = 'body'
	"""

	def __init__(self, **kwargs):
		# Ensure a default, consistent screen name for navigation
		kwargs.setdefault("name", "body")
		super().__init__(**kwargs)

	def on_kv_post(self, base_widget):
		"""Attach the root Body widget once the KV rules are ready.

		We instantiate the 'Body' class (declared in body.kivy) and add it
		as the child of this Screen. This prevents an empty Screen (black view).
		"""
		if not self.children:
			try:
				self.add_widget(Factory.Body())
			except Exception as exc:
				from kivy.logger import Logger
				Logger.exception("[body] Failed to instantiate Body from KV: %s", exc)


# Local demo runner (optional). Run `python body.py` to preview the screen.
if __name__ == "__main__":
	from kivy.app import App
	from kivy.uix.screenmanager import ScreenManager

	class _DemoApp(App):
		def build(self):
			sm = ScreenManager()
			sm.add_widget(BodyScreen())
			return sm

	_DemoApp().run()