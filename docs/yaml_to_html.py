import yaml
from jinja2 import Environment, FileSystemLoader

# Read the YAML file
with open("docs/examples.yaml", "r") as file:
    test_cases = yaml.safe_load(file)

# Group test cases by the 'name' key
test_cases_by_key = dict()
for test_case in test_cases:
    name = test_case["name"]
    if name in test_cases_by_key:
        test_cases_by_key[name].append(test_case)
    else:
        test_cases_by_key[name] = [test_case]

# Create a Jinja2 environment
env = Environment(
    loader=FileSystemLoader(".")
)  # Use the current directory as the template directory

# Load the HTML template
template = env.get_template("docs/assets/template.html")

rendered_html = template.render({"test_cases_by_key": test_cases_by_key})

# Save the combined HTML content to a single file

with open("docs/examples.html", "w") as output_file:
    output_file.write(rendered_html)

print(f"HTML Docs Generated: examples.html")
