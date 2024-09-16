from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Store the uploaded file path and dataframe globally
uploaded_file_path = None
uploaded_df = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global uploaded_file_path, uploaded_df
    
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    
    if file.filename == '':
        return redirect(url_for('index'))

    # Save the file
    uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(uploaded_file_path)

    # Read the file using pandas
    uploaded_df = pd.read_csv(uploaded_file_path)

    # Pass the column names to the template for column selection
    columns = uploaded_df.columns.tolist()
    
    return render_template('choose_columns.html', columns=columns)

@app.route('/view_data', methods=['POST'])
def view_data():
    global uploaded_df

    # Get selected columns from the form
    selected_columns = request.form.getlist('columns')

    # Filter the DataFrame based on selected columns
    if selected_columns:
        filtered_df = uploaded_df[selected_columns]
    else:
        filtered_df = uploaded_df  # Default to show all columns if none selected

    # Convert the filtered DataFrame to HTML for rendering
    table_html = filtered_df.head().to_html(classes='table table-striped')

    return render_template('view_data.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True)
