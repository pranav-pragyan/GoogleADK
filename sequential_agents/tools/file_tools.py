from pathlib import Path
from datetime import datetime

def save_html(html_content: str) -> str:
    """
    Save generated HTML to a timestamped file.
    """

    Path("output").mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"generated_{timestamp}.html"

    output_path = Path("output") / filename

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    return f"HTML saved successfully to {output_path}"