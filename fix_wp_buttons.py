"""Compatibility wrapper for older local workflows.

Button/link conversion now lives in build_wp.py so the WordPress theme can be
regenerated from one source of truth.
"""

from build_wp import build_theme


if __name__ == "__main__":
    build_theme()
    print("Regenerated WordPress theme links and assets.")
