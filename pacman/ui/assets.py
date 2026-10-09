"""
Asset & Resource Path Manager.

Responsibility:
- Resolve correct file paths for fonts, sprites, and sounds.
- Ensure compatibility with both standard local runs and PyInstaller frozen bundles
  (handling sys._MEIPASS vs relative directory paths).
- Gracefully provide fallback placeholder drawing routines if an asset file is missing.

Assigned Developer:
- P2
"""
