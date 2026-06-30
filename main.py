"""
main.py
-------
Entry point for the SliceMatic / PizzaFlow ordering system.

Run with:
    uv run python main.py

Gradio will print the local URL (usually http://127.0.0.1:7860).
"""

from ui.app import demo, LAUNCH_KWARGS


def main():
    demo.launch(share=True, **LAUNCH_KWARGS)


if __name__ == "__main__":
    main()
