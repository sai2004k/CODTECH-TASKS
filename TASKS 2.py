import pandas as pd
from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Load Data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# Analyze Data
def analyze_data(data):
    summary = {
        'Total Students': len(data),
        'Average Score': data['Score'].mean(),
        'Highest Score': data['Score'].max(),
        'Lowest Score': data['Score'].min()
    }
    return summary

# Generate PDF Report
def generate_pdf(data, summary, output_file):
    # Set up PDF document
    doc = SimpleDocTemplate(output_file, pagesize=LETTER)
    elements = []
    styles = getSampleStyleSheet()
    
    # Title
    title = Paragraph("Automated Report", styles['Title'])
    elements.append(title)
    
    # Summary
    summary_text = f"""
    <br/><br/>
    <b>Summary:</b><br/>
    Total Students: {summary['Total Students']}<br/>
    Average Score: {summary['Average Score']:.2f}<br/>
    Highest Score: {summary['Highest Score']}<br/>
    Lowest Score: {summary['Lowest Score']}<br/>
    <br/><br/>
    """
    summary_paragraph = Paragraph(summary_text, styles['BodyText'])
    elements.append(summary_paragraph)
    
    # Data Table
    table_data = [list(data.columns)] + data.values.tolist()
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(table)
    
    # Build PDF
    doc.build(elements)
    print(f"Report generated: {output_file}")

# Main Function
if _name_ == "_main_":
    file_path = "data.csv"
    output_file = "report.pdf"
    
    # Step 1: Load Data
    data = load_data(file_path)
    if data is None:
        exit()
    
    # Step 2: Analyze Data
    summary = analyze_data(data)
    
    # Step 3: Generate PDF Report
    generate_pdf(data, summary, output_file)