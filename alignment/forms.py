from django import forms

class SequenceUploadForm(forms.Form):
    file = forms.FileField(label='Selecciona un archivo de secuencia')
    
    # Ampliar las opciones de formato para incluir todos los formatos soportados por SeqIO
    format_choices = [
        ('fasta', 'FASTA'),
        ('fastq', 'FASTQ'),
        ('genbank', 'GenBank'),
        ('embl', 'EMBL'),
        ('clustal', 'Clustal'),
        ('phylip', 'PHYLIP'),
        ('nexus', 'NEXUS'),
        ('pdb', 'PDB'),
        ('mmcif', 'mmCIF'),
        ('sam', 'SAM'),
        ('bam', 'BAM'),
        ('gff', 'GFF'),
        ('gtf', 'GTF'),
        ('vcf', 'VCF'),
    ]
    
    format = forms.ChoiceField(choices=format_choices, label='Formato de archivo')