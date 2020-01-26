from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import psycopg2
from django.contrib.auth.models import User
from .models import LcmUrl

# Create your views here.
def home(request):
    return render(request, 'home.html')
def long_addition(request):
    return render(request,'long_addition.html')
def long_additions(request):
    res1=int(request.POST.get('instr1'))
    res2=int(request.POST.get('instr2'))
    res=res1+res2
    e=list(reversed(list(str(res))))
    g=[]
    f=[]
    for i in e:
        g.append(i)
        h=list(reversed(g))
        f.append(''.join(h))
    return render(request,'detail_long_addition.html',{'res1':res1,'res2':res2,'res':res,'e':e,'f':f,'i':i,'g':g})
def find_lcm(num1, num2):
        if(num1>num2):
            num = num1
            den = num2
        else:
            num = num2
            den = num1
        rem = num % den
        while(rem != 0):
            num = den
            den = rem
            rem = num % den
        gcd = den
        lcm = int(int(num1 * num2)/int(gcd))
        return lcm
def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(str(i))
        if n > 1:
            factors.append(str(n))
        return factors
def lcm_more(request):
    return render(request,'lcm_more.html')
def lcm_more1(request):
    x=request.POST.get('instr1')
    input_list=x.split(',')
    l=[]
    ll=x.split(',')
    l4=[]
    lll=[]
    for i in ll:
        lll.append(int(i))
    l4.append(str(lll)[1:-1])
    for i in input_list:
        l.append(int(i))

    num1 = int(l[0])
    num2 = int(l[1])
    lcm = find_lcm(num1, num2)

    for i in range(2, len(l)):
        lcm = find_lcm(lcm, int(l[i]))
    fact=prime_factors(lcm)
    l2=[]
    fact1=[]

    l6=[]
    for i in fact:
        for j in l:
            if int(j)%int(i)==0:
                l2.append(j)
        if len(l2)>=2:
            for k in l2:
                l[l.index(k)]= int(k)//int(i)
            fact1.append(i)
            l2=[]
        else:
            l2=[]
    if len(fact1)==0:
        fact1=[1]
    for i in fact1:
        for j in input_list:
            if int(j)%int(i)==0:

                input_list[input_list.index(j)]=int(j)//int(i)

            else:
                input_list[input_list.index(j)]=int(j)
        lx=str(input_list)[1:-1]
        lx2=str(input_list)
        l4.append(lx)
        l6.append(eval(lx2))
    if len(fact1)==1 and fact1[0]==1:
        x2='Given numbers has no common factors except 1. So, there LCM is their product'
    else:
        x2=zip(fact1,l4)
    x3=l4[-1]

    list_6=[]
    for i in range(len(l6[-1])):
        list_6.append(str(l6[-1][i]))
    l5=' x '.join(list_6)
    if len(fact1)==1 and fact1[0]==1:
        s1=l5
    else:
        s1=' x '.join(fact1)+' x '+l5
    if len(fact1)==1 and fact1[0]==1:
        return render(request,'lcm-more2.html',{'r':lcm,'z':l,'xx':x2,'xxx':x3,'xxxx':l4[0],'llll':s1})
    else:
        return render(request,'lcm_more1.html',{'r':lcm,'z':l,'xx':x2,'xxx':x3,'xxxx':l4[0],'llll':s1})

def lcm_more_slug(request, slug):
    u = LcmUrl.objects.get(url_string= slug)
    data = ','.join([str(x) for x in u.numbers])
    context_data = { "numbers": data}
    print("-----------------")
    return render(request, "lcm_result.html",context_data)


def add_numbers(request):
    numbers = request.POST.get('instr1').split(',')
    url = "lcm-" + "-".join(numbers)
    try:
      u = LcmUrl.objects.create(url_string= url, numbers=numbers)
      u.save()
      url = u.url_string
    except :
        pass
    return HttpResponse(url, status=200)
