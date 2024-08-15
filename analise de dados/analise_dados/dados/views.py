# dados/views.py
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, FileResponse
import os

def index(request):
    return render(request, 'dados/index.html')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        
        # Verificar se o nome do arquivo é "dados.xlsx"
        if uploaded_file.name != 'dados.xlsx':
            return HttpResponse("O arquivo enviado deve se chamar 'dados.xlsx'.", status=400)
        
        # Salvar o arquivo
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = fs.path(filename)
        
        # Aqui você pode processar o arquivo Excel se desejar
        
        return HttpResponse("Arquivo enviado e salvo com sucesso!")
    
    return render(request, 'dados/upload.html')

def download(request):
    # Caminho para o arquivo Excel que você deseja disponibilizar para download
    file_path = 'arquivos_download/dados.xlsx'
    
    if not os.path.exists(file_path):
        return HttpResponse("Arquivo não encontrado.", status=404)
    
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename='dados.xlsx')
    return response
