def handle_uploaded_file(f):
    with open('trials_csv' + f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)