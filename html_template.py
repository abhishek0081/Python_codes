import csv

def export_csv_to_html(input_file, output_file):
    """Exports CSV data to an HTML table."""
    try:
        with open(input_file, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

            if not data:
                print(f"No data found in {input_file}.")
                return

            html_table = "<html>\n<head>\n<title>Utilization Report</title>\n</head>\n<body>\n"
            html_table += "<h1>Utilization Report</h1>\n<table border=\"1\">\n<tr>"

            for key in data[0].keys():
                html_table += f"<th>{key}</th>"

            html_table += "</tr>\n"

            for row in data:
                html_table += "<tr>"
                for value in row.values():
                    html_table += f"<td>{value}</td>"
                html_table += "</tr>\n"

            html_table += "</table>\n</body>\n</html>"

            with open(output_file, mode="w") as html_file:
                html_file.write(html_table)

            print(f"HTML report exported to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    csv_input_file = "utilization_report.csv"
    html_output_file = "utilization_report.html"

    export_csv_to_html(csv_input_file, html_output_file)