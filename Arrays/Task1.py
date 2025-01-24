import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_report_card(student_id, student_name, total_score, avg_score, subject_scores):
    try:
        
        filename = f"report_card_{student_id}.pdf"
        pdf = SimpleDocTemplate(filename, pagesize=letter)
        elements = []
        
        
        styles = getSampleStyleSheet()
        title_style = styles['Heading1']
        text_style = styles['BodyText']
        
        
        title = Paragraph(f"Report Card for {student_name}", title_style)
        elements.append(title)
        
        
        summary_data = [
            ['Student ID', student_id],
            ['Name', student_name],
            ['Total Score', total_score],
            ['Average Score', avg_score]
        ]
        summary_table = Table(summary_data, hAlign='LEFT')
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(summary_table)
        elements.append(Paragraph("<br/>", text_style))
        
        
        subject_scores.insert(0, ['Subject', 'Score'])  
        scores_table = Table(subject_scores, hAlign='LEFT')
        scores_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(scores_table)
        
        
        pdf.build(elements)
        print(f"Report card generated: {filename}")
    except Exception as e:
        print(f"Error generating report card for {student_id}: {e}")


def main():
    try:
        
        excel_file = 'student_scores.xlsx'
        data = pd.read_excel(excel_file)
        
        
        required_columns = {'Student ID', 'Name', 'Subject', 'Score'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Missing required columns: {required_columns - set(data.columns)}")
        
        
        grouped = data.groupby(['Student ID', 'Name'])
        for (student_id, student_name), group in grouped:
            total_score = group['Score'].sum()
            avg_score = group['Score'].mean()
            subject_scores = group[['Subject', 'Score']].values.tolist()
            
            # Generate the report card
            generate_report_card(student_id, student_name, total_score, avg_score, subject_scores)
    
    except FileNotFoundError:
        print("The file 'student_scores.xlsx' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

