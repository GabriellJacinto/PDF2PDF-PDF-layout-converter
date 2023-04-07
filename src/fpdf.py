from fpdf import FPDF
#pdf_w = 210 mm
#pdf_h = 297 mm

HEIGHT = 297
WIDTH = 210

class PDF(FPDF):
    def lines(self):
        self.set_line_width = (0,0)
        self.line(5.0,5.0,205.0,5.0) # top one
        self.line(5.0,292.0,205.0,292.0) # bottom one
        self.line(5.0,5.0,5.0,292.0) # left one
        self.line(205.0,5.0,205.0,292.0) # right one

    def titles(self):
        self.set_xy(0.0,0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220, 50, 50)
        self.cell(w=210.0, h=40.0, align='C', txt="LORD OF THE PDFS", border=0)

if __name__ == "__main__":
    test = PDF()
    test.add_page()
    test.set_author('Moi')
    test.lines()
    test.titles()
    test.output("trial.pdf", "F")
