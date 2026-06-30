# 🍕 SliceMatic — PizzaFlow Ordering System

**FDE Project · Group 10**  
A cart-based pizza ordering system built with Python and Gradio.  
Customers build a multi-pizza cart, choose bases and toppings, review a live bill, then confirm payment.

---

## Project Structure

```
slice-matic/
├── main.py                        # Entry point — run this
├── pyproject.toml                 # uv project config & dependencies
├── config/
│   └── settings.py                # All constants, paths, pricing rules, branding
├── core/
│   └── pizzaflow_core.py          # Business logic (validation, pricing, persistence)
├── ui/
│   └── app.py                     # Gradio UI (5-step ordering flow)
├── data/
│   ├── Types_of_Base.txt          # Crust options  (ID;Name;Price)
│   ├── Types_of_Pizza.txt         # Pizza options  (ID;Name;Price)
│   └── Types_of_Toppings.txt      # Topping options (ID;Name;Price)
├── logs/
│   └── orders_log.txt             # Persisted order records (pipe-delimited)
├── scripts/
│   └── generate_sample_log.py    # Seeds logs/ with sample orders
└── tests/
    └── test_core.py               # Plain-Python test suite (no Gradio needed)
```

---

## Prerequisites

| Tool | Version |
|------|---------|
| [uv](https://docs.astral.sh/uv/getting-started/installation/) | ≥ 0.5 |
| Python | ≥ 3.11 (uv manages this automatically) |

> **Install uv** (if not already installed):
> ```powershell
> # Windows (PowerShell)
> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
> ```
> ```bash
> # macOS / Linux
> curl -LsSf https://astral.sh/uv/install.sh | sh
> ```

---

## Setup

Clone the repo and install dependencies in one step:

```bash
git clone <repo-url>
cd slice-matic
uv sync
```

`uv sync` does the following automatically:
- Reads `.python-version` (pinned to **3.13**) and uses that interpreter
- Creates a `.venv/` virtual environment
- Installs all dependencies from `uv.lock` (exact, reproducible versions)

No manual `pip install` or `python -m venv` needed.

---

## Running the App

```bash
uv run python main.py
```

Gradio will print a local URL — open it in your browser:

```
Running on local URL:  http://127.0.0.1:7860
```

The 5-step ordering flow:
1. **Your Details** — name and 10-digit mobile number
2. **Build Your Order** — pick pizzas, bases, quantities, and toppings
3. **Review Bill** — itemised breakdown with GST and discount
4. **Payment** — Cash, Card, or UPI
5. **Confirmation** — order saved to `logs/orders_log.txt`

---

## Running Tests

```bash
uv run python tests/test_core.py
```

Runs 65 tests covering all 8 edge cases, cart pricing, menu loading,
and order persistence — no Gradio involved.

---

## Generating Sample Log Data

To seed `logs/orders_log.txt` with three representative sample orders:

```bash
uv run python scripts/generate_sample_log.py
```

> ⚠️ This **overwrites** the existing log file.

---

## Business Rules (quick reference)

| Rule | Value |
|------|-------|
| Name | Letters + spaces only, 2–40 chars |
| Phone | 10 digits, must start with 6/7/8/9 |
| Quantity per pizza | 0–10 (0 = skip) |
| Total pizzas per order | 1–10 |
| Toppings per pizza | 0–5× per topping type |
| Discount | 10% off subtotal when ≥ 5 pizzas |
| GST | 18% on post-discount amount |

---

## Menu Files

Menu files live in `data/` and use the format `ID;Name;Price` (one item per line).  
Swap them out freely — the app reloads them at startup with no code changes needed.

---

## Configuration

All magic variables (pricing rates, quantity limits, file paths, UI colours) are in  
[`config/settings.py`](config/settings.py). Edit that file to change any business rule.

---

## Dependency Management

```bash
# Install / sync dependencies
uv sync

# Add a new dependency
uv add <package>

# Add a dev-only dependency
uv add --dev <package>

# Run any command inside the project's venv
uv run <command>
```
