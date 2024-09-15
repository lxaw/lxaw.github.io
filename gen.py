import json
from html import escape

def generate_html(json_file_path, output_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as file:
        papers = json.load(file)

    # Generate the HTML content
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Searchable paper list</title>
    <style>
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
            cursor: pointer;
        }}
        .search-inputs {{
            margin-bottom: 10px;
        }}
        .search-inputs input {{
            margin-right: 10px;
            margin-bottom: 5px;
        }}
    </style>
</head>
<body>
    <h1>Here's where I keep a list of papers I have read.</h1>
    <p>
        This list was curated by <a href="index.html">Lexington Whalen</a>, beginning from his first year of PhD to end. As he is me, I hope he keeps going!
    </p>
    <p>
        I typically use this to organize papers I found interesting. Please feel free to do whatever you want with it. Note that this is not every single paper I have ever read, just a collection of ones that I remember to put down.
    </p>
    <p id="paperCount">
        So far, we have read {len(papers)} papers. Let's keep it up!
    </p> 
    <small id="searchCount">
        Your search returned {len(papers)} papers. Nice! 
    </small>
    
    <div class="search-inputs">
        <input type="text" id="titleSearch" placeholder="Search title...">
        <input type="text" id="authorSearch" placeholder="Search author...">
        <input type="text" id="yearSearch" placeholder="Search year...">
        <input type="text" id="topicSearch" placeholder="Search topic...">
        <input type="text" id="venueSearch" placeholder="Search venue...">
        <input type="text" id="descriptionSearch" placeholder="Search description...">
        <button id="clearSearch">Clear Search</button>
    </div>
    
    <table id="paperTable">
        <thead>
            <tr>
                <th data-sort="title">Title</th>
                <th data-sort="author">Author</th>
                <th data-sort="year">Year</th>
                <th data-sort="topic">Topic</th>
                <th data-sort="venue">Publication Venue</th>
                <th data-sort="description">Description</th>
                <th>Link</th>
            </tr>
        </thead>
        <tbody>
        {generate_table_rows(papers)}
        </tbody>
    </table>

    <script>
        const table = document.getElementById('paperTable');
        const tbody = table.querySelector('tbody');
        const clearButton = document.getElementById('clearSearch');
        const searchInputs = {{
            title: document.getElementById('titleSearch'),
            author: document.getElementById('authorSearch'),
            year: document.getElementById('yearSearch'),
            topic: document.getElementById('topicSearch'),
            venue: document.getElementById('venueSearch'),
            description: document.getElementById('descriptionSearch')
        }};
        const paperCountElement = document.getElementById('paperCount');
        const searchCountElement = document.getElementById('searchCount');
        let sortOrder = {{}};

        function setupEventListeners() {{
            for (let key in searchInputs) {{
                searchInputs[key].addEventListener('keyup', searchTable);
            }}

            clearButton.addEventListener('click', function() {{
                for (let key in searchInputs) {{
                    searchInputs[key].value = '';
                }}
                searchTable();
            }});

            table.querySelector('thead').addEventListener('click', function(e) {{
                const th = e.target.closest('th');
                if (!th) return;
                const column = th.dataset.sort;
                const dataType = column === 'year' ? 'number' : 'string';
                sortOrder[column] = sortOrder[column] === 'asc' ? 'desc' : 'asc';
                sortTable(column, dataType, sortOrder[column]);
            }});
        }}

        function searchTable() {{
            const rows = tbody.getElementsByTagName('tr');
            let numRowsMatch = 0;
            for (let i = 0; i < rows.length; i++) {{
                const row = rows[i];
                const cells = row.getElementsByTagName('td');
                let foundMatch = true;

                for (let key in searchInputs) {{
                    const cellText = cells[Object.keys(searchInputs).indexOf(key)].textContent.toLowerCase();
                    const searchTerm = searchInputs[key].value.toLowerCase();
                    if (searchTerm && !cellText.includes(searchTerm)) {{
                        foundMatch = false;
                        break;
                    }}
                }}

                if(foundMatch) {{
                    row.style.display = '';
                    numRowsMatch++;
                }} else {{
                    row.style.display = 'none';
                }}
            }}
            updateSearchCount(numRowsMatch);
        }}

        function updateSearchCount(count) {{
            searchCountElement.textContent = `Your search returned ${{count}} papers. Nice!`;
        }}

        function sortTable(column, dataType, order) {{
            const rows = Array.from(tbody.querySelectorAll('tr'));
            const columnIndex = Array.from(table.querySelector('thead tr').children).findIndex(th => th.dataset.sort === column);

            rows.sort((a, b) => {{
                let aValue = a.children[columnIndex].textContent;
                let bValue = b.children[columnIndex].textContent;

                if (dataType === 'number') {{
                    return order === 'asc' ? Number(aValue) - Number(bValue) : Number(bValue) - Number(aValue);
                }} else {{
                    return order === 'asc' ? aValue.localeCompare(bValue) : bValue.localeCompare(aValue);
                }}
            }});

            tbody.append(...rows);
        }}

        setupEventListeners();
    </script>
</body>
</html>
    """

    # Write the HTML content to a file
    with open(output_file_path, 'w') as file:
        file.write(html_content)

def generate_table_rows(papers):
    rows = []
    for paper in papers:
        row = f"""
            <tr>
                <td>{escape(paper['title'])}</td>
                <td>{escape(paper['author'])}</td>
                <td>{escape(str(paper['year']))}</td>
                <td>{escape(paper['topic'])}</td>
                <td>{escape(paper['venue'])}</td>
                <td>{escape(paper['description'])}</td>
                <td>{'<a href="' + escape(paper['link']) + '" target="_blank">Link</a>' if paper.get('link') else 'N/A'}</td>
            </tr>
        """
        rows.append(row)
    return ''.join(rows)

if __name__ == "__main__":
    json_file_path = "papers/list.json"  # Update this path to your JSON file
    output_file_path = "papers_read.html"  # The output HTML file
    generate_html(json_file_path, output_file_path)
    print(f"HTML file generated successfully: {output_file_path}")