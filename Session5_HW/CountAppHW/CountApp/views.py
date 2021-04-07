from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text=request.POST['text']
    total_len = len(text)
    no_space_len=len(text.replace(" ",""))
    if len(text) > 0:
        word_count = text.count(" ") + 1
    else:
        word_count = 0

    return render(request, 'result.html', {
        'text': text,
        'total_len': total_len, 
        'no_space_len':no_space_len,
        'word_count' : word_count,
    })