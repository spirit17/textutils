# #this is created by me - khushal
from django.http import HttpResponse
from django.shortcuts import render
#
# def index(request):
#     return HttpResponse("hello khushal you got it")
#
# def about(request):
#     return HttpResponse("hello khushal about you got it")

#this is created by me - khushal
### this is for video 6
# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse('''<h2>Hey khushal</h2> <a href= "https://www.facebook.com/"> facebook </a><br>
#     <a href= "https://www.instagram.com/"> Instagram </a><br>
#     <a href= "https://github.com/stars/spirit17/topics?filter=topics"> Github </a><br>
#     <a href= "https://discord.com/channels/@me"> Discord </a><br>
#     <a href= "https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Youtube </a>''')
#
# def about(request):
#     return HttpResponse("hello khushal about you got it")

#this is created by me - khushal
# ## this is for video 9
# from django.http import HttpResponse
# from django.shortcuts import render
#
# # Code for video 9
#
# def index(request):
#     khus = {'name':'khushal','place':'simga'}
#     return render(request,  'index.html', khus)
#
#     # return HttpResponse("Home it's khushal")
#
# def removepunc(request):
#     return HttpResponse("remove punc ")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("capitalize first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("charcount ")


## this is for video 10
from django.http import HttpResponse
from django.shortcuts import render

# # Code for video 10
#
# def index(request):
#     return render(request,  'index.html', )
#
#     # return HttpResponse("Home it's khushal")
#
# def removepunc(request):
#     djtext = request.GET.get('text','defult')
#     print(djtext)
#     return HttpResponse("remove punc ")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("capitalize first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("charcount ")

# Code for video 11
#
# def index(request):
#     return render(request,  'index.html', )
#
#     # return HttpResponse("Home it's khushal")
#
# def analyze(request):
#     djtext = request.GET.get('text','defult')
#     removepunc = request.GET.get('removepunc','off')
#     print(removepunc)
#     print(djtext)
#     return HttpResponse("remove punc ")

#
# def index(request):
#     return render(request,  'index.html', )
#
#     # return HttpResponse("Home it's khushal")
#
# def analyze(request):
#     djtext = request.GET.get('text','defult')
#     removepunc = request.GET.get('removepunc','off')
#     fullcap = request.GET.get('fullcap','off')
#     newlineremover = request.GET.get('newlineremover', 'off')
#     extraspaceemove = request.GET.get('extraspaceemove', 'off')
#     Countcharecters = request.GET.get('Countcharecters', 'off')
#
#     if (removepunc == "on"):
#         punctuations = '''!()-{}[]:;,<>""''./?@#$%^&*_~'''
#         analyzed = " "
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#         params = {'Purpose':'Removed Punctuation','analyed_text': analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
#
#     if(fullcap=="on"):
#         analyzed =""
#         for char in djtext:
#             analyzed = analyzed + char.upper()
#
#         params = {'Purpose': 'Changed to Uppercase', 'analyed_text': analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
#
#
#     if (newlineremover == "on"):
#         analyzed = ""
#         for char in djtext:
#             if char !="\n":
#                 analyzed = analyzed + char
#
#         params = {'Purpose': 'New line remover', 'analyed_text': analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
#
#
#     if(extraspaceemove =="on"):
#         analyzed = ""
#         for index, char in enumerate(djtext):
#             if not(djtext[index] == " " and djtext[index+1]==" "):
#                 analyzed = analyzed + char
#
#         params = {'Purpose': 'Exter space remover', 'analyed_text': analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
#
#     if (Countcharecters == "on"):
#         analyzed = ""
#         count = 0;
#         for char in range(0, len(djtext)):
#             if (djtext != ''):
#                 count = count + 1;
#                 analyzed = count
#         params = {'Purpose': 'chareters couter', 'analyed_text': analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
#
#
#     else:
#         return HttpResponse("Error")
#
#     return render(request, 'analyze.html', params)



def index(request):
    return render(request,  'index.html')

    # return HttpResponse("Home it's khushal")

def analyze(request):
    djtext = request.GET.get('text','defult')
    removepunc = request.GET.get('removepunc','off')
    fullcap = request.GET.get('fullcap','off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremove = request.GET.get('extraspaceremove', 'off')
    Countcharecters = request.GET.get('Countcharecters', 'off')

    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./"?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'Purpose':'Removed Punctuation','analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcap=="on"):
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'Purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)


    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'Purpose': 'New line remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)


    if (extraspaceremove == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (Countcharecters == "on"):
        analyzed = ""
        count = 0;
        # count = len(djtext);
        # for char in range(0, len(djtext)):
        #     if (djtext != ''):
        #         count = count + 1;
        #         analyzed = count
        #         print(analyzed + count)
        for char in djtext:
             analyzed = len(djtext);
        params = {'Purpose': 'chareters couter', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if (removepunc != "on" and fullcap !="on" and newlineremover != "on" and extraspaceremove !="on" and Countcharecters != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)