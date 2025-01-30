from graphviz import Digraph

def create_mindmap_from_summary(summary, output_file="mindmap"):
    """
    Generates a mindmap using Graphviz and saves it as a PDF and PNG.
    :param summary: The summarized text to structure the mindmap.
    :param output_file: File path to save the mindmap.
    """
    lines = summary.split(". ")
    dot = Digraph()

    root = "Mindmap"
    dot.node(root)

    for i, line in enumerate(lines):
        if line.strip():
            node = f"Node_{i+1}"
            dot.node(node, line)
            dot.edge(root, node)

    dot.render(output_file, format="png", cleanup=True)
