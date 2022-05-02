from django.shortcuts import render
from django.http import HttpResponse
def testPaper(request):
    q="Who developed C-Language"
    a="Ken Thompson"
    b="Dennis Ritchi"
    c="Bjarne Stroustrup"
    d="Guido Van Rossum"
    d1={'que':q,'a':a,'b':b,'c':c,'d':d}
    res=render(request,'exam/show_test.html',d1)
    return res
def testResult(request):
    s="Display result on my website"
    return HttpResponse(s)
        
