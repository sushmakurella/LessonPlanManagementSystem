from django import forms

class PDFUploadForm(forms.Form):
    n = forms.IntegerField(
        label="Enter a number",
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number'})
    )
    pdf_file = forms.FileField(
        label="Upload a PDF",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )
