from django.shortcuts import render
from .forms import SequenceUploadForm
import numpy as np
from Bio import SeqIO
from django.contrib.auth.decorators import login_required
import io

@login_required
def upload_sequence(request):
    form = SequenceUploadForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        uploaded_file1 = request.FILES['file1']
        uploaded_file2 = request.FILES['file2']
        file_format1 = form.cleaned_data['format']
        file_format2 = form.cleaned_data['format']

        try:
            # Leer las secuencias del archivo subido
            seq1 = SeqIO.read(io.TextIOWrapper(uploaded_file1, encoding='utf-8'), file_format1)
            seq2 = SeqIO.read(io.TextIOWrapper(uploaded_file2, encoding='utf-8'), file_format2)

            # Aplicar el algoritmo Needleman-Wunsch
            alignment, score = needleman_wunsch(str(seq1.seq), str(seq2.seq))

            return render(request, 'result.html', {
                'alignment': alignment,
                'score': score,
            })
        except Exception as e:
            return render(request, 'upload.html', {'form': form, 'error': str(e)})

    return render(request, 'upload.html', {'form': form})

def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    # Inicialización de la matriz
    n = len(seq1) + 1
    m = len(seq2) + 1
    score_matrix = np.zeros((n, m), dtype=int)

    # Inicialización de la primera fila y columna
    for i in range(n):
        score_matrix[i][0] = gap * i
    for j in range(m):
        score_matrix[0][j] = gap * j

    # Llenado de la matriz
    for i in range(1, n):
        for j in range(1, m):
            diag = score_matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            up = score_matrix[i-1][j] + gap
            left = score_matrix[i][j-1] + gap
            score_matrix[i][j] = max(diag, up, left)

    # Backtracking para obtener el alineamiento
    alignment_a = ""
    alignment_b = ""
    i, j = n - 1, m - 1

    while i > 0 or j > 0:
        current_score = score_matrix[i][j]
        if i > 0 and j > 0 and current_score == score_matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch):
            alignment_a += seq1[i-1]
            alignment_b += seq2[j-1]
            i -= 1
            j -= 1
        elif i > 0 and current_score == score_matrix[i-1][j] + gap:
            alignment_a += seq1[i-1]
            alignment_b += "-"
            i -= 1
        else:
            alignment_a += "-"
            alignment_b += seq2[j-1]
            j -= 1

    return (alignment_a[::-1], alignment_b[::-1]), score_matrix[n-1][m-1]